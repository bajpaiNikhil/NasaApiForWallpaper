# Our POA
# Step -1 Establish connection
# Step -2 Download the image
# Step -3 Set the image as wallpaper
import ctypes
import datetime
import json
import random
import requests


def establishConnection(dateString):
    API_KEY = "DEMO_KEY"
    url = "https://api.nasa.gov/planetary/apod"

    passingParameters = {
        "api_key": API_KEY,
        "hd": "True",
        "date": dateString
    }
    response = requests.get(url=url, params=passingParameters)
    responseJson = json.loads(response.text)
    if response.status_code == 200 and responseJson["hdurl"] is not None:
        responseJson["code"] = 200
        return responseJson
    else:
        responseJson["code"] = 400
        return responseJson


def randomDate():
    date = datetime.date.today()
    randomYear = random.randint(1997, date.year)
    randomMonth = random.randint(1, 12)
    randomDay = random.randint(1, 30)
    return str(randomYear) + "-" + str(randomMonth) + "-" + str(randomDay)


def savingImage(jsonData):
    image_url = jsonData["hdurl"]
    file = requests.get(image_url)
    print(file)
    if file.status_code == 200:
        with open("image1.jpg", "wb") as f:
            f.write(file.content)
            print("success")
        f.close()


def displayImageAsWallpaper(AbsoluteImagePath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, AbsoluteImagePath, 0)


if __name__ == '__main__':
    while True:
        metaResponse = establishConnection(randomDate())
        if metaResponse["code"] == 200:
            print(metaResponse)
            savingImage(metaResponse)
            displayImageAsWallpaper(r"AbsoluteImagePath")
            break
