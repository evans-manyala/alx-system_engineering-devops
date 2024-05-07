#!/usr/bin/python3
"""Python funtion that returns the
total number of subscribers on a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Python funtion that returns the total number of subscribers on a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome / 13.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
