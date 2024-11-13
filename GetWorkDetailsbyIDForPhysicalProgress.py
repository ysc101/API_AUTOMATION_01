import requests
from New_token import bearer_token
url="http://192.168.0.162:8082/api/PhysicalProgress/GetWorkDetailsbyIDForPhysicalProgress"
headers={
"Authorization": f"Bearer {bearer_token}"
}
params= {
"WorkID":"10"
}
response=requests.get(url,headers=headers, params=params)

if response.status_code==200:
    try:
        data=response.json()
        print("Response Data: " ,data)
    except requests.exceptions.JSONDecodeError:
        print("Response not in json")
else:
    print(f"Error:Status code: {response.status_code}")
    print(response.text)


