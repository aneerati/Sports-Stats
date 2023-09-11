import bs4

with open("index.html", 'r') as html_file:
    content = html_file.read()
    print(content)