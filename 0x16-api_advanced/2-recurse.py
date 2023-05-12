#!/usr/bin/python3
""" 2-recurse"""
import requests


def recurse(subreddit, after=None, titles=None):
    """
    Recursive function that queries the Reddit API and returns a list\
        containing the titles of all hot articles for a given subreddit.
    """
    # Set up the API URL
    url = "https://www.reddit.com/r/{}/hot.json?".format(subreddit)
    if after:
        url += "&after={}".format(after)

    # Set custom User-Agent header
    headers = {'User-Agent': 'my-bot/0.0.1'}

    # Make the API request
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    # Extract the post data from the response
    data = response.json()['data']
    after = data['after']
    posts = data['children']

    # Add the titles of the posts to the list
    if not titles:
        titles = []
    for post in posts:
        titles.append(post['data']['title'])

    # Recurse if there are more posts to retrieve
    if after:
        return recurse(subreddit, after, titles)

    return titles
