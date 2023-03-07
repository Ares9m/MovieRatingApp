# === User interaction file ===
import database

MENU_PROMPT = """
options:

1) add new movie
2) see all movies
3) find movie by title
4) see best movie from a director
5) remove movie form list

0) exit

your selection: """


def menu():
    connection = database.connect()
    database.create_tables(connection)

    user_input = input(MENU_PROMPT)
    while user_input != "0":
        if user_input == "1":
            promopt_add_movie(connection)
        elif user_input == "2":
            prompt_get_all_movies(connection)
        elif user_input == "3":
            prompt_get_movies_by_title(connection)
        elif user_input == "4":
            prompt_get_best_movie_of_director(connection)
        elif user_input == "5":
            prompt_delete_movie(connection)
        # elif user_input == "6":
        #     pass
        else:
            print("invalid imput try again")
        user_input = input(MENU_PROMPT)

def prompt_add_movie(connection):
    if user_input == "1":
        title = input("title: ")
        year = int(input("release year: "))
        while len(str(year)) != 4:
            year = int(input("release year: "))
        director = input("director's full name: ")
        rating = int(input("enter your rating from 0 to 100: "))
        while rating < 0 or rating > 100:
            rating = int(input("enter your rating from 0 to 100: "))
        database.add_movie(connection, title, year, director, rating)

def prompt_get_all_movies(connection):
    movies = database.get_top_movies(connection)
    for movie in movies:
        print(f"{movie[1]} {movie[2]} by: {movie[3]} score: {movie[4]}/100")

def prompt_get_movies_by_title(connection):
    title = input("enter the title: ")
    movies = database.get_movies_by_name(connection, title)
    for movie in movies:
        print(f"{movie[1]} {movie[2]} by: {movie[3]} score: {movie[4]}/100")

def prompt_get_best_movie_of_director(connection):
    director = input("enter the director's full name: ")
    movies = database.get_best_movie_of_director(connection, director)
    print(f"the best move of {director} is: {movies[1]} with a score of: {movies[4]}/100")

def prompt_delete_movie(connection):
    movies = database.get_all_movies(connection)
    for movie in movies:
        print(f"Id: {movie[0]} | {movie[1]} {movie[2]} by: {movie[3]} score: {movie[4]}/100")
    Id = int(input("Id of a movie you want deleted: "))
    database.delete_a_movie(connection, Id)

if __name__ == '__main__':
    menu()


