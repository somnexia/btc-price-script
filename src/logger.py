from config import SERVICE_NAME


def _format_value(value) -> str:
    text = str(value).replace('"', '\\"')
    if any(char.isspace() for char in text):
        return f'"{text}"'
    return text


def _escape_message(message: str) -> str:
    return message.replace('"', '\\"')


def log(level: str, message: str, **fields) -> None:
    parts = [f"[{level}]", f"service={SERVICE_NAME}"]
    parts.extend(f"{key}={_format_value(value)}" for key, value in fields.items())
    parts.append(f'message="{_escape_message(message)}"')
    print(" ".join(parts), flush=True)


def info(message: str, **fields) -> None:
    log("INFO", message, **fields)


def warning(message: str, **fields) -> None:
    log("WARN", message, **fields)


def error(message: str, **fields) -> None:
    log("ERROR", message, **fields)