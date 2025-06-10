#!/sur/bin/python3
"""This module fetches posts from JSONPlaceholder

Attributes:
    url (str): url of JSONPlaceholder
    response (object): response from http request
    json_data (object): response as json
"""

import requests
import csv

# Defining the URL
url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints the titles."""

    #sending request
    response = requests.get(url)

    #printing response status code
    print("Status code: {}".format(response.status_code))

    #fetching data if response code successful
    if response.status_code == 200:
        json_data = response.json()

    #printing titles of all posts
        for post in json_data:
            print(post["title"])

    #if not successful
    else:
        print("Request not successful")


def fetch_and_save_posts():
    """Fetches all posts from JSONPlaceholder
    and saves them in a csv file."""

    # Sending the request
    response = requests.get(url)

    # Printing the response status code
    print(f"Status Code: {response.status_code}")

    # Fetching the data if request is successful
    if response.status_code == 200:
        json_data = response.json()
        csvf = 'posts.csv'
        datalist = []

        # Creating new list element for each post
        for element in json_data:
            post = {
                'id': element.get('id'),
                'title': element.get('title'),
                'body': element.get('body')
            }
            datalist.append(post)

        # Writing to the csv file
        with open(csvf, 'w', encoding='UTF-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(datalist)

    # If request is not successful
    else:
        print("Request was not successful.")
