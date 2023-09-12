import bs4

with open("index.html", 'r') as html_file:
    content = html_file.read()
    print(content)

    soup = bs4.BeautifulSoup(content, 'lxml')
    print(soup.prettify())