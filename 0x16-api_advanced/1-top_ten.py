#!/usr/bin/python3
""" 1-top_ten """
import requests
import json


def top_ten(subreddit):
    """ prints top ten hot posts of a subreddit """
    subreddit = 'python'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = json.loads(response.text)
        for post in data['data']['children'][:10]:
            title = post['data']['title']
            print(title)
    else:
        print('None')
