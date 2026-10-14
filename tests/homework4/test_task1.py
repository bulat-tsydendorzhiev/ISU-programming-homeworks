import pytest

from homework4.task1 import invert_dictionary


@pytest.mark.parametrize(
    ("eng_to_lat", "expected"),
    [
        ({"cat": ["felis"]},
         {"felis": ["cat"]}),
        ({"one": ["un", "uno"]},
         {"un": ["one"],
          "uno": ["one"]}),
        ({"one": ["numero"],
          "two": ["numero"]},
          {"numero": ["one", "two"]}),
        ({"one": ["numero", "unit"],
          "two": ["due"]},
          {"due": ["two"],
           "numero": ["one"],
           "unit": ["one"]}),
        ({"apple": ["malum", "pomum", "popula"],
            "fruit": ["baca", "bacca", "popum"],
            "punishment": ["malum", "multa"]},
            {"baca": ["fruit"],
             "bacca": ["fruit"],
             "malum": ["apple", "punishment"],
             "multa": ["punishment"],
             "pomum": ["apple"],
             "popula": ["apple"],
             "popum": ["fruit"],})
    ],
)
def test_invert_dictionary(eng_to_lat, expected):
    assert invert_dictionary(eng_to_lat) == expected


@pytest.mark.parametrize(
    ("eng_to_lat", "expected_latin_words_count"),
    [
        ({"one": ["numero"],
          "two": ["due"]},
         2),
        ({"one": ["numero", "unit"],
          "two": ["numero", "due"]},
          3),
        ({"one": ["numero", "numero"]},
         1),
         ({"apple": ["malum", "pomum", "popula"],
                    "fruit": ["baca", "bacca", "popum"],
                    "punishment": ["malum", "multa"]},
         7)
    ],
)
def test_number_of_latin_words(eng_to_lat, expected_latin_words_count):
    assert len(invert_dictionary(eng_to_lat)) == expected_latin_words_count


def test_latin_words_are_sorted_by_key():
    result = invert_dictionary({"one": ["tre"], "two": ["due"], "three": ["tre"]})

    assert list(result) == ["due", "tre"]


def test_english_words_keep_order_of_source_dictionary():
    result = invert_dictionary({"one": ["numero"], "three": ["numero"], "two": ["numero"]})

    assert result["numero"] == ["one", "three", "two"]


def test_source_dictionary_is_not_modified():
    eng_to_lat = {"one": ["numero"], "two": ["due"]}

    invert_dictionary(eng_to_lat)

    assert eng_to_lat == {"one": ["numero"], "two": ["due"]}
