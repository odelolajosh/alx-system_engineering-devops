#!/usr/bin/python3
"""
This script queries the Reddit API
"""
import requests

# disable requests warnings
requests.packages.urllib3.disable_warnings()


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    params = {'after': after}
    r = requests.get(url, headers=headers, params=params,
                     allow_redirects=False)
    if r.status_code == 200:
        for i in range(len(r.json().get('data').get('children'))):
            hot_list.append(r.json().get('data').get(
                'children')[i].get('data').get('title'))
        if r.json().get('data').get('after') is not None:
            return recurse(subreddit, hot_list, r.json()
                           .get('data').get('after'))
        else:
            return hot_list
    else:
        return None
