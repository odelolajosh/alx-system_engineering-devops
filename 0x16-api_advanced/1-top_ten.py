#!/usr/bin/python3
"""
This script queries the Reddit API
"""
import requests

# disable requests warnings
requests.packages.urllib3.disable_warnings()


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a
    given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        for i in range(10):
            print(r.json().get('data')
                  .get('children')[i].get('data').get('title'))
    else:
        print(None)
