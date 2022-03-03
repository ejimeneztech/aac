import requests
#from aws_requests_auth import aws_auth

POST_ENDPOINT = "https://q6j8s8rwj1.execute-api.us-west-2.amazonaws.com/dev/aac-get-post"
response = requests.get(POST_ENDPOINT, json={"postId":"*"})
response.raise_for_status()
data = response.json()

print(data)