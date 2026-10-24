#!/usr/bin/python3
"""Gets the titles of all hot posts of a subreddit using recursion."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return all hot post titles, or None if the subreddit is invalid."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:2-recurse:v1.0 (by /u/your_username)"}
    params = {"limit": 100, "after": after}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
    except requests.RequestException:
        return None
    if response.status_code != 200:
        return None
    try:
        data = response.json().get("data", {})
    except ValueError:
        return None
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
