import os
import subprocess

print(os.getcwd())
os.chdir('sentiment')

subprocess.run(["python", "app.py", "1"])