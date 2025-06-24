from utils import validate_credentials, generate_token

def handle_login(request):
    if not validate_credentials(request["username"], request["password"]):
        return {"status": "fail"}
    token = generate_token(request["username"])
    return {"status": "success", "token": token}
