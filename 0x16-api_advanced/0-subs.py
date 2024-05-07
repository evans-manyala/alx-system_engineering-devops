#!/usr/bin/python3
"""
Python Script queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
  """Queries Reddit API for subscriber count of a subreddit.

  Args:
      subreddit: The name of the subreddit (e.g., "learnpython").

  Returns:
      The number of subscribers for the subreddit or 0 if invalid.
  """
  # Set a custom User-Agent to avoid Too Many Requests error
  headers = {'User-Agent': 'My Python Script 1.0 (by /u/your_username)'}  # Replace with your username
  url = f'https://reddit.com/r/{subreddit}/about.json'

  try:
    # Send GET request, disallowing redirects
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()  # Raise exception for non-200 status codes

    # Parse JSON data, handle potential missing keys
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)

  except requests.HTTPError:
    # Likely invalid subreddit or redirect (since redirects are disabled)
    return 0
  except requests.RequestException as e:
    # Network or other request issues
    print(f"An error occurred: {e}")
    return 0
