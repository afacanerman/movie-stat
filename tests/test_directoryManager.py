__author__ = 'afacanerman'

import os
from unittest import TestCase
from DirectoryManager import DirectoryManager

TEST_DIRECTORY = "./testDirectory"


class TestDirectoryManager(TestCase):
    def setUp(self):
        if not os.path.exists(TEST_DIRECTORY):
            os.makedirs(TEST_DIRECTORY)
        if not os.path.exists(TEST_DIRECTORY + "/movie1"):
            os.makedirs(TEST_DIRECTORY + "/movie1")
        if not os.path.exists(TEST_DIRECTORY + "/movie2"):
            os.makedirs(TEST_DIRECTORY + "/movie2")
        if not os.path.exists(TEST_DIRECTORY + "/test movie_2014_7.5"):
            os.makedirs(TEST_DIRECTORY + "/test movie_2014_7.5")

        self.dm = DirectoryManager(TEST_DIRECTORY)


    def test_get_movie_directories(self):
        dirs = self.dm.get_movie_directories()
        assert len(dirs) == 2
        assert dirs[0] == "movie1"
        assert dirs[1] == "movie2"

    def test_remove_unexpected_string(self):
        filtered_string = self.dm.remove_unexpected_string('Whiplash.2014.BluRay\'.720p[1995]')
        assert filtered_string == 'Whiplash 2014'


    def tearDown(self):
        if os.path.exists(TEST_DIRECTORY + "/test movie_2014_7.5"):
            os.removedirs(TEST_DIRECTORY + "/test movie_2014_7.5")
        if os.path.exists(TEST_DIRECTORY + "/movie2"):
            os.removedirs(TEST_DIRECTORY + "/movie2")
        if os.path.exists(TEST_DIRECTORY + "/movie1"):
            os.removedirs(TEST_DIRECTORY + "/movie1")
        if os.path.exists(TEST_DIRECTORY):
            os.removedirs(TEST_DIRECTORY)