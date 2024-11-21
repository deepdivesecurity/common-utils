#!/usr/bin/env python

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
from urllib3.util import Retry
import logging

# Basic logging configuration
logging.basicConfig(
    # Default logging level
    level=logging.DEBUG,
    # Format of log
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    # Log to a file in append mode
    handlers=[
        logging.FileHandler("coding_pattern_utils.log", mode="a")
    ]
)

def requests_with_retry(url: str, http_method: str = "GET", headers: dict = None, payload: dict = None, proxies: dict = None, retries: int = 3, backoff_factor: int = 1, status_forcelist: set[int]=(500,502,503,504), timeout: float=10.0) -> requests.Response: 
    """ requests_with_retry: Attempts to connect to a URL using the retry with backoff pattern in the case of a set of passed in errors

    Args:
        url (str): The URL that the user is requesting
        http_method (str, optional): The HTTP method used to perform the request (e.g. GET, PUT, POST). Defaults to GET.
        headers (dict, optional): The HTTP headers used in the request. Defaults to {}.
        payload (dict, optional): The data sent in the request. Defaults to {}.
        proxies (dict, optional): The proxy settings, if required for the request. Defaults to {}.
        retries (int, optional): The number of times to retry connecting to the URL. Defaults to 3.
        backoff_factor (int, optional): Base value of delay to use in between retry attempts. Defaults to 1.
        status_forcelist (set[int], optional): Set of HTTP error codes to force a retry on. Defaults to (500,502,503,504).
        timeout (float, optional): The timeout for the request in seconds. Defaults to 10.0 seconds.

    Returns:
        requests.Reponse: The raw Response object from the URL request; None if error encountered.
    """

    # Default to empty dictionaries if None was passed
    headers = headers or {}
    payload = payload or {}
    proxies = proxies or {}

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
        response = session.request(http_method, url, headers=headers, data=payload, proxies=proxies, timeout=timeout)
        response.raise_for_status()
        
        return response
    
    except RequestException as e:
        # Log the error with context (URL, HTTP method, etc.)
        logging.exception(f"Request failed [URL: {url}, Method: {http_method}]: {e}")
        
        # Return None for graceful error handling
        return None