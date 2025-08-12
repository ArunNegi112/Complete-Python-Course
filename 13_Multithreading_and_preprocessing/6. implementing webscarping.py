from bs4 import BeautifulSoup
import requests
import threading
import time
## This is used for
# Web Scraping: Extracting data from HTML or XML documents.
# HTML Parsing: Navigating and manipulating the structure of a webpage. (Parsing means converting raw, unstructured data (like text, HTML, or JSON) into a structured format that is easier to work with programmatically.)
# Data Extraction: Finding specific elements like text, links, or tags in a web page.


urls = [
    'https://www.imdb.com/review/rw10088336/?ref_=tturv_perm_1',
    'https://www.imdb.com/review/rw10085656/?ref_=tturv_perm_2',
    'https://www.imdb.com/review/rw10087856/?ref_=tturv_perm_3'
]

t = time.time()
def fetch(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"This url {url} have {len(soup.text)} characters")   # we only getting number of characters from here, tho we can get more things too

threads = []

for url in urls:
    thread = threading.Thread(target=fetch,args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

final_time = time.time() - t
print(f"All urls are fetched in {final_time}")
