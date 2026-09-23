import requests

print("Hello, World!")

url = "https://google.com"
r = requests.get(url, timeout=10)
print(f"Status code from {url}: {r.status_code}")