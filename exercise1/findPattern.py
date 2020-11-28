#!/usr/bin/env python3

import re

lineInfo = "May 27 11:45:40 ubuntu.local ticky: INFO Created ticket [#1234] (Leo)"
lineError = "May 27 11:45:40 ubuntu.local ticky: ERROR Error creating ticket [#1234] (Jonny)"

info = re.search(r"ticky: INFO ([\w ]*)", lineInfo)
error = re.search(r"ticky: ERROR ([\w ]*)", lineError)
leo = re.search(r"ticky: ERROR: ([\w ]*)", lineError)
fullMatch = re.search(r"[\w\s.:#\[\]]*\(([\w]+)\)", lineError)
allInfo = re.search(r"[\w\s:.]*(ticky: INFO [\w\s]+)\[#([\d]+)\][\s]+\(([\w]+)\)", lineInfo)
allError = re.search(r"[\w\s:.]*(ticky: ERROR [\w\s]+)\[#([\d]+)\][\s]+\(([\w]+)\)", lineError)

print(info[0])
print(error[0])
print(fullMatch[0])
print(fullMatch[1])
print(f"info  -> {allInfo[1]}, ticket #: {allInfo[2]}, user: {allInfo[3]}")
print(f"error -> {allError[1]}, ticket #: {allError[2]}, user: {allError[3]}")