import json

from colorama import Fore, init
import file_handler

init()


def serialize_info(movies_dict):
    """Serializes the dictionary info into a formatted string"""
    str_output = ""
    # serialize the info from the movies
    for movie in movies_dict.keys():
        rating = movies_dict[movie]['rating']
        year = movies_dict[movie]['release_year']
        poster = movies_dict[movie]['poster']
        notes = movies_dict[movie].get('notes')
        link = movies_dict[movie]['movie_link']

        # format a html string with that info
        str_output += f"""
         <li>
         
            <div class="movie">
                <a href="{link}">
                    <img class="movie-poster"
                         src={poster} title="{notes}"/></a>
                    <div class="movie-title">{movie} - {rating}</div>
                    <div class="movie-year">{year}</div>
            </div>
        </li>
         
     """
    return str_output


def html_generator(movies_dict):
    """Takes a formatted string and writes it into an HTML file."""
    # Load the template from the file
    movies_template = file_handler.load_document('index_template.html')

    # Replace the title placeholder with the formatted title
    title = 'My Movies List'
    movies_template = movies_template.replace('__TEMPLATE_TITLE__', title)

    # Replace the movie grid placeholder with the serialized movie info
    movies_info_output = serialize_info(movies_dict)
    movies_template = movies_template.replace('__TEMPLATE_MOVIE_GRID__', movies_info_output)

    # Save the HTML file
    file_handler.save_html('movies-app.html', movies_template)
    print(Fore.GREEN + "Website successfully updated" + Fore.RESET)
