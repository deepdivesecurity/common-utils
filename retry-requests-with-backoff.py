#!/usr/bin/env python

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import logging

def requests_with_retry(url, retries=3, backoff_factor=1, status_forcelist=(500,502,503,504)): 
    # Define retry strategy
    retry_strategy = Retry(total=retries, status_forcelist=status_forcelist, backoff_factor=backoff_factor)

    # Create an HTTP adapter with the retry info
    adapter = HTTPAdapter(max_retries=retry_strategy)

    # Create a new session object
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    # Attempt to get URL and handle any other errors that may occur (e.g. DNS resolution errors)
    try: 
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e: 
        # Log error
        print("This should change to regular logging")
        
    return None

def main(): 
    response = requests_with_retry("https://google.ca")

    if response == None: 
        print("Nothing returned")
    elif response.status_code == 200:
        print("Success")
    else:
        print("Failed")

if __name__ == "__main__": 
    main()