# Define URL and query parameters
import requests

url = "http://192.168.0.162:8082/api/LoginApi/GetUserDetails"
params = {
    "Username": "AUDITWORK4",
    "Password": "Pass@123"
}

# Make the GET request with parameters
response = requests.get(url, params=params)

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

#
# if response.status_code == 200:
#     # Parse the token from the response (assuming it’s in JSON and under 'access_token')
#     token_data = response.json()
#     bearer_token = token_data.get("access_token")
#
#     # Step 2: Save the token to token.py
#     with open("New_token.py", "w") as token_file:
#         token_file.write(f'bearer_token = "{bearer_token}"\n')
#     print("Token saved successfully to New_token.py")
# else:
#     print(f"Failed to retrieve token. Status code: {response.status_code}")
