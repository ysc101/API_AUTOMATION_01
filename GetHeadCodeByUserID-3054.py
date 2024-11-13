import requests
from New_token import bearer_token
url="http://192.168.0.162:8082/api/HeadCodeType/GetHeadCodeByUserID"
headers={
"Authorization": f"Bearer {bearer_token}"
}
params={
"ZPID":"3",
"DeptID":"9",
"UserID":"10036"
}

response=requests.get(url, headers=headers,params=params)

if response.status_code==200:
    try:
        data=(response.json())
        print("Response Data ",data)
    except requests.exceptions.JSONDecodeError():
        print("Output not in json format")
else:
    print(f"Error:Staus code{response.status_code}")
    print(response.text)


