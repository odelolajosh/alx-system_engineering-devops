#!/usr/bin/python3
""" export TODO list progress for a given employee ID into a JSON file. """
import json
import requests as request
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usage = "Usage: ./0-gather_data_from_an_API.py <employee_id>"

    try:
        if len(sys.argv) != 2:
            raise ValueError(usage)

        employee_id = int(sys.argv[1])
        number_of_tasks = 0
        number_of_done_tasks = 0
        titles = []

        employee = request.get(url + "users/{}".format(employee_id)).json()
        params = {"userId": employee_id}
        tasks = request.get(url + "todos", params=params).json()

        employee_name = employee.get("username")
        file = "{}.json".format(employee_id)

        value = []
        for task in tasks:
            value.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name
            })

        with open(file, 'x', newline='') as f:
            json.dump({employee_id: value}, f)
    except Exception:
        exit
