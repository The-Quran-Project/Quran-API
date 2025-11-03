import os
import re

from config import reciters, recitersWithID, originalUrl
from helper import makeDir, makeJson, readJsonFile, goToRightDir, prettifyJson


def pprint(x: dict):
    print(prettifyJson(x))


def remove_html_tags(text: str) -> str:
    # Remove tags and their contents (like <tag ...>...</tag>)
    text = re.sub(r"<[^>]+?>.*?</[^>]+?>", "", text)
    # Remove self-closing or single tags (like <br>, <img />, etc.)
    text = re.sub(r"<[^>]+?>", "", text)
    return text.strip()


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
quranTr = readJsonFile("quran_tr.json")
quranUz = readJsonFile("quran_uz.json")

# Translations that are not major (i.e., not included in the main surah data)
nonMajor = [
    "turkish",
    "uzbek",
]  # save the whole json translation, but not the ayah by ayah or whole chapter data

allSurahData = []
translations = {
    "english": [],
    "arabic1": [],
    "arabic2": [],
    "bengali": [],
    "urdu": [],
    "turkish": [],
    "uzbek": [],
}

# NOTE FROM DEVELOPER
# There are *tons* of nesting here, i know! :)
# I didn't try to simplify it further cuz this code isn't gonna be modified that often.
# So, yeah. :3


for surahNo in range(1, 115):
    eng = quranEn[surahNo - 1]
    ara = quranAr[surahNo - 1]
    ben = quranBn[surahNo - 1]
    urd = quranUr[surahNo - 1]
    tur = quranTr[surahNo - 1]
    uzb = quranUz[surahNo - 1]

    totalAyah = len(eng)
    surahInfo = surahData[surahNo - 1]
    surahName = surahInfo["surahName"]
    surahNameAr = surahInfo["surahNameAr"]
    surahNameArLong = surahInfo["surahNameArLong"]
    surahNameTranslation = surahInfo["surahNameMeaning"]
    revelationPlace = surahInfo["revelationPlace"]
    # verseAudio = "https://quranaudio.pages.dev/{num}/{surahNo}_{ayahNo}.mp3" # discontinued due to total file limit
    # verseAudio = "https://github.com/The-Quran-Project/Quran-Audio/raw/refs/heads/data/Data/{num}/{surahNo}_{ayahNo}.mp3" # github raw

    verseAudio = "https://the-quran-project.github.io/Quran-Audio/Data/{num}/{surahNo}_{ayahNo}.mp3"
    verseOriginalAudio = "https://everyayah.com/data/{name}/{surah}{ayah}.mp3"
    chapterAudio = "https://github.com/The-Quran-Project/Quran-Audio-Chapters/raw/refs/heads/main/Data/{}/{}.mp3"

    # Make the folder
    makeDir(f"api/{surahNo}")

    for ayahNo in range(1, totalAyah + 1):
        arabic1, arabic2 = ara[ayahNo - 1]
        english = eng[ayahNo - 1]
        bengali = ben[ayahNo - 1]
        urdu = urd[ayahNo - 1]
        ayahTranslations = {
            "english": remove_html_tags(english),
            "arabic1": remove_html_tags(arabic1),
            "arabic2": remove_html_tags(arabic2),
            "bengali": remove_html_tags(bengali),
            "urdu": remove_html_tags(urdu),
        }
        ayahAudioData = {
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
        }

        defaultAyahData = {
            "surahName": surahName.strip(),
            "surahNameArabic": surahNameAr.strip(),
            "surahNameArabicLong": surahNameArLong.strip(),
            "surahNameTranslation": surahNameTranslation.strip(),
            "revelationPlace": revelationPlace.strip(),
            "totalAyah": totalAyah,
            "surahNo": surahNo,
            "ayahNo": ayahNo,
            "audio": ayahAudioData,
        }

        ayahData = defaultAyahData | ayahTranslations

        makeJson(f"api/{surahNo}/{ayahNo}.json", ayahData)
        makeDir(f"api/audio/{surahNo}/")
        makeJson(f"api/audio/{surahNo}/{ayahNo}.json", ayahAudioData)

        # I know there are better ways, I'm just lazy.
        print(
            f"\033[92m[main.py]\033[0m => Done \033[93m{surahNo}\033[0m:\033[96m{ayahNo}\033[0m\r",
            end="",
        )

    chapterTranslations = {
        "english": [remove_html_tags(i) for i in eng],
        "arabic1": [remove_html_tags(i[0]) for i in ara],
        "arabic2": [remove_html_tags(i[1]) for i in ara],
        "bengali": [remove_html_tags(i) for i in ben],
        "urdu": [remove_html_tags(i) for i in urd],
        "turkish": [remove_html_tags(i) for i in tur],
        "uzbek": [remove_html_tags(i) for i in uzb],
    }

    chapterAudioData = {
        i: {
            "reciter": j,
            "url": chapterAudio.format(i, surahNo),
            "originalUrl": originalUrl[i].format(f"{surahNo:03}"),
        }
        for (i, j) in reciters.items()
    }

    defaultChapterData = {
        "surahName": surahName,
        "surahNameArabic": surahNameAr,
        "surahNameArabicLong": surahNameArLong,
        "surahNameTranslation": surahNameTranslation,
        "revelationPlace": revelationPlace,
        "totalAyah": totalAyah,
        "surahNo": surahNo,
        "audio": chapterAudioData,
    }

    finalData = defaultChapterData | chapterTranslations

    # For specific translations
    for lang, value in chapterTranslations.items():
        _data = defaultChapterData | {
            "verseAudio": {
                i: {
                    "reciter": j,
                    "audios": [
                        {
                            "url": verseAudio.format(
                                num=i, surahNo=surahNo, ayahNo=ayahNo
                            ),
                            "originalUrl": verseOriginalAudio.format(
                                name=recitersWithID[i],
                                surah=f"{surahNo:03}",
                                ayah=f"{ayahNo:03}",
                            ),
                        }
                        for ayahNo in range(1, totalAyah + 1)
                    ],
                }
                for (i, j) in reciters.items()
            },
            "translation": value,
        }

        # pprint(_data["verseAudio"])
        translations[lang].append(_data)

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
    for lang in nonMajor:
        del finalData[lang]  # Remove the non-major translations from the final data

    makeJson(f"api/{surahNo}.json", finalData)
    makeJson(f"api/audio/{surahNo}.json", chapterAudioData)
    print()


makeJson("api/surah.json", allSurahData)
for lang, value in translations.items():
    makeJson(f"api/{lang}.json", value, indent=None)


# Run other scripts
os.system("python scripts/generateSitemap.py")
os.system("python scripts/dumpTemplates.py")
os.system("python scripts/writeTafsirs.py")
