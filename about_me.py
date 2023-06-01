"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        # TODO: Put full name into data structure
        'name' : 'Bansari Patel',
        # TODO: Put student ID into data structure
        'Student ID' : '10296950',
        # TODO: Put list of 3 pizza toppings into data structure
        'Pizza Toppings' : [
            'Tomatos',
            'Green Pepper',
            'Mushrooms'
        ],
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'Twilight',
                'genre': 'Rommantic'
            },
            # TODO: Add one more movie
            {
                'title' : 'Suryavanshi',
                'genre' : 'Action'
            },
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['Pineapple', 'Jalapenos'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'The Fantasy Island', 'Suspense')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    # Print sentence containing student ID
    print(f"My name is {my_info['name']}.\nMy student ID is {my_info['Student ID']}.")
    print()
    

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    # Print bullet list of favourite pizza toppings
    
    print(f"My favourite pizza toppings are: ")
    
    for toppings_on_pizza in my_info['Pizza Toppings']:
        print(f"- {toppings_on_pizza}")
        
def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    my_info['Pizza Toppings'].extend(toppings)
    # Convert all pizza toppings to lowercase
    # Sort toppings list alphabetically
    for i, toppings_on_pizza in enumerate(my_info['Pizza Toppings']):
        my_info['Pizza Toppings'][i] = toppings_on_pizza.capitalize()

    my_info['Pizza Toppings'].sort()
    print()
    return add_pizza_toppings


def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    another_movie = {
        'title' : title,
        'genre' : genre
    }
    my_info['movies'].append(another_movie)
    print()
    return add_movie

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres


    Args:
        my_info (dict): Data structure containing information about me
   """
    # TODO: Complete function body per Step 7
    
    print(f"I like to watch", end = ' ')
   # print(', '.join(movie), end='.')
    
    for i, movie in enumerate(my_info['movies']):
        print(movie['genre'], end = ', ')


def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    print(f"movies.\n")
    movie_list = [movie['title'] for movie in movie_list]
    print(f"Some of my favourite movies are",end=" ")

#for i, movie in enumerate(movie_list['movies']):
   # print(movie['title'])

    print(', '.join(movie_list), end='.')



if __name__ == '__main__':
    main()



