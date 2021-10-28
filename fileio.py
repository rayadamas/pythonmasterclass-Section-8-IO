# jabber = open("sample.txt", 'r') # open() is the built in function to open a file.
#
# for line in jabber:
#     if "jabberwock" in line.lower(): # converting to lowercase to perform a casecheck against our sample lowercase txt
#         print(line, end='') # `end=''` stops us from going to the next line
#
# jabber.close()
#
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

# ^ Reads the entire file and return the list, which can then be processed automatically as ever we would like.

for line in lines[::-1]:
    print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')

