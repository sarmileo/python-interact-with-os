#!/usr/bin/env python3

# This scripts generates two csv files from a log file
# The user csv file contains the user and how many INFO and ERROR logs for the user
# The error csv contains the error messages and the count for each message
#  
# Usage: ./ticky_check.py

import re
import csv
#import operator

# the perUser nested dictionary
# perUser = { 
#   username1: {
#       'INFO' : 0, 
#       'ERROR' : 0
#   },
#   username2: {
#       'INFO' : 0, 
#       'ERROR' : 0
#   }
# }

# the errors dictionary
# errors = { 
#   'The Error String1' : 0,
#   'The Error String2' : 0
# }

errors = {}
perUser = {}

filename = "../exercise1/syslog.log"
INFO = "INFO"
ERROR = "ERROR"
infoPattern = "^[\w\s:.]*(ticky: INFO [\w\s]+)\[#([\d]+)\][\s]+\(([\w.]+)\)"
#infoPattern = "^[\w\s:.]+INFO[\w\s\[#\]]+\(([\w]+)\)"
errorPattern = "^[\w\s:.]+ticky: ERROR ([\w\s']+)[\s]+\(([\w.]+)\)"

with open(filename) as logFile:
    for line in logFile:
        if INFO in line:
            result = re.search(infoPattern, line)
            if result is not None:
                # update perUser[username][INFO]
                username = result[3]
                perUser[username] = perUser.get(username, {})
                perUser[username][INFO] = perUser[username].get(INFO, 0) + 1
        elif ERROR in line:
            result = re.search(errorPattern, line)
            if result is not None:
                # update perUser[username][ERROR]
                username = result[2]
                perUser[username] = perUser.get(username, {})
                perUser[username][ERROR] = perUser[username].get(ERROR, 0) + 1

                # update errors["The Error String"]
                errorString = result[1]
                errors[errorString] = errors.get(errorString, 0) + 1

#perUser = dict(sorted(perUser.items(), key = operator.itemgetter(0)))
perUser = dict(sorted(perUser.items(), key = lambda kv:kv[0]))
#print(perUser)
#print(perUser['mdouglas'])
#print(perUser['mdouglas'][INFO])
#print(dict(sorted(errors.items())))

errors = dict(sorted(errors.items(), key = lambda k:k[1], reverse = True))
#print(errors)

userCsvFile = "user_statistics.csv"
errorCsvFile = "error_message.csv"

with open(userCsvFile, "w") as userCsv:
    fieldnames = ["Username", "INFO", "ERROR"]
    writer = csv.DictWriter(userCsv, fieldnames = fieldnames)

    writer.writeheader();
    for user in perUser:
        # This is important, in case any user does not have INFO or ERROR we set the 
        # value to 0
        info = perUser[user].get(INFO, 0)
        error = perUser[user].get(ERROR, 0)

        writer.writerow({
            "Username" : user, 
            "INFO" : info, 
            "ERROR" : error
            })

with open(errorCsvFile, "w") as errorCsv:
    fieldnames = ["Error", "Count"]
    writer = csv.DictWriter(errorCsv, fieldnames = fieldnames)

    writer.writeheader();
    for error in errors:
        count = errors[error]

        writer.writerow({
            "Error" : error, 
            "Count": count
            })