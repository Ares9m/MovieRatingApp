# === User interaction file ===
import database

MENU_PROMPT = """
options:

1) add new movie
2) see all movies
3) find movie by title
4) see best movie of a director
5) remove movie form list
6) change the score of a movie
0) exit

your selection: """


def menu():
    connection = database.connect()
    database.create_tables(connection)

    user_input = input(MENU_PROMPT)
    while user_input != "0":
        # it would be better to turn all this into seprate functions
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
        elif user_input == "2":
            movies = database.get_all_movies(connection)
            for movie in movies:
                print(f"{movie[1]} {movie[2]} by: {movie[3]} score: {movie[4]}/100")
        elif user_input == "3":
            title = input("enter the title: ")
            movies = database.get_movies_by_name(connection, title)
            for movie in movies:
                print(f"{movie[1]} {movie[2]} by: {movie[3]} score: {movie[4]}/100")
        elif user_input == "4":
            director = input("enter the director's full name: ")
            movies = database.get_best_movie_of_director(connection, director)
            print(f"the best move of {director} is: {movies[1]} with a score of: {movies[4]}/100")
        elif user_input == "5":
            movies = database.get_all_movies(connection)
            for movie in movies:
                print(f"Id: {movie[0]} | {movie[1]} {movie[2]} by: {movie[3]} score: {movie[4]}/100")
            Id = int(input("Id of a movie you want deleted: "))
            database.delete_a_movie(connection, Id)
        elif user_input == "6":
            pass
        else:
            print("invalid imput try again")
        user_input = input(MENU_PROMPT)

menu()


