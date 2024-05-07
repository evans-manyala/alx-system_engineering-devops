#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Prints titles of the first 10 hot posts from a subreddit.

    Args:
        subreddit: The name of the subreddit (e.g., "learnpython").
    """
    # Set a generic User-Agent to avoid throttling (replace with your username)
    headers = {'User-Agent': 'My Python Script 1.0 (by /u/generic_username)'}

    url = f'https://reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        # Send GET request, disallowing redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-200 status codes

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # Print titles of first 10 posts or handle empty list
        if posts:
            for post in posts[:10]:
                print(post.get('data', {}).get('title'))
        else:
            print(None)  # No posts found (possibly invalid subreddit)

    except requests.HTTPError:
        # Likely invalid subreddit or redirect (since redirects are disabled)
        print(None)
    except requests.RequestException as e:
        # Network or other request issues
        print(f"An error occurred: {e}")
