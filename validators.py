"""Utils for Flask app."""
from typing import Union


def is_int(value: Union[int, float, str]) -> bool:
    """Checking for number type."""
    try:
        int(value)
        return True
    except Exception:
        return False


def is_positive_int(value: int) -> bool:
    """Checking for positive number."""
    try:
        if int(value) >= 0:
            return True
    except Exception:
        return False
