import requests

BASE = "http://176.100.37.220:19999"

def get(chart):
    url = f"{BASE}/api/v1/data?chart={chart}&after=-1"
    return requests.get(url).json()

cpu  = get("system.cpu")
ram  = get("system.ram")
load = get("system.load")

print("CPU:", cpu["data"][0])
print("RAM:", ram["data"][0])
print("Load:", load["data"][0])
