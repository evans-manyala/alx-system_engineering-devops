#!/usr/bin/python3
"""Python funtion that returns the
total number of subscribers on a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        allow_redirects=False,
        headers={"user_agent": "Chrome/13.0"},
    )

    return (
        response.json()["data"]["subscribers"]
        if response.status_code == 200
        else 0
    )
