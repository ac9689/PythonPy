import requests

response = requests.get("https://github.com/jaiswaladi246/Python-4-DevOps/blob/main/Day-6.md")

print(response.status_code)  # Shows 200 if OK
print(response.text)         # Shows the website's content
