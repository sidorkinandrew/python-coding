import html
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="div", class_="article-title-description__text")

print(all_movies)
print(len(all_movies))
print(all_movies[-1])

movies = []

for amovie in all_movies:
    place, title = amovie.findNext(name="h3", class_="title").getText().replace("12:","12)").split(') ')
    year = amovie.findNext(name="strong").getText()
    if place == "2":
        year = 1980
    # print(place, html.unescape(title), year)
    movies.append(f"{place}) {html.unescape(title)} ({year})")

#movie_titles = [movie.getText() for movie in all_movies]
movies = movies[::-1]

#print(movies)
with open("movies.txt", mode="w", encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")
