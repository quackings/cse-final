from enum import Enum
from typing import Union, Optional

class colors(Enum):
    NONE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6

    @staticmethod
    def _returnColorCode(color: Union[colors, int]) -> str:
        return (color.value if isinstance(color, colors) else color)

    @classmethod
    def light(cls, text: str, color: Union[colors, int]) -> str:
        return f"\033[9{cls._returnColorCode(color)}m{text}{cls.NONE}"
    
    @classmethod
    def dark(cls, text: str, color: Union[colors, int]) -> str:
        return f"\033[3{cls._returnColorCode(color)}m{text}{cls.NONE}"

class terminal:
    @staticmethod
    def clear() -> None:
        print('\033c')