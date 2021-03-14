import webbrowser

# 1.1 Opening up a web browser
#webbrowser.open('http://myebeat.com')

# http://www.gutenberg.org/cache/epub/1112/pg1112.txt

# automate-the-boring-stuff-with-python-2015-.pdf  Page237

import requests
# res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# print(res.text[:250])

import bs4

# res = requests.get('http://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, features="html.parser")
# print(type(noStarchSoup))

# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile, features="html.parser")
# print(type(exampleSoup))

# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features="html.parser")
# elems = exampleSoup.select('#author')
# print(len(elems))
# print(type(elems[0]))
# print(elems[0].getText())
# str(elems[0])
# elems[0].attrs


import sys

input = input("What do you want to search: ")
url = "http://google.com/search?q="+input
res = requests.get(url)
# webbrowser.open(url)
soup = bs4.BeautifulSoup(res.text, features="html.parser")
linkElems = soup.select("div a")
# for link in linkElems:
#     print(link)
count = 0
for link in linkElems:
    if "http" in str(link) and "img" not in str(link) and "google" not in str(link):
        cut_pos = str(link).find("=")

        open_link = link["href"][cut_pos:]
        extra_pos = open_link.find("&")
        if extra_pos != -1:
            open_link = open_link[0:extra_pos]
        # print(open_link)
        if count < 5:
            webbrowser.open(open_link)
            count += 1

