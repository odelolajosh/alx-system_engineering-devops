#!/usr/bin/python3
""" export TODO list progress for a given employee ID into a JSON file. """
import json
import requests as request
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    file = "todo_all_employees.json"

    try:
        number_of_tasks = 0
        number_of_done_tasks = 0
        titles = []

        employees = request.get(url + "users").json()
        content = {}

        for employee in employees:
            employee_name = employee.get("username")
            params = {"userId": employee.get("id")}
            tasks = request.get(url + "todos", params=params).json()

            value = []
            for task in tasks:
                value.append({
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": employee_name
                })

            content[employee.get("id")] = value

        with open(file, 'x', newline='') as f:
            json.dump(content, f)
    except Exception:
        exit
