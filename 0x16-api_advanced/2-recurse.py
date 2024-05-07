#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    - If not a valid subreddit, return None.
    """
    headers = {'User-Agent': 'Custom'}
    url = f'https://reddit.com/r/{subreddit}/hot.json?after={after}'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-200 status codes

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # Extract titles and handle empty list
        if posts:
            hot_list.extend([post.get('data', {}).get('title')
                             for post in posts])

        # Check for "after" parameter for pagination (if available)
        after = data.get('data', {}).get('after')

        # Recursively call if there's more data (after parameter)
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list  # No more data, return accumulated list

    except requests.HTTPError:
        # Likely invalid subreddit or redirect (since redirects are disabled)
        return None
    except requests.RequestException as e:
        # Network or other request issues
        print(f"An error occurred: {e}")
        return None
