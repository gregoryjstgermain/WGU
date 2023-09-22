"""
Write a program that reads movie data from a CSV (comma separated values) file and output the data in a formatted table.
The program first reads the name of the CSV file from the user. The program then reads the CSV file and outputs the
contents according to the following requirements:

    Each row contains the title, rating, and all showtimes of a unique movie.
    A space is placed before and after each vertical separator ('|') in each row.
    Column 1 displays the movie titles and is left justified with a minimum of 44 characters.
    If the movie title has more than 44 characters, output the first 44 characters only.
    Column 2 displays the movie ratings and is right justified with a minimum of 5 characters.
    Column 3 displays all the showtimes of the same movie, separated by a space.

Each row of the CSV file contains the showtime, title, and rating of a movie.
Assume data of the same movie are grouped in consecutive rows.

Ex: If the input of the program is:

movies.csv

and the contents of movies.csv are:

16:40,Wonders of the World,G
20:00,Wonders of the World,G
19:00,Journey to Space,PG-13
12:45,Buffalo Bill And The Indians or Sitting Bull's History Lesson,PG
15:00,Buffalo Bill And The Indians or Sitting Bull's History Lesson,PG
19:30,Buffalo Bill And The Indians or Sitting Bull's History Lesson,PG
10:00,Adventure of Lewis and Clark,PG-13
14:30,Adventure of Lewis and Clark,PG-13
19:00,Halloween,R

the output of the program is:

Wonders of the World                         |     G | 16:40 20:00
Journey to Space                             | PG-13 | 19:00
Buffalo Bill And The Indians or Sitting Bull |    PG | 12:45 15:00 19:30
Adventure of Lewis and Clark                 | PG-13 | 10:00 14:30
Halloween                                    |     R | 19:00


"""
import csv
movie_times = {}
#filename = input()
filename = 'movies.csv'

with open(filename, 'r') as csvfile:
    movies = csv.reader(csvfile, delimiter=',')

    #i = next(movies)
    #for row in movies:
    #    print(f'Row #{row_num}:', row)
    #    row_num += 1

    try:
        for row in movies:
            #row = (row, next(movies))
            #if row[1] == row[1]:

            i = next(movies)
            #print(f"{row[1] :<44} | {row[2] :>5} | {row[0]}")
            if row[1] in i:
                print("{:.44} | {:>5} | {} {}".format(row[1], row[2], row[0], i[0]))
            else:
                print("{:44} | {:>5} | {}".format(row[1], row[2], row[0]))
            """
            if row[1] in i:
                print(f"{row[1] :<44s} | {row[2] :>5} | {row[0]} {i[0]}")
            else:
                print(f"{row[1] :<44s} | {row[2] :>5} | {row[0]}")
            """
    except StopIteration:
        a = 10
#file = open(filename, "r")
#lines = file.readlines()

#for line in lines:
#    print(line)
#    a = line.split(',')
#    print(f'{a[0]}')