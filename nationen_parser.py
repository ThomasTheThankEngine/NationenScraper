from bs4 import BeautifulSoup
import re

header_file = "nationen_headers.txt"

# Super inefficient way to add new title to file
# todo: find a better way to do this
def add_header(header, filepath):

    file = open(filepath, "r")
    lines = file.readlines()
    for line in lines:
        line = re.sub("[\n]", "", line)
        # Skip if the title already exists
        if line == header:
            return 1
    
    file = open(filepath, "a")
    file.write(header + "\n")
    return 0

def parse_eb_file(filepath):

    # Read html file (right now just as file)
    raw_file = open(filepath, "r")
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

parse_eb_file("1849.html")
parse_eb_file("nationen.html")