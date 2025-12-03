#!/usr/bin/python3
import requests
import csv
def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder.
    Prints the status code.
    If successful, parses the JSON and prints the titles of the posts.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    # Print the status code as required
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        # Parse the response body into a JSON object (list of dictionaries)
        posts = response.json()
        # Iterate through the list and print the titles
        for post in posts:
            print(post['title'])
def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder.
    If successful, structures the data into a list of dictionaries
    (id, title, body) and writes it to a CSV file called posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        structured_data = []
        # Iterate through posts to create the structured list
        for post in posts:
            # Create a dictionary with only the required keys
            post_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_data.append(post_dict)
        # Write the data to a CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_data)
