def validate_credentials(username, password):
    return username == "admin" and password == "1234"

def generate_token(username):
    return f"TOKEN_{username}"
