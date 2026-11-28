import json
import pytest
from homework10.app import (
    create_users_json,
    parse_users_json,
    format_users_for_display,
    handle_parse
)


def test_create_users_json():
    test_users = [
        {
            "login": "admin", 
            "last_login": "2026-11-28 12:00:00", 
            "session_duration_minutes": 15
        }
    ]
    
    result = create_users_json(test_users)
    parsed = json.loads(result)
    
    assert isinstance(parsed, list)
    assert parsed[0]["login"] == "admin"
    assert parsed[0]["last_login"] == "2026-11-28 12:00:00"
    assert parsed[0]["session_duration_minutes"] == 15


def test_parse_users_json_success():
    raw_json = '[{"login": "guest", "last_login": "2026-11-28 14:00:00", "session_duration_minutes": 5}]'
    
    result = parse_users_json(raw_json)
    
    assert len(result) == 1
    assert result[0]["login"] == "guest"
    assert result[0]["last_login"] == "2026-11-28 14:00:00"
    assert result[0]["session_duration_minutes"] == 5


def test_parse_users_json_not_list():
    raw_json = '{"login": "admin"}'
    
    with pytest.raises(ValueError, match="Корневой элемент JSON должен быть списком."):
        parse_users_json(raw_json)


def test_parse_users_json_broken_format():
    raw_json = '[{"login": "admin"'
    
    with pytest.raises(ValueError, match="Некорректный формат JSON:"):
        parse_users_json(raw_json)


def test_format_users_for_display_empty():
    assert format_users_for_display([]) == "Список пользователей пуст."


def test_format_users_for_display_with_data():
    test_users = [{"login": "user1", "last_login": "2026-11-28 10:00:00", "session_duration_minutes": 60}]
    
    result = format_users_for_display(test_users)
    
    assert "Найдено пользователей: 1" in result
    assert "Логин: user1" in result
    assert "Последняя сессия: 2026-11-28 10:00:00" in result
    assert "Длительность сессии: 60" in result


def test_handle_parse_file_not_found(capsys):
    handle_parse("absent_file.json")
    
    captured = capsys.readouterr().out
    assert "Ошибка: Файл" in captured and "не найден" in captured


def test_handle_parse_wrong_extension(tmp_path, capsys):
    wrong_file = tmp_path / "test_data.html"
    wrong_file.write_text("some data")
    
    handle_parse(str(wrong_file))
    
    captured = capsys.readouterr().out
    assert "Ошибка: файл должен заканчиваться на .json" in captured


def test_handle_parse_success(tmp_path, capsys):
    json_file = tmp_path / "users_data.json"
    valid_content = '[{"login": "file_user", "last_login": "2026-11-28 11:00:00", "session_duration_minutes": 30}]'
    json_file.write_text(valid_content, encoding="utf-8")
    
    handle_parse(str(json_file))
    
    captured = capsys.readouterr().out
    assert "Найдено пользователей: 1" in captured
    assert "Логин: file_user" in captured