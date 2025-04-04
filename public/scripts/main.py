import os

from config import reciters, recitersWithID, originalUrl
from helper import makeDir, makeJson, readJsonFile, goToRightDir


goToRightDir()


makeDir("api")
makeDir("api/audio")
makeJson("api/reciters.json", reciters)

surahNames = readJsonFile("surah.json")
surahData = readJsonFile("surahData.json")
quranAr = readJsonFile("quran_ar.json")
quranEn = readJsonFile("quran_en.json")
quranBn = readJsonFile("quran_bn.json")
quranUr = readJsonFile("quran_ur.json")


allSurahData = []
translations = {"english": [], "arabic1": [], "arabic2": [], "bengali": [], "urdu": []}


for surahNo in range(1, 115):
    eng = quranEn[surahNo - 1]
    ara = quranAr[surahNo - 1]
    ben = quranBn[surahNo - 1]
    urd = quranUr[surahNo - 1]

    totalAyah = len(eng)
    surahInfo = surahData[surahNo - 1]
    surahName = surahInfo["surahName"]
    surahNameAr = surahInfo["surahNameAr"]
    surahNameArLong = surahInfo["surahNameArLong"]
    surahNameTranslation = surahInfo["surahNameMeaning"]
    revelationPlace = surahInfo["revelationPlace"]
    # verseAudio = "https://quranaudio.pages.dev/{num}/{surahNo}_{ayahNo}.mp3" # discontinued due to total file limit
    # verseAudio = "https://github.com/The-Quran-Project/Quran-Audio/raw/refs/heads/data/Data/{num}/{surahNo}_{ayahNo}.mp3" # github raw

    verseOriginalAudio = "https://everyayah.com/data/{name}/{surah}{ayah}.mp3"
    verseAudio = "https://the-quran-project.github.io/Quran-Audio/Data/{num}/{surahNo}_{ayahNo}.mp3"
    chapterAudio = "https://github.com/The-Quran-Project/Quran-Audio-Chapters/raw/refs/heads/main/Data/{}/{}.mp3"

    # Make the folder
    makeDir(f"api/{surahNo}")

    for ayahNo in range(1, totalAyah + 1):
        arabic1, arabic2 = ara[ayahNo - 1]
        english = eng[ayahNo - 1]
        bengali = ben[ayahNo - 1]
        urdu = urd[ayahNo - 1]
        ayahTranslations = {
            "english": english,
            "arabic1": arabic1,
            "arabic2": arabic2,
            "bengali": bengali,
            "urdu": urdu,
        }

        defaultAyahData = {
            "surahName": surahName,
            "surahNameArabic": surahNameAr,
            "surahNameArabicLong": surahNameArLong,
            "surahNameTranslation": surahNameTranslation,
            "revelationPlace": revelationPlace,
            "totalAyah": totalAyah,
            "surahNo": surahNo,
            "ayahNo": ayahNo,
            "audio": {
                i: {
                    "reciter": j,
                    "url": verseAudio.format(num=i, surahNo=surahNo, ayahNo=ayahNo),
                    "originalUrl": verseOriginalAudio.format(
                        name=recitersWithID[i],
                        surah=f"{surahNo:03}",
                        ayah=f"{ayahNo:03}",
                    ),
                }
                for (i, j) in reciters.items()
            },
        }

        ayahData = defaultAyahData | ayahTranslations

        makeJson(f"api/{surahNo}/{ayahNo}.json", ayahData)

        print(f"Done {ayahNo} of {surahNo}\r", end="")

    chapterTranslations = {
        "english": [i for i in eng],
        "arabic1": [i[0] for i in ara],
        "arabic2": [i[1] for i in ara],
        "bengali": [i for i in ben],
        "urdu": [i for i in urd],
    }
    defaultChapterData = {
        "surahName": surahName,
        "surahNameArabic": surahNameAr,
        "surahNameArabicLong": surahNameArLong,
        "surahNameTranslation": surahNameTranslation,
        "revelationPlace": revelationPlace,
        "totalAyah": totalAyah,
        "surahNo": surahNo,
        "audio": {
            i: {
                "reciter": j,
                "url": chapterAudio.format(i, surahNo),
                "originalUrl": originalUrl[i].format(f"{surahNo:03}"),
            }
            for (i, j) in reciters.items()
        },
    }

    finalData = defaultChapterData | chapterTranslations

    # For specific translations
    for lang, value in chapterTranslations.items():
        _data = defaultChapterData | {lang: value}
        translations[lang].append(_data)

    chapterAudioData = {
        i: {
            "reciter": j,
            "url": chapterAudio.format(i, surahNo),
            "originalUrl": originalUrl[i].format(f"{surahNo:03}"),
        }
        for (i, j) in reciters.items()
    }

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
    makeJson(f"api/{surahNo}.json", finalData)
    makeJson(f"api/audio/{surahNo}.json", chapterAudioData)
    print()


makeJson("api/surah.json", allSurahData)
for lang, value in translations.items():
    makeJson(f"api/{lang}.json", value)


# Generate the sitemap
os.system("python scripts/generateSitemap.py")
os.system("python scripts/dumpTemplates.py")
