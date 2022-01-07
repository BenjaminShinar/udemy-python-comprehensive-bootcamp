from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#quotes_page = "https://bluelimelearning.github.io/my-fav-quotes"


def scrape(page):
    with uReq(page) as uClient:
        page_html = uClient.read()
    page_soup = soup(page_html, "html.parser")
    return page_soup


def getQuotes(soupPage):
    quotes = soupPage.findAll("div", {"class": "quotes"})
    return quotes


def webScrap() -> None:
    print("started!")
    page = scrape(
        "http://page:80/")  #service name in network. docker-compose only hack
    quotes = getQuotes(page)
    print(len(quotes))

    for q in quotes:
        quote = q.findAll("p", {"class": "aquote"})[0].text.strip()
        author = q.findAll("p", {"class": "author"})[0].text.strip()
        print(quote, author)


if __name__ == "__main__":
    webScrap()