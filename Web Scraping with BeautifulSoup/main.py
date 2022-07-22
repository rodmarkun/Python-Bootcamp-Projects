from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
article_link = article_tag.get("href")

score_tag = soup.find(name="span", class_="score")
article_upvote = score_tag.getText()
print(article_upvote)
