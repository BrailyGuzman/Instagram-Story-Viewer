# Please stop forking my code if you aren't making any changes.

from time import sleep
import requests
from random import randint
import stdiomask

session = requests.Session()
username = input("[+] Username: ")
password = stdiomask.getpass(prompt="[+] Password: ", mask='*')

url = "https://www.instagram.com/accounts/login/ajax/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "x-csrftoken": "flABydJVnZRJYaGedv2ItjmC9UI77bqW",
    "mid": "xgDrB4ZsEzKAr1Tqyb5QlmbS2oa6JqCt"
}
data = {
"enc_password": "#PWD_INSTAGRAM_BROWSER:0:1651709336:" + password,
"username": username,
"queryParams": "{}",
"optIntoOneTap": "false",
}
data = session.post(url, headers=headers, data=data)
print(data.text)
if "userId" in data.text:
    session_id = data.cookies.get("sessionid")
    headers["cookie"] = f"sessionid={session_id}"
    print("Successfully Logged In")
    print("Enter The Person's Username")
    target = input("[?] Target: ")
    target_info = session.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={target}", headers=headers)
    target_stories = []
    userId = target_info.json()["data"] ["user"] ["id"]
    x = (f"https://i.instagram.com/api/v1/feed/user/{userId}/story/")
    headers["user-agent"] = "Instagram 85.0.0.21.100 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)"
    response = session.get(x, headers=headers,)
    story_items = response.json()["reel"] ["items"]
    
    for story in story_items:
        story_url = story["image_versions2"] ["candidates"] [0] ["url"]
        target_stories.append(story_url)

    for collected_story in target_stories:
        response = session.get(collected_story)
        with open (f"{randint(0, 100)}.jpeg", "wb") as writer:
            writer.write(response.content)
