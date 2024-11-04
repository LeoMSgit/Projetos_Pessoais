#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'bestInGenre' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING genre as parameter.
# Base URL: https://jsonmock.hackerrank.com/api/tvseries?page=
#

def bestInGenre(genre):
    base_url = "https://jsonmock.hackerrank.com/api/tvseries?page="
    best_show = None
    highest_rating = -1
    
    # Initialize the page number to 1
    page = 1
    
    while True:
        # Make a request to the API
        response = requests.get(f"{base_url}{page}")
        data = response.json()
        
        # Process each show in the data
        for show in data['data']:
            # Check if the genre matches
            if genre in show['genre']:
                # Check if this show has a higher rating
                if (show['imdb_rating'] > highest_rating) or (show['imdb_rating'] == highest_rating and (best_show is None or show['name'] < best_show)):
                    best_show = show['name']
                    highest_rating = show['imdb_rating']
        
        # Check if there are more pages
        if page >= data['total_pages']:
            break
        page += 1
    
    return best_show

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    genre = input()

    result = bestInGenre(genre)

    fptr.write(result + '\n')

    fptr.close()
