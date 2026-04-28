import os
from helper import goToRightDir


goToRightDir()


os.system("python scripts/writeSurahs.py")
os.system("python scripts/makeJuz.py")
os.system("python scripts/generateSitemap.py")
os.system("python scripts/dumpTemplates.py")
os.system("python scripts/writeTafsirs.py")
