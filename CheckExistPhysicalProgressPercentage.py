import requests

from New_token import bearer_token

url="http://192.168.0.162:8082/api/PhysicalProgress/CheckExistPhysicalProgressPercentage"
headers={
    "Authorization":f"bearer {bearer_token}"
}
params={
           "HeadcodeID":"1",
           "FYID":"8",
           "WorkID":"33312",
           "ZPID":"3",
            "DEPTID":"9"
}
response=requests.get(url,headers=headers,params=params)

if response.status_code==200:
    try:
        data=response.json()
        print("Response Data:",data)
    except requests.exceptions.JSONDecodeError():
        print("Output not in Json Format")

else:
    print(f"Error:Staus code{response.status_code}")
    print(response.text)

