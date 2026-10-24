#!/usr/bin/python3
"""Prints the status code Reddit gives for a subreddit."""
import requests


def top_ten(subreddit):
    """Print the status code or the error for a subreddit request."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:1-top_ten:v1.0 (by /u/your_username)"}
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        print(response.status_code)
    except requests.RequestException as error:
        print(type(error).__name__)
