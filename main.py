import requests as r
from bs4 import BeautifulSoup as b
import time

website = input("Enter URL: ")

url = r.get(website)

if url.status_code == 200:

    soup = b(url.content, "html.parser")
    tag = input("Enter HTML TAG: ")
    class_id = input("Input class ID: ")
    content = soup.find_all(tag, class_=class_id)

    if content:
        for sub in content:
            with open("extracted_data.txt", "a", newline= "", encoding="utf-8") as data:
                data.write(f"{sub.get_text().strip()}\n")
            time.sleep(0.5)
    else:
        print("No Data to Extract!")


