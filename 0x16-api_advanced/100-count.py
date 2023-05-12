import requests
import re

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise ValueError("Request failed")

    data = response.json()["data"]
    after = data["after"]

    for post in data["children"]:
        title = post["data"]["title"].lower()
        for word in word_list:
            word = word.lower()
            if re.search("\\b{}\\b".format(word), title):
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

    if len(counts) == 0:
        return



