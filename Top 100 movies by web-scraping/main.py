from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

titles = soup.find_all(name="h3", class_="title")

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in titles:
        file.write(title.getText() + "\n")