from auth import handle_login
from config import load_config

def main():
    config = load_config("config.yaml")
    user_input = {"username": "admin", "password": "1234"}
    result = handle_login(user_input)
    print(result)

if __name__ == "__main__":
    main()
