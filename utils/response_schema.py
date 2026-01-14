from typing import Any


def response_dict(message: str, data: Any = None) -> dict:
    return {
        "message"   : message,
        "data"      : data,
    }