#!/usr/bin/python3
""" export TODO list progress for a given employee ID into a CSV file. """
import csv
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
        employee_name = employee.get("username")
        params = {"userId": employee_id}
        tasks = request.get(url + "todos", params=params).json()

        file = "{}.csv".format(employee_id)

        with open(file, 'x', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in tasks:
                writer.writerow([employee_id, employee_name,
                                 task.get("completed"),
                                 task.get("title")])

    except Exception:
        exit
