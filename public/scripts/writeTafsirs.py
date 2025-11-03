import os, json
from dotenv import load_dotenv
from helper import pprint, makeJson, getSurahName, readJsonFile

load_dotenv()


folderPath = "api/tafsir"

os.makedirs(folderPath, exist_ok=True)

with open("Data/tafsirs.json", "rb") as file:
    tafsirs = json.load(file)


# a = tafsirs[0][0]["tafsirs"]
# pprint(a[0].keys())


# exit(1)

for surahNo, surah in enumerate(tafsirs, 1):
    surahName = getSurahName(surahNo)

    surahTafsirPath = f"{folderPath}/{surahNo}.json"
    surahTafsir = {
        "surahName": surahName,
        "totalVerse": len(surah),
        "tafsirs": [i["tafsirs"] for i in surah],
    }
    makeJson(surahTafsirPath, surahTafsir)

    for tafsir in surah:
        ayahNo = tafsir["ayahNo"]
        # tafsirData = tafsir["tafsir"]
        # author = tafsirData["author"]
        # groupVerse = tafsirData["groupVerse"]
        # content = tafsirData["content"]  # tafsir in `MD` format

        ayahTafsirPath = f"{folderPath}/{surahNo}_{ayahNo}.json"
        makeJson(ayahTafsirPath, tafsir)

        # print(f"Tafsir Written {ayahTafsirPath}", end="\r")

print(f"\033[92m[writeTafsirs.py]\033[0m => All tafsirs written successfully.\n")


if os.environ.get("PROD"):
    # Cloudflare Pages only supports max 25MB files.
    os.remove("Data/tafsirs.json")
    print("Removed Data/tafsirs.json as PROD environment variable is set.")
