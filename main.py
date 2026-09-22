import requests

print("Hello, World!")

r = requests.get("https://google.com", timeout=10)
print(r.status_code)