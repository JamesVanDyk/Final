import re
import argparse
import json

parser = argparse.ArgumentParser()

#arguments
parser.add_argument('defaultMessage',
                    nargs='*',
                    default='Hello! Welcome to my program! Use \"-h\" for help.',
                    help='The default message when no arguements are passed.')
parser.add_argument('-f', '--file',
                    type=str,
                    help='Input the file to find secret patterns.')

#collects the arguments
args = parser.parse_args()



if args.file != None:
    #loading the json file data
    patterns = open('patterns.json', 'r')
    patternData = json.load(patterns)
    patterns.close()

    #extracts the regex patterns and puts them in a list
    patternList = patternData['patterns']
    regexPatterns = []
    for object in patternList:
        regexPatterns.append(object['regex'])

    #getting user file data
    try:
        badFile = False
        userFile = open(args.file, 'r')
        userFileData = userFile.readlines()
    except:
        badFile = True
        print("There seems to be an error loading this file.\nMake sure the file name is spelled correctly and is in the same directory as main.py and try again.")


    
    #compares each line to each of the regex tokens
    matchCount = 0
    if badFile == False:
        for line in userFileData:
            for p in regexPatterns:
                matches = re.search(p, line)
                if matches:
                    matchCount += 1
                    print('found a match')
                    print(matches)

        #prints results
        print(f"{matchCount} matches found.")
        if matchCount > 0:
            print(matches)

else:

    #prints the default hello message
    print(args.defaultMessage)