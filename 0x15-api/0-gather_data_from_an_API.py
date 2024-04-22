#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""

import requests
import sys

URL = "https://jsonplaceholder.typicode.com/users/"


def fetch_todo_progress(employee_id):
    """Get the employee id"""
    return requests.get(f"{URL}/{user_id}/todos").json()


def get_completed_tasks(tasks: "list[dict]") -> "list[dict]":
    """Returns all the TODO tasks that the user has completed.
    """
    return [task for task in tasks if task.get("completed") is True]


def print_completed_tasks(
        user: str, num_of_tasks: int, completed_tasks: "list[dict]"
) -> None:
    """
    Shows the completed tasks for a given user.
    """
    print(
        f"Employee {user} is done with "
        f"tasks({len(completed_tasks)}/{num_of_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


def get_name(user_id: int) -> "str | None":
    """
     Fetches name associated with the user ID from API.
    """
    return requests.get(f"{URL}/{user_id}").json().get("name", None)


def get_username(user_id):
    """
    Retrieves the name associated with the given user ID from an API.
    """
    return requests.get(f"{URL}/{user_id}").json().get("username", None)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <user_id>\n")
        sys.exit(1)

    user = get_name(sys.argv[1])
    if user is None:
        sys.stderr.write("Invalid user id.\n")
        sys.exit(1)

    todos = get_todos(sys.argv[1])
    completed_tasks = get_completed_tasks(todos)
    print_completed_tasks(user, len(todos), completed_tasks)
