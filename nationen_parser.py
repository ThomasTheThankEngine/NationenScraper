from bs4 import BeautifulSoup
import re

# Super inefficient way to add new title to file
# todo: find a better way to do this
def add_header(header, file):

    lines = file.readlines()
    for line in lines:
        # Skip if the title already exists
        if line == header:
            return 1
    
    file.write(header + "\n")
    return 0

# Read html file (right now just as file)
raw_file = open("nationen.html", "r")
header_file = open("nationen_headers.txt", "a+")
soup = BeautifulSoup(raw_file, "lxml")

# Find all oo-line class tags
tags = soup.findAll("div", class_="oo-line")

for tag in tags:
    # Skip invalid lines
    if tag.string == None:
        continue
    s = tag.string
    s = re.sub("[\t\n]", "", s).lstrip(' ')
    add_header(s, header_file)
