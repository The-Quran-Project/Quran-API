import os
import json


def makeDir(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def makeJson(path, content):
    with open(path, "w", encoding="utf8") as file:
        json.dump(content, file, ensure_ascii=0, indent=4)


with open("Data/surah.json", "r", encoding="utf8") as f:
    surahNames = json.load(f)

with open("Data/surahData.json", "r", encoding="utf8") as f:
    surahData = json.load(f)


with open("Data/quran_ar.json", "r", encoding="utf8") as f:
    quranAr = json.load(f)

with open("Data/quran_en.json", "r", encoding="utf8") as f:
    quranEn = json.load(f)

with open("Data/quran_bn.json", "r", encoding="utf8") as f:
    quranBn = json.load(f)



makeDir("api")

allSurahData = []
for surahNo, j in quranEn.items():

    audioUrl = "https://quranaudio.pages.dev/{num}/{surahNo}_{ayahNo}.mp3"
    surahNo = int(surahNo)
    totalAyah = len(j)
    # surahName = surahNames[surahNo - 1]

    surahInfo = surahData[surahNo - 1]

    surahName = surahInfo["surahName"]
    surahNameAr = surahInfo["surahNameAr"]
    surahNameArLong = surahInfo["surahNameArLong"]
    surahNameTranslation = surahInfo["surahNameMeaning"]
    revelationPlace = surahInfo["revelationPlace"]

    ara = quranAr[str(surahNo)]
    ben = quranBn[surahNo - 1]
    
    # Make the folder
    makeDir(f"api/{surahNo}")

    for ayahNo, english in enumerate(j, start=1):
        arabic1, arabic2 = ara[ayahNo - 1]
        bangla = ben[ayahNo - 1]
        
        ayahData = {
            "surahName": surahName,
            "surahNameArabic": surahNameAr,
            "surahNameArabicLong": surahNameArLong,
            "surahNameTranslation": surahNameTranslation,
            "revelationPlace": revelationPlace,
            "totalAyah": totalAyah,
            "surahNo": surahNo,
            "ayahNo": ayahNo,
            "english": english,
            "arabic1": arabic1,
            "arabic2": arabic2,
            "bangla": bangla,
            "audio": {
                "1": {
                    "reciter": "Mishary Rashid Al-Afasy",
                    "url": audioUrl.format(num=1, surahNo=surahNo, ayahNo=ayahNo),
                },
                "2": {
                    "reciter": "Abu Bakr Al-Shatri",
                    "url": audioUrl.format(num=2, surahNo=surahNo, ayahNo=ayahNo),
                },
            },
        }
        makeJson(f"api/{surahNo}/{ayahNo}.json", ayahData)

        print(f"Done {ayahNo} of {surahNo}\r", end="")

    finalData = {
        "surahName": surahName,
        "surahNameArabic": surahNameAr,
        "surahNameArabicLong": surahNameArLong,
        "surahNameTranslation": surahNameTranslation,
        "revelationPlace": revelationPlace,
        "totalAyah": totalAyah,
        "surahNo": surahNo,
        "english": j,
        "arabic1": [i[0] for i in ara],
        "arabic2": [i[1] for i in ara],
    }
    makeJson(f"api/{surahNo}.json", finalData)
    allSurahData.append(
        {
            "surahName": surahName,
            "surahNameArabic": surahNameAr,
            "surahNameArabicLong": surahNameArLong,
            "surahNameTranslation": surahNameTranslation,
            "revelationPlace": revelationPlace,
            "totalAyah": totalAyah,
        }
    )
    print()

makeJson("api/surah.json", allSurahData)

# TODO: Add other reciters
reciters = {"1": "Mishary Rashid Al-Afasy", "2": "Abu Bakr Al-Shatri"}

makeJson("api/reciters.json", reciters)
print("Done")
