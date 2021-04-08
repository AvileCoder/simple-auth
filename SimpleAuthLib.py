#Coded by Avile
import os, requests, subprocess

HWID = os.popen('wmic baseboard get serialnumber').read().replace('SerialNumber', '').replace('\n', '').replace(' ', '') #Get Motherboard serial number aka our HWID
def Auth(link, lkey):
    try:
        cfb = requests.get(link)
        dumpped = cfb.text
    except:
        print("Can't connect to this link")
    try:
        if ('"'+HWID+'":"'+lkey+'"') not in dumpped:
            return 0
        else:
            return 1
    except:
        print("Error while computing your licence")
