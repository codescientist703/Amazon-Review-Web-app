import csv
from scraper import getCSV, scrape
from summarization import summarization
from sentiment import sentiment
import json


def get_data(url, limit):
    pText = """"""
    nText = """"""
    positive = 0
    negative = 0
    neutral = 0
    reviewLength = 0
    getCSV(url, limit)
    with open("Dataset/data.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temp = json.loads(sentiment(row["content"]))
            if temp["errors"]:
                continue
            pScore = float(temp["documents"][0]["confidenceScores"]["positive"])
            nScore = float(temp["documents"][0]["confidenceScores"]["negative"])
            if pScore > 0.5:
                pText = pText + row["content"]
                positive += 1
            elif nScore > 0.5:
                nText = nText + row["content"]
                negative += 1
            else:
                neutral += 1
            reviewLength += 1
            # if cn == 20:
            #     break

    # print(pText)
    result = dict()
    nSummarization = json.loads(summarization(nText))
    pSummarization = json.loads(summarization(pText))
    if "snippets" in nSummarization:
        result["negative"] = nSummarization["snippets"]
    else:
        result["negative"] = ["No negative reviews to show."]

    if "snippets" in pSummarization:
        result["positive"] = pSummarization["snippets"]
    else:
        result["positive"] = ["No positive reviews to show."]

    result["pScore"] = round((positive / reviewLength) * 100, 2)
    result["nScore"] = round((negative / reviewLength) * 100, 2)
    result["neScore"] = round((neutral / reviewLength) * 100, 2)
    return result
