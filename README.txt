CLI commands:

No command: will print a greeting message.
-h, --help: will bring up the help menu showing each command.
-f, --file: (argument: file name in a string) opens the file in the argument and checks for an api token pattern. Prints the results.

How the --file command works:

1. opens the patterns.json file and extracts the regex patterns from the patterns list.
2. opens the user file and uses .readlines() to make a list of each line.
3. uses the .search() method in the re package to use each regex pattern to look for a match in each line from the user file.
4. if a match is found, it is saved and the match counter adds 1.
5. at the end results are printed and if there are no matchs found a '0 matches found.' message is printed instead.