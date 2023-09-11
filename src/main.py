import bs4

with open("index.html", 'r') as html_file:
    content = html_file.read()

    soup = bs4.BeautifulSoup(content, 'lxml')
    course_html_tags = soup.find_all('h5')
    for course in course_html_tags:
        print(course.text)