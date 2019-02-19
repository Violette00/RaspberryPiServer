import subprocess
import os

print(os.getcwd())
print(subprocess.check_output(["git", "pull"], cwd="/home/pi/Documents/Programming/RaspberryPi/RaspberryPiServer/"))
