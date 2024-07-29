from dotenv import load_dotenv
import os

def test_updatee_req():
    load_dotenv()
    url = os.getenv("URL")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username)
    print(password)
    print(url)
