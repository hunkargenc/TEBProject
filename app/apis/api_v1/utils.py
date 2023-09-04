# This a dummy module
# This gets called in the module_main.py file

from __future__ import annotations

import json
import logging
import os

from app.core.config import DATA_URL as data_url
from app.core.config import MODEL_URL as model_url

from transformers import pipeline

def get_data(errors):
    # Get data from data/conversation.json
    try:
        with open(data_url, "r") as json_file:
            data = json.load(json_file)
    except Exception as e:
        handle_error(errors, "Error loading data", e)
    finally:
        # close file
        json_file.close()

    # Return data
    return data

def get_model():

    # if inside models file is not None
    try:
        if len(os.listdir(model_url))>1:
            is_model = True
        else:
            is_model = False
    except FileNotFoundError:
        is_model = False

    if is_model:
        # Load the BART model and tokenizer
        bart_model = pipeline("zero-shot-classification", model=model_url)   
    else:
        # Load the sentiment classification pipeline
        bart_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        
        # Save the BART model to a local file
        bart_model.save_pretrained(model_url)

    return bart_model

def handle_error(errors, error_message, exception):
    error = f"{error_message}: {exception}"
    errors.append(error)
    logging.error(error)