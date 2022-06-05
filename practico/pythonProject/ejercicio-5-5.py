db_movies = [{'movie':'Star Wars', 'availability': 5},
             {'movie':'Matrix', 'availability': 12},
             {'movie':'Kill Bill', 'availability': 3},
             {'movie':'Jurassic Park', 'availability': 0},
             {'movie':'Se7en', 'availability': 3},
             {'movie':'Casino', 'availability': 4},
             {'movie':'Memento', 'availability': 0}]

def search_movie(movie):
    for mov in db_movies:
        if movie == mov.keys():
            print('si')

search_movie('Kill Bill')