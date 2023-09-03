# This a dummy module
# This gets called in the module_main.py file

from __future__ import annotations

import json
import logging

from app.core.config import DATA_URL as data_url


def get_data(errors):
    # Get data from data/conversation.json
    try:
        with open('app/data/conversation.json', "r") as json_file:
            data = json.load(json_file)
    except Exception as e:
        handle_error(errors, "Error loading data", e)
    finally:
        # close file
        json_file.close()

    # Return data
    return data

def handle_error(errors, error_message, exception):
    error = f"{error_message}: {exception}"
    errors.append(error)
    logging.error(error)