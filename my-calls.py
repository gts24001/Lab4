import httpx

url = "http://127.0.0.1:5000/"

response = httpx.get(url)
print(response.status_code)
print(response)


response = httpx.get(url)
print(response.status_code)
print(response.text)

mydata = {
    "text": "Hello Phil!",
    "param2": "Making a POST request",
    "body": "my own value"
}

# A POST request to the API
response = httpx.post(url + "echo", data=mydata)

# Print the response
print(response.status_code)
print(response.text) 

# A GET request to the API
# Example: Prime number (97)
response = httpx.get(url + "factors?inINT=97")
print(response.status_code)
print(response.text)

# Example: Non-prime number (100)
response = httpx.get(url + "factors?inINT=100")
print(response.status_code)
print(response.text)

# Example: Edge case (1)
response = httpx.get(url + "factors?inINT=1")
print(response.status_code)
print(response.text)

# Example: Invalid input (missing parameter)
response = httpx.get(url + "factors")
print(response.status_code)
print(response.text)
