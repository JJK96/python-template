import shutil
import os

shutil.copyfile('settings.example.toml', 'settings.toml')
os.system("git init")
