import os, json


def makeDir(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def makeJson(path, content, indent=4):
    with open(path, "w", encoding="utf8") as file:
        json.dump(content, file, ensure_ascii=0, indent=indent)


def prettifyJson(data: dict):
    return json.dumps(data, indent=3, ensure_ascii=False)


def readJsonFile(path: str, folder: str = "Data", prettify: bool = False):
    with open(f"{folder}/{path}", "r", encoding="utf8") as file:
        file = json.load(file)
        if prettify:
            return prettifyJson(file)

        return file


def goToRightDir():
    if os.path.exists("templates"):
        os.chdir("..")

    if os.path.exists("public"):
        os.chdir("public")


