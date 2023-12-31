from bs4 import BeautifulSoup

"""""
with open('src/test.html', 'r') as home_file:
    content = home_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_html_tags = soup.find_all("h5")
    for course in course_html_tags:
        print(course.text)
"""
with open('/Users/akshatneerati/Documents/Sports-Stats/tests/test.html', "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")
    course_cards = soup.find_all("div", class_="card")

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f"{course_name} costs {course_price}")
