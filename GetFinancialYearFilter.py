# Define URL and headers
import requests
from New_token import bearer_token

url = "http://192.168.0.162:8082/api/FinancialYearFilter/GetFinancialYearFilter"
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

# Make the GET request with headers
response = requests.get(url, headers=headers)

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
