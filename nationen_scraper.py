from bs4 import BeautifulSoup
import urllib3
import re

def fetch_html(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response.data.decode('cp1252')

def parse_eb_html(raw_html):

    soup = BeautifulSoup(raw_html, "lxml")
    titles = []

    # Apparently all tags called 'oo-line' contain
    tags = soup.findAll("div", class_="oo-line")

    for tag in tags:
        # Skip invalid lines
        if tag.string == None:
            continue
        title = tag.string
        title = re.sub("[\t\n]", "", title)
        title = title.lstrip(' ')
        titles.append(title)
    
    # Remove duplicates 
    titles = list(set(titles))

    return titles


def append_titles(titles, filepath):
    
    existing_titles = set()
    with open(filepath, 'r') as file:
        for title in file.readlines():
            existing_titles.add(title)
    
    new_titles = set(titles).difference(existing_titles)
    with open(filepath, 'a') as file:
        file.writelines(new_title + '\n' for new_title in new_titles)


def scrape_to_file(filepath):
    raw_nationen = fetch_html('https://ekstrabladet.dk/nationen/')
    titles_nationen = parse_eb_html(raw_nationen)
    raw_1849 = fetch_html('https://ekstrabladet.dk/nationen/1849/')
    titles_1849 = parse_eb_html(raw_1849)

    titles = titles_nationen + titles_1849
    append_titles(titles, filepath)