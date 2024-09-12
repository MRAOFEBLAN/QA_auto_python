
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

GITHUB_API_URL = "https://api.github.com/user/repos"

def create_repository():
    response = requests.post(
        GITHUB_API_URL,
        json={"name": REPO_NAME, "private": False},
        auth=(GITHUB_USERNAME, GITHUB_TOKEN)

    )


    return response

def check_repository():
    response = requests.get(
        f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}",

        auth=(GITHUB_USERNAME, GITHUB_TOKEN)
    )

    return response.status_code == 200

def delete_repository():    
    response = requests.delete(
        f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}",

        auth=(GITHUB_USERNAME, GITHUB_TOKEN)

    )

    return response

def run_tests():   
    print("Creating repository...")
    
    create_response = create_repository()
    print(f"Create response: {create_response.status_code} - {create_response.json()}")

    print("Checking repository...")
    exists = check_repository()
    print(f"Repository exists: {exists}")

    if exists:
        print("Deleting repository...")
        delete_response = delete_repository()
        print(f"Delete response: {delete_response.status_code}")



if __name__ == "__main__":
    run_tests()
