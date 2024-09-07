import requests

reqUrl = "http://localhost:8000/send_name/Salomon"

headersList = {
 "Accept": "*/*",
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)