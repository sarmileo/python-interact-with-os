#!/usr/bin/env python3

import re
import os

file = "syslog.log"
infoFile = "infoFile.txt"
errorFile = "errorFile.txt"
infoFileCsv = "infoFileCsv.txt"
errorFileCsv = "errorFileCsv.txt"
infoStr = "INFO"
errorStr = "ERROR"

## If file exists, delete it, just for practice here##
if os.path.isfile(infoFile):
    os.remove(infoFile)
if os.path.isfile(errorFile):
    os.remove(errorFile)

infoList = []
errorList = []
infoListCsv = []
errorListCsv = []

with open(file) as f:
    lines = f.readlines()

    for line in lines:
        if infoStr in line:
            allInfo = re.search(r"^[\w\s:.]*(ticky: INFO [\w\s]+)\[#([\d]+)\][\s]+\(([\w.]+)\)", line)
            if allInfo is not None:
                infoList.append(allInfo[0])
                infoListCsv.append(f"{allInfo[3]}, {allInfo[2]}, {allInfo[1]}")
        elif errorStr in line:
            allError = re.search(r"^[\w\s:.]*(ticky: ERROR [\w\s']+)[\s]+\(([\w.]+)\)", line)
            if allError is not None:
                errorList.append(allError[0])
                errorListCsv.append(f"{allError[2]}, {allError[1]}")
                
with open(infoFile, "w+") as infofile:
    for info in infoList:
        infofile.write(f"{info}\n")

with open(errorFile, "w+") as errorfile:
    for error in errorList:
        errorfile.write(f"{error}\n")

with open(infoFileCsv, "w+") as infocsv:
    infocsv.write(f"User, Ticket, Information\n")
    for info in infoListCsv:
        infocsv.write(f"{info}\n")   

with open(errorFileCsv, "w+") as errorcsv:
    errorcsv.write(f"Error, Information\n")
    for error in errorListCsv:
        errorcsv.write(f"{error}\n")