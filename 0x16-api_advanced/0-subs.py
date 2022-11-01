#!/usr/bin/python3
"""
This script queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function returns the number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    else:
        return 0
