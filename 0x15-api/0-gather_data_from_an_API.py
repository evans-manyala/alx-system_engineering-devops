#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    URL = "https://jsonplaceholder.typicode.com/users"
    employee_url = f"{URL}/{employee_id}"
    todo_url = f"{URL}/{employee_id}/todos"
    
    try:
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        employee_data = employee_response.json()
        
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo_data = todo_response.json()
        
        employee_name = employee_data.get("name")
        completed_tasks = [task for task in todo_data if task["completed"]]
        total_tasks = len(todo_data)
        
        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
        
        for task in completed_tasks:
            print(f"\t{task['title']}")
        
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)

