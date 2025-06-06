import os, json


folderPath = "api/tafsir"

os.makedirs(folderPath, exist_ok=True)

with open("Data/tafsirs.json", "rb") as file:
    tafsirs = json.load(file)


for surahNo, surah in enumerate(tafsirs, 1):
    for ayahNo, tafsir in enumerate(surah, 1):
        fileName = f"{folderPath}/{surahNo}_{ayahNo}.json"
        with open(fileName, "w", encoding="utf-8") as file:
            json.dump(tafsir, file, ensure_ascii=False, indent=4)
        print(f"Written {fileName}")

print("All tafsirs written successfully.")
