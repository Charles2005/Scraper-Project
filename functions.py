"""

This file will contain all the functions we need for
the this project.

"""
import os


def create_directory(folder_name):
    """
    Create a directory for the files we will scrape
    :param folder_name:
    :return None:
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def create_files(path):
    """
    Creating a new files in a specific folder
    :param path:
    :return none:
    """
    f =  open(path, 'w')
    f.write("")
    f.close()


def file_writer(path, data):
    """
    This will write to the file we will create
    :param path:
    :param data:
    :return None:
    """
    with open(path, "a") as file:
        file.write(data + "\n")


def delete_item(path):
    """
    Delete the items/data in a file
    :param path:
    :return None:
    """
    f = open(path, "w")
    f.close()


def search_existing_file(path):
    """
    Search if the file is already existed in the directory
    :param path:
    :return Boolean value:
    """
    return os.path.isfile(path)


def read_files(path):
    """
    Reading the files we created
    :param path:
    :return:
    """
    with open(path, "rt") as f:
        for line in f:
            print(line.replace("\n", ""))










