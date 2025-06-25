import os, json
from dotenv import load_dotenv

load_dotenv()


folderPath = "api/tafsir"

os.makedirs(folderPath, exist_ok=True)

with open("Data/tafsirs.json", "rb") as file:
    tafsirs = json.load(file)


for surahNo, surah in enumerate(tafsirs, 1):
    for tafsir in surah:
        ayahNo = tafsir["ayahNo"]
        fileName = f"{folderPath}/{surahNo}_{ayahNo}.json"
        with open(fileName, "w", encoding="utf-8") as file:
            json.dump(tafsir, file, ensure_ascii=False, indent=4)
        print(f"Written {fileName}")

print("All tafsirs written successfully.")


if os.environ.get("PROD"):
    # Cloudflare Pages only supports max 25MB files.
    os.remove("Data/tafsirs.json")
    print("Removed Data/tafsirs.json as PROD environment variable is set.")
