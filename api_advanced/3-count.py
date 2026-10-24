#!/usr/bin/python3
"""Counts keywords in the hot post titles of a subreddit using recursion."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print sorted keyword counts found in hot post titles of a subreddit."""
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:3-count:v1.0 (by /u/your_username)"}
    params = {"limit": 100, "after": after}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
    except requests.RequestException:
        return
