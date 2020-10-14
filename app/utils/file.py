import os
from app import app


def get_current_path(file=""):
    """
    Pass __file__ to get your current file path
    :param file: __file__
    :return: string
    """

    try:
        return os.path.dirname(os.path.abspath(file))
    except Exception as e:
        print("ERROR: get_current_path(file)", e)
        return ""


def get_file_path(file_path=""):
    project_path = app.config.get("ROOT_PATH")

    try:
        return os.path.join(project_path, file_path)
    except Exception as e:
        print("ERROR: get_file_path(file_path)", e)
        return ""
