#!/usr/bin/env python

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import logging

# Basic logging configuration
logging.basicConfig(
    # Default logging level
    level=logging.DEBUG,
    # Format of log
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    # Log to a file in append mode
    handlers=[
        logging.FileHandler('retry-requests-with-backoff-pattern.log', mode='a')
    ]
)

def requests_with_retry(url: str, retries: int = 3, backoff_factor: int = 1, status_forcelist: set[int]=(500,502,503,504)) -> str: 
    """ requests_with_retry: Attempts to connect to a URL using the retry with backoff pattern in the case of a set of passed in errors

    Args:
        url (str): The URL that the user is requesting
        retries (int, optional): The number of times to retry connecting to the URL. Defaults to 3.
        backoff_factor (int, optional): Base value of delay to use in between retry attempts. Defaults to 1.
        status_forcelist (set[int], optional): Set of HTTP error codes to force a retry on. Defaults to (500,502,503,504).

    Returns:
        str: Response from the URL request; None if error encountered
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
        response.raise_for_status()
        
        return response
    
    except requests.exceptions.Timeout as e:
        logging.exception(f"Request timed out: {e}")
    
    except requests.exceptions.TooManyRedirects as e:
        logging.exception(f"Too many redirects: {e}")
    
    except requests.exceptions.ConnectionError as e:
        logging.exception(f"Connection error: {e}")
    
    except requests.exceptions.HTTPError as e:
        logging.exception(f"HTTP error occurred: {e}")
    
    except requests.exceptions.JSONDecodeError as e:
        logging.exception(f"JSON decoding error: {e}")
    
    except requests.exceptions.ProxyError as e:
        logging.exception(f"Proxy error: {e}")
    
    except requests.exceptions.SSLError as e:
        logging.exception(f"SSL error: {e}")
    
    except requests.exceptions.ContentDecodingError as e:
        logging.exception(f"Content decoding error: {e}")
    
    except requests.exceptions.RequestException as e:
        logging.exception(f"Request failed: {e}")
    
    # Return None for graceful error handling
    return None