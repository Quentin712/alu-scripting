#!/usr/bin/python3
"""Gets the number of subscribers of a subreddit from the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Return the total subscribers of a subreddit, or 0 if it is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0-subs:v1.0 (by /u/your_username)"}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=10)
    except requests.RequestException:
        return 0
    if response.status_code != 200:
        return 0
    try:
        return response.json().get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
