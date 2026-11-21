import requests, pandas as pd
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

books = [{"title": b.h3.a["title"],
          "price": b.find("p", class_="price_color").text,
          "rating": b.p["class"][1]} for b in soup.select("article.product_pod")]

df = pd.DataFrame(books)
print(df)
df.to_csv("books.csv", index=False)