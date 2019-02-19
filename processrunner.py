import subprocess
import os

path = "/home/pi/Documents/Programming/RaspberryPi/RaspberryPiServer/"

pservice = {}
processfile = {"transferServer":"websocketserver.py"}

def initialize():
    pservice["transferServer"] = subprocess.Popen(["python3", "websocketserver.py"], cwd=path)

def kill(service):
    pservice[service].kill()
    del pservice[service]

def killall():
    for service in pservice:
        pservice[service].kill()
    pservice.clear()

def start(service):
    pservice[service] = subprocess.Popen(["python3", processfile[service]], cwd=path)

def list_active_services():
    for key in pservice:
        print("Service = " + key + " PID = " + str(pservice[key].pid))

def update():
    subprocess.Popen(["git", "pull"], cwd=path)
    killall()
    initialize()

initialize()
