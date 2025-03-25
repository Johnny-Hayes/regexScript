import re

def regexScript(pattern, file):

    file = open(file, "r")
    with file as logFile:
        logFileLines = logFile.readlines()

        for line in logFileLines:

            for match in re.finditer(pattern, line, re.S):
                matchText = match.group()

                print("Matched Text:")
                return matchText


IPv4 = "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

print(regexScript(IPv4, "./log.txt"))
