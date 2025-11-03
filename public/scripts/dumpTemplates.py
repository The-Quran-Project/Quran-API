from helper import goToRightDir, readJsonFile, prettifyJson
from config import reciters

goToRightDir()


def readFile(fileName):
    with open(f"templates/{fileName}", "r") as file:
        return file.read()


def writeFile(fileName, content):
    with open(f"../pages/getting-started/{fileName}", "w", encoding="utf-8") as file:
        file.write(content)


def createReciterTable(reciters_dict):
    table = "| Reciter ID | Name                    |\n"
    table += "| ---------- | :---------------------- |\n"

    for reciter_id, name in reciters_dict.items():
        table += f"| {reciter_id:<10} | {name:<23} |\n"

    return table


replacements = {
    "audio-recitation.mdx": {
        "RECITER_ID_AND_NAME_TABLE": createReciterTable(reciters),
        "AUDIO_2_RESPONSE": readJsonFile("audio/2.json", "api", prettify=True),
        "AUDIO_2_VERSE_RESPONSE": readJsonFile("audio/2/1.json", "api", prettify=True),
    },
    "get-a-verse.mdx": {
        "VERSE_2_RESPONSE": readJsonFile("1/2.json", "api", prettify=True),
    },
    "get-a-chapter.mdx": {
        "CHAPTER_112_RESPONSE": readJsonFile("112.json", "api", prettify=True),
    },
    "available-reciters.mdx": {
        "RECITER_LIST": prettifyJson(reciters),
    },
}

for file_name, replacement_dict in replacements.items():
    file = readFile(file_name)
    for placeholder, replacement in replacement_dict.items():
        file = file.replace(placeholder, replacement)

    writeFile(file_name, file)
    print(
        f"\033[95mCreated {file_name}\033[0m with replacements: \033[94m{', '.join(list(replacement_dict.keys()))}\033[0m"
    )
