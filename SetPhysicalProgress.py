import requests
from New_token import bearer_token

url = "http://192.168.0.162:8082/api/PhysicalProgress/SetPhysicalProgress"

headers = {
    "Authorization": f"Bearer {bearer_token}"
}

payload = {
    "zpid": "3",
    "deptID": "9",
    "headCodeID": "1",
    "financialYearID": "8",
    "workDetailsID": "333123",
    "workDetailsUID": "333123",
    "physicalProgressPercentage": "5",
    "remark": "TestEntry",
    "uploadImagesList": "123string.jpg",
    "userID": "10340"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    try:
        data = response.json()
        print(f"Response Data:", data)
    except requests.exceptions.JSONDecodeError:
        print("Output not in JSON format")
else:
    print(f"Error: Status code {response.status_code}")
    print(response.text)
