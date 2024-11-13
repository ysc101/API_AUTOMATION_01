# Define URL and headers
import requests
from New_token import bearer_token

url = "http://192.168.0.162:8082/api/TechnicalSanctionAPI/GET_TechnicalSactionNumberInbox"
headers = {
    "Authorization": f"Bearer {bearer_token}"  # Replace with actual token
}
params={
"ZPID":"3",
"UserID":"10036"
}

# Make the GET request with headers
response = requests.get(url, headers=headers,params=params)

# Process the response as above
if response.status_code == 200:
    try:
        data = response.json()
        print("Response Data:", data)
    except requests.exceptions.JSONDecodeError:
        print("The response is not in JSON format.")
else:
    print(f"Error: Status code {response.status_code}")
    print(response.text)
