def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if 'hello' in lowered:
        return 'Hello there'

