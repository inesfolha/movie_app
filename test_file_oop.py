from storage_json import StorageJson
#list_movies_test
#storage_1 = StorageJson('movies_2.json')
#print(storage_1.list_movies())

#add_movies_test
#storage.add_movie("test_movie", 1234, 10, 'poster_link', 'movie_url')
#print(storage.list_movies())

#delete_movies_test
#storage.delete_movie("test_movie")
#print(storage.list_movies())
#storage.add_movie("test_movie", 1234, 10, 'poster_link', 'movie_url')
#storage.delete_movie("Test_movie")
#print(storage.list_movies())


#update_movies_test
#storage.add_movie("test_movie", 1234, 10, 'poster_link', 'movie_url')
#print(storage.list_movies())
#storage.update_movie("test_movie", "notesblabla afsdfsd oh+taodsfnsa")
#print(storage.list_movies())


from storage_csv import StorageCSV
from movie_app import MovieApp

storage = StorageCSV('movies.csv')
#print(storage.list_movies())
#storage.add_movie('Interstellar', 8.6,  2014, 'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg', 'https://www.imdb.com/title/tt0816692/')
storage.add_movie('Spider-Man: No Way Home', 8.2, 2021, 'https://m.media-amazon.com/images/M/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_SX300.jpg', 'https://www.imdb.com/title/tt10872600/')
#torage.add_movie('Inception', 8.8, 2010, 'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg', 'https://www.imdb.com/title/tt0816692/')
print(storage.list_movies())
#storage.delete_movie("Inception")
#storage.delete_movie('Spider-Man: No Way Home')
#storage.delete_movie("Interstellar")
#print(storage.list_movies())
#movie_app = MovieApp(storage)
#movie_app._command_list_movies()
#movie_app._command_movie_stats()
#movie_app.run()