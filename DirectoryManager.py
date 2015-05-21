__author__ = 'develoopers'

import re
from os import walk


class DirectoryManager:
    def __init__(self, directory_path):
        self.movieDirectory = directory_path

    def get_movie_directories(self):

        movie_dir_list = []
        return_list = []

        for (dirpath, dirnames, filenames) in walk(self.movieDirectory):
            movie_dir_list = dirnames
            break

        for movie_path in movie_dir_list:
            if not re.match('.*?_(\d*)_\d.\d', movie_path):
                return_list.append(self.remove_unexpected_string(movie_path))

        return return_list

    def remove_unexpected_string(self, movie_path):
        # remove [text]
        movie_path = re.sub('\[(.*?)\]', '', movie_path)
        # replace . with ' '
        movie_path = re.sub('(720p|320p|BluRay)', '', movie_path)
        # replacements
        movie_path = movie_path.replace('.', ' ') \
            .replace('_', ' ') \
            .replace('-', '') \
            .replace('\'', '')\
            .lstrip().rstrip()

        return movie_path