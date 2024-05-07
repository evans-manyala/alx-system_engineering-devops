#!/usr/bin/python3
"""Python funtion that returns the
total number of subscribers on a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Chrome/13.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json().get("data", {})
        subscribers = data.get("subscribers", 0)
        return subscribers
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return 0
