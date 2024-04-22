#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""

import requests
from sys import argv


def fetch_todo_progress(employee_id):
    """Fetch the employee id"""
    URL = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(URL)
    return response.json()


def fetch_user(employee_id):
    """Fetch  the user associated with the resource"""
    URL = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(URL)
    user_data = response.json()
    name = user_data.get('name')
    return name


def display_tasks(employee_id):
    """Show the completed tasks for a user"""
    tasks_data = fetch_todo_progress(employee_id)
    num_of_tasks = len(tasks_data)
    completed_tasks = sum(task['completed'] for task in tasks_data)
    return completed_tasks, num_of_tasks


if __name__ == '__main__':
    employee_id = argv[1]
    complete_task, sum_tasks = display_tasks(employee_id)
    user = fetch_user(employee_id)

    print(f"Employee {user} is done with tasks({complete_task}/{sum_tasks}):")
    for task in fetch_todo_progress(employee_id):
        if task['completed']:
            print(f"\t {task['title']}")
