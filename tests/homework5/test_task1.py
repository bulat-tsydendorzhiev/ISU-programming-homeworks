import pytest

from homework5.task1 import (
    get_default_output_path,
    get_roles_and_text_lines,
    group_roles_text,
    write_roles_text,
)


def write_play(tmp_path, content: str) -> str:
    path = tmp_path / "play.txt"
    path.write_text(content, encoding="utf-8")
    return str(path)


PLAY = """\
roles:
Городничий
Аммос Федорович
Артемий Филиппович
Лука Лукич

textLines:
Городничий: Сообщаю вам неприятное известие: к нам едет ревизор.
Аммос Федорович: Как ревизор?
Артемий Филиппович: Как ревизор?
Городничий: Ревизор из Петербурга, инкогнито.
Аммос Федорович: Вот те на!
Артемий Филиппович: Вот не было заботы, так подай!
Лука Лукич: Господи боже! Еще и с секретным предписаньем!
"""


def test_reads_roles_and_lines_preserving_order(tmp_path):
    roles, text_lines = get_roles_and_text_lines(write_play(tmp_path, PLAY))

    assert roles == ["Городничий", "Аммос Федорович", "Артемий Филиппович", "Лука Лукич"]
    assert len(text_lines) == 7
    assert text_lines[0] == "Городничий: Сообщаю вам неприятное известие: к нам едет ревизор."
    assert text_lines[-1] == "Лука Лукич: Господи боже! Еще и с секретным предписаньем!"


@pytest.mark.parametrize(
    "content, expected_roles, expected_lines",
    [
        pytest.param("roles:\nА\nБ\n", ["А", "Б"], [], id="without_text_lines"),
        pytest.param("textLines:\nА: раз\n", [], ["А: раз"], id="without_roles"),
        pytest.param(
            "textLines:\nА: раз\n   продолжение\n",
            [],
            ["А: раз", "продолжение"],
            id="strips_indentation",
        ),
        pytest.param("", [], [], id="empty_file"),
    ],
)
def test_section_boundaries(tmp_path, content, expected_roles, expected_lines):
    assert get_roles_and_text_lines(write_play(tmp_path, content)) == (
        expected_roles,
        expected_lines,
    )


def test_replicas_order_follows_roles_list():
    result = group_roles_text(["Б", "А"], ["А: раз", "Б: два"])

    assert list(result) == ["Б", "А"]


def test_role_name_inside_text_is_not_split_off():
    roles = ["Лука", "Лука Лукич"]
    text_lines = [
        "Лука Лукич: Лука: я иду",
        'Лука: он сказал: "Лука Лукич: ухожу"',
    ]

    assert group_roles_text(roles, text_lines) == {
        "Лука Лукич": [(1, "Лука: я иду")],
        "Лука": [(2, 'он сказал: "Лука Лукич: ухожу"')],
    }


def test_prefixed_role_names_are_distinguished():
    roles = ["Лука", "Лука Лукич", "Лука Лука"]
    text_lines = ["Лука Лукич: раз", "Лука Лука: два", "Лука: три"]

    assert group_roles_text(roles, text_lines) == {
        "Лука": [(3, "три")],
        "Лука Лукич": [(1, "раз")],
        "Лука Лука": [(2, "два")],
    }


def test_multiline_replica_is_grouped_as_one():
    roles = ["Лука", "Лука Лукич"]
    text_lines = [
        "Лука: привет",
        "текст: продолжение",
        "и Лука Лукич: вложенная роль",
        "Лука Лукич: пока",
    ]

    assert group_roles_text(roles, text_lines) == {
        "Лука": [(1, "привет\nтекст: продолжение\nи Лука Лукич: вложенная роль")],
        "Лука Лукич": [(4, "пока")],
    }


def test_role_line_without_text_is_filled_by_following_lines():
    roles = ["А", "Б"]
    text_lines = [
        "А:",
        "первая строка",
        "вторая строка",
        "Б: ответ",
    ]

    assert group_roles_text(roles, text_lines) == {
        "А": [(2, "первая строка\nвторая строка")],
        "Б": [(4, "ответ")],
    }


def test_grouping_does_not_modify_inputs():
    roles = ["А", "Б"]
    text_lines = ["А: раз", "  два", "Б: три"]

    group_roles_text(roles, text_lines)

    assert roles == ["А", "Б"]
    assert text_lines == ["А: раз", "  два", "Б: три"]


def test_default_output_path_is_next_to_input(tmp_path):
    input_path = tmp_path / "roles.txt"

    assert get_default_output_path(str(input_path)) == str(tmp_path / "roles.grouped.txt")


def test_write_roles_text_aligns_multiline_replicas(tmp_path):
    roles_text = {
        "а": [(2, "первая реплика\nвторая"), (10, "третья\nчетвёртая")],
        "б": [(12, "пятая")],
    }
    output_path = tmp_path / "result.txt"

    write_roles_text(str(output_path), roles_text)

    assert output_path.read_text(encoding="utf-8") == (
        "а:\n"
        "2) первая реплика\n"
        "   вторая\n"
        "10) третья\n"
        "    четвёртая\n"
        "\n"
        "б:\n"
        "12) пятая\n"
    )
