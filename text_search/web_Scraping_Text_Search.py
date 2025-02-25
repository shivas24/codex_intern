import requests
from bs4 import BeautifulSoup

def search(query):
    headers={
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    search_url=f"https://www.bing.com/search?q={query.replace(' ', '+')}"
    response=requests.get(search_url, headers=headers)

    if response.status_code ==200:
        '''print("Error in search.",response.status_code)
        return'''

        soup=BeautifulSoup(response.text, "html.parser")
        results=soup.find_all("li", class_="b_algo",limit=5)

        if not results :
            print("No results found.")
            return

        for i,search in enumerate(results,start=1):
            title=search.find("h2").text  if search.find("h2") else "Title Not found"
            link=search.find('a')['href'] if search.find("a") else "Link not found"
            desc=search.find('p').text if search.find('p') else "no text found"

            print(f"{i}.  title::{title} ")
            print(f"     Link:: {link}")
            print(f"     text:: {desc}")
        else:
            print("Error in search.",response.status_code)
            return

query=input("Enter Input:::\n")
search(query)
