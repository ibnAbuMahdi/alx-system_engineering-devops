#!/usr/bin/python3
''' count subs of a subreddit '''
from os import getenv
import requests


def number_of_subscribers(subreddit):
    """ returns number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'myBot/0.0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    else:
        return 0
