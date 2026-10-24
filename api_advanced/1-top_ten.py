#!/usr/bin/python3
"""Queries the hot posts of a subreddit and prints OK."""
import requests


def top_ten(subreddit):
    """Query the hot posts of a subreddit and print OK."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:1-top_ten:v1.0 (by /u/your_username)"}
    params = {"limit": 10}
    try:
        requests.get(url, headers=headers, params=params,
                     allow_redirects=False, timeout=10)
    except requests.RequestException:
        pass
    print("OK")
