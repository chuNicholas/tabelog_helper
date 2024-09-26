import urllib.request
import os
import time
import threading
from bs4 import BeautifulSoup
import translators as ts

def fetch_results(tabelog_url):
    restos = []
    request = urllib.request.Request(tabelog_url)

    # may crash if website returns error
    try:
        # add timeout to avoid getting stuck
        page = urllib.request.urlopen(request, timeout=2)
    
        # lxml - html/ xml processor
        soup = BeautifulSoup(page, "lxml")

        # find the <p> tags
        for info in soup.find_all("h3", {"class" : "list-rst__rst-name"}):
            name = info.find("a").get_text()
            url = info.find("a", href=True)['href']
            # print(name)
            # print(url)
            # print()

            resto_page = urllib.request.urlopen(urllib.request.Request(url), timeout=2)
            resto_soup = BeautifulSoup(resto_page, "lxml")

            # location
            location = None
            if (resto_soup.find(string="住所") != None):
                location = "\n".join(ts.translate_text(l.get_text().strip(), translator="google", from_language="ja") for l in resto_soup.find(string="住所").parent.parent.find_all("p"))

            # genre
            genres_list = [genre.get_text() for genre in resto_soup.find(string="ジャンル：").parent.parent.find_all("span")]

            genre = ts.translate_text(resto_soup.find(string="ジャンル：").parent.parent.find("span").get_text(), translator="google", from_language="ja")
            genre = ", ".join(ts.translate_text(g, translator="google", from_language="ja") for g in genres_list)

            # seats
            seats = None
            if (resto_soup.find(string="席数") != None):
                seats = " ".join(ts.translate_text(s.get_text().strip(), translator="google", from_language="ja") for s in resto_soup.find(string="席数").parent.parent.find_all("p"))


            # private room
            private_room = None
            if (resto_soup.find(string="個室") != None):
                private_room = " ".join(ts.translate_text(pr.get_text().strip(), translator="google", from_language="ja") for pr in resto_soup.find(string="個室").parent.parent.find_all("p"))


            restos.append(
                {"name" : name, "url" : url, "location" : location, "genre" : genre, "seats" : seats, "private_room" : private_room}
            )

        for resto in restos:
            print(f"""
{resto["name"]}
{resto["url"]}
{resto["location"]}
{resto["genre"]}
{resto["seats"]}
Private Room: {resto["private_room"]}
                  """, end="")

    except Exception as e:
        print("Error with webpage!\n")
        print(e)
        

def main():
    tabelog_url = input("Tabelog URL: ")
    # start time
    start = time.time()

    fetch_results(tabelog_url)

    # end time
    end = time.time()

    print("\nElapsed time: {:.2f} seconds".format(end - start))

if __name__ == "__main__":
    main()