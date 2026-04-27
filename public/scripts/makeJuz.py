# no AI was involved in writing this entire file. coded in sublime text 4

import os, json
from dotenv import load_dotenv
from helper import pprint, makeJson, getSurahName, readJsonFile

load_dotenv()


folderPath = "api/juz"
os.makedirs(folderPath, exist_ok=True)
juzFileData = readJsonFile("juz.json")
multiLanguages = {
    "arabic" : readJsonFile("quran_ar.json"),
    "english" : readJsonFile("quran_en.json"),
    "bengali" : readJsonFile("quran_bn.json"),
    "urdu" : readJsonFile("quran_ur.json"),
    "turkish" : readJsonFile("quran_tr.json"),
    "uzbek" : readJsonFile("quran_uz.json"),
}



excluded = ["audio"]
languages = ["english", "arabic1", "arabic2", "bengali", "urdu"]


def getChapterHeaders(chapterNum, verseStart, verseEnd, juz):
    data = readJsonFile(f"{chapterNum}.json", "api")

    modified = {}

    for i, j in data.items():
        if i not in [*excluded, *languages]:
            modified[i] = j

    modified["juzNum"] = juz
    modified["verseStart"] = verseStart
    modified["verseEnd"] = verseEnd
    modified["range"] = f"{chapterNum}:{verseStart}-{verseEnd}"

    return modified


def getSpecificRangeOfChapter(chapterNum, verseStart, verseEnd, juz):
    data = readJsonFile(f"{chapterNum}.json", "api")

    modified = getChapterHeaders(chapterNum, verseStart, verseEnd, juz)

    for l in languages:
        modified[l] = data[l][verseStart - 1 : verseEnd]

    return modified


def getSpecificByLanguage(language, chapterNum, verseStart, verseEnd, juz=None):
    modified = getChapterHeaders(chapterNum, verseStart, verseEnd, juz)

    withTashkeel = False
    if language.startswith("arabic"):
        withTashkeel:bool = language[-1] == "1"
        language = "arabic"

    modified["translation"] = multiLanguages[language][chapterNum - 1][verseStart - 1 : verseEnd]

    if language == "arabic":
        modified["translation"] = [i[int(not withTashkeel)] for i in modified["translation"]]

    return modified


# pprint(getSpecificByLanguage("english", 2, 1, 5))
# print(getChapterHeaders(2, 3, 11, True))
# print(getSpecificRangeOfChapter(2, 3, 11, True))


juzHeadersData = {}

# i know the code is messy, but if you look for couple of seconds, it's not as confusing as it might appear
languageWiseJuz = {
    "arabic1": [[] for _ in range(30)],
    "arabic2": [[] for _ in range(30)],
    **{i:[[] for _ in range(30)] for i in multiLanguages.keys() if i!="arabic"}
    # "english" : [[]..30] // 30 empty arrays. [[]]*30 is not gonna work cuz then the arrays are not indipendent
    # "bengali" : [[]..30] // so i did list comprehension. didn't wanna do the .copy or deepcopy thing.
    # ...
}

for juzNum, surahs in juzFileData.items():
    juzData = []
    juzHeaders = []
    juzNum = int(juzNum)
    juzPath = f"api/juz/{juzNum}.json"

    for surah in surahs:
        verseStart = surah["startVerse"]
        verseEnd = surah["endVerse"]
        surahNum = surah["surahNumber"]
        data = getSpecificRangeOfChapter(surahNum, verseStart, verseEnd, juzNum)
        headers = getChapterHeaders(surahNum, verseStart, verseEnd, juzNum)

        for lang in languageWiseJuz:
            langData = getSpecificByLanguage(lang, surahNum, verseStart, verseEnd, juzNum)
            languageWiseJuz[lang][juzNum - 1].append(langData)

        
        juzData.append(data)
        juzHeaders.append(headers)

    juzHeadersData[juzNum] = juzHeaders
    makeJson(juzPath, juzData)

makeJson("api/juz.json", juzHeadersData)
for lang, data in languageWiseJuz.items():
    makeJson(f"api/juz/{lang}.json", data)


print(f"\033[92m[makeJuz.py]\033[0m => All juz written successfully.\n")