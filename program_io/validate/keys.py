""" Key Validation """


def is_valid(key: str) -> bool:
    """
    Determines if the String is a valid Key.
    If Key is invalid, a message is printed containing details
    """
    # Check for Empty String
    if key is None or len(key) < 1:
        print("Key Cannot be Empty")
        return False
    # Limit Key Length
    if len(key) > 1000:
        print("Key Is Too Large")
        return False
    # Reserved and inappropriate characters
    if key in ('*', '_', '"'):
        print("Illegal Key : " + key)
        return False
    # Space only strings cannot be keys
    if str.isspace(key):
        return False
    # Key is Valid
    return True
