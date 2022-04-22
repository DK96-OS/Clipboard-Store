""" Key Validation """


def isValid(key: str) -> bool:
    """
    Determines if the String is a valid Key.
    If Key is invalid, a message is printed containing details
    """

    # Check for Empty String
    if key == None or len(key) < 1:
        print("Key Cannot be Empty")
        return False
    
    # Limit Key Length
    elif len(key) > 1000:
        print("Key Is Too Large")
        return False
    
    # Reserved and inappropriate characters
    elif key in ('*', '_', '"'):
        print("Illegal Key : " + key)
        return False
    
    # Key is Valid
    return True
