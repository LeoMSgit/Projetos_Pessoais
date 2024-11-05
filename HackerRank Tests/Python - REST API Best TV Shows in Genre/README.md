Use the HTTP GET method to retrieve information about recent television shows. Query https://jsonmock.hackerrank.com/api/tvseries to find all the shows in a genre. The query result is paginated. To access additional pages, append ?page={num} to the URL where num is the page number.

The response is a JSON object with the following 5 fields:
page: the current page of the results (Number)
per_page: the maximum number of results returned per page (Number)
total: the total number of results (Number)
total_pages: the total number of pages with results (Number)
data: an array of tv series records

Example of a data  array object:
    "name": "Game of Thrones",
    "runtime_of_series": "(2011–2019)",
    "certificate": "A",
    "runtime_of_episodes": "57 min",
    "genre": "Action, Adventure, Drama",
    "imdb_rating": 9.3,
    "overview": "Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.",
    "no_of_votes": 1773458,
    "id": 1


In data, each tv series has the following schema:
name: (String)
runtime_of_series: years with a new season (String)
certificate: rating (String)
runtime_of_episodes: average length per episode in minutes (String).
genre: genre (String)
imdb_rating: average viewer rating (Number)
overview: short description (String)
no_of_votes: how many votes were cast at imdb (Number)
id: unique id (Number) 

Given a genre, find the series with the highest imdb_rating. If there is a tie, return the alphabetically lower name.

Function Description
bestInGenre has the following parameter(s):
    string genre: the genre to search

Return
string: the highest-rated show in the genre, with the lowest name alphabetically if there is a tie

Note: Please review the header in the code stub to see available libraries for API requests in the selected language. Required libraries can be imported in order to solve the question. Check our full list of supported libraries at https://www.hackerrank.com/environment
