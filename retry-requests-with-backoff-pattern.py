#!/usr/bin/env python

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import logging

def requests_with_retry(url: str, retries: int = 3, backoff_factor: int = 1, status_forcelist: set[int]=(500,502,503,504)) -> str: 
    """_summary_

    Args:
        url (str): The URL that the user is requesting
        retries (int, optional): The number of times to retry connecting to the URL. Defaults to 3.
        backoff_factor (int, optional): Base value of delay to use in between retry attempts. Defaults to 1.
        status_forcelist (set[int], optional): Set of HTTP error codes to force a retry on. Defaults to (500,502,503,504).

    Returns:
        str: _description_
    """

    # Define retry strategy
    retry_strategy = Retry(total=retries, status_forcelist=status_forcelist, backoff_factor=backoff_factor)

    # Create an HTTP adapter with the retry info
    adapter = HTTPAdapter(max_retries=retry_strategy)

    # Create a new session object
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    # Attempt to get response and handle any other errors that may occur (e.g. DNS resolution errors)
    try: 
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e: 
        # Log error
        print("Change to regular logging")
    
    # Return None for graceful error handling
    return None