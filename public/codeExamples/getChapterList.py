import requests

url = "https://quranapi.pages.dev/api/surah.json"
res = requests.get(url)
data = res.json()

fatiha = data[0]
print(fatiha)
