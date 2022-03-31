import pytest

from pathlib import Path
from geonames.translit.translit import RussianTransliterator

test_transliterator_rules_filepath = Path("../geonames/translit/rules.json")


def test_init_transliterator():
    """
    Tests that transliterator initializes properly.
    :return:
    """
    _ = RussianTransliterator(test_transliterator_rules_filepath)


@pytest.mark.parametrize("input_text, expected", [
    ("Смородинка", "Smorodinka"),
    ("Красногвардейский", "Krasnogvardeyskiy"),
    ("Голый Камень", "Golyy Kamen’")
])
def test_transliterator_convert(input_text: str, expected: str):
    """
    Tests proper transliterator text conversion.
    :return:
    """
    t = RussianTransliterator(test_transliterator_rules_filepath)

    assert t.convert(input_text) == expected
