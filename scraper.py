from selectorlib import Extractor
import requests
import json
from time import sleep
import csv

e = Extractor.from_yaml_file("selectors.yml")


def scrape(url):
    headers = {
        "authority": "www.amazon.in",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "dnt": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-dest": "document",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    }
    try:
        r = requests.get(url, headers=headers)
    except:
        return -1
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print(
                "Page %s was blocked by Amazon. Please try using better proxies\n" % url
            )
        else:
            print(
                "Page %s must have been blocked by Amazon as the status code was %d"
                % (url, r.status_code)
            )
        return None
    return e.extract(r.text)


def getCSV(url, limit):
    with open("Dataset/data.csv", "w") as outfile:
        writer = csv.DictWriter(
            outfile,
            fieldnames=[
                "title",
                "content",
                "rating",
            ],
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        page = 1
        cn = 0
        while 1:
            ha = f"&pageNumber={page}"
            data = scrape(url + ha)
            if cn == limit:
                break
            if data["reviews"] != None:
                for r in data["reviews"]:
                    r["rating"] = r["rating"].split(" out of")[0]
                    del r["variant"]
                    del r["author"]
                    del r["verified"]
                    del r["images"]
                    del r["date"]
                    writer.writerow(r)
                    cn += 1
                    if cn == limit:
                        break
                # sleep(4)
            else:
                break
            page += 1


# getCSV(
#     "https://www.amazon.in/Test-Exclusive-550/product-reviews/B077Q7GW9V/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
# )
