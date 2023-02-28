import requests

# server url
from record_sound import record_sound

URL = "http://127.0.0.1:5000/predict"


# audio file we'd like to send for predicting keyword
# FILE_PATH = "test.wav"

def post_file():
    file_name=record_sound()
    file = open(file_name, "rb") #rb -> read binary
    response = requests.post(URL, files={"file": file})
    data=response.json()
    print(data["text"])



if __name__ == "__main__":
    while True:
        post_file()