import json
import logging
from pathlib import Path

from typing import Dict

logger = logging.getLogger(__name__)

# common rules for russian transliterator
_COMMON_RULES = (u"абвгдеёжзийклмнопрстуфшъыьэюАБВГДЕЁЖЗИЙКЛМНОПРСТУФШЪЫЬЭЮ",
                 u"abvgdeejzijklmnoprstufs’y’euABVGDEEJZIJKLMNOPRSTUFS’Y’EU")


def _build_common_rules() -> Dict[int, str]:
    return {ord(a): ord(b) for a, b in zip(*_COMMON_RULES)}


class RussianTransliterator:
    """
    Russian transliterator, that can be configured via json file of rules.
    """
    def __init__(self, rules_filepath: Path):
        """
        Init russian transliterator with specific rules from json file
        :param rules_filepath: file path to json rule configuration
        """
        if not rules_filepath.exists():
            raise FileNotFoundError(f"rule file not found: {str(rules_filepath)}")

        self._rules = _build_common_rules()

        with open(rules_filepath, 'rb') as fp:
            specific_rules: Dict[str, str] = json.load(fp)["specific"]

            for key, val in specific_rules.items():
                self._rules[ord(str(key))] = val
                self._rules[ord(str(key).upper())] = str(val).title()

        logger.info("Russian transliterator has been initialized")

    def convert(self, text: str) -> str:
        """
        Converts text in english transliteration
        :param text: russian text
        :return: english transliteration of input text
        """
        return text.translate(self._rules)
