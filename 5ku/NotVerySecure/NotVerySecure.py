def alphanumeric(password):
    return False if password is None or password =="" else all(c.isalnum() for c in password)


""" best
def alphanumeric(string):
    return string.isalnum()
"""
