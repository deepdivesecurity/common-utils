#!/usr/bin/env python

import os
import requests
import json
#from coding_pattern_utils import requests_with_retry
import logging

# Basic logging configuration
logging.basicConfig(
    # Default logging level
    level=logging.DEBUG,
    # Format of log
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    # Log to a file in append mode
    handlers=[
        logging.FileHandler("prisma_cloud_utils.log", mode="a")
    ]
)

def authn_to_prisma_cloud() -> str:
    
    # Set authn info
    user = os.getenv("user")
    password = os.getenv("password")
    prismaID = os.getenv("prismaID")

    # Set URL to login URL
    url = "https://api.ca.prismacloud.io/login"

    # Set payload with authn info
    payload = f"""
    {{
    "username": "{user}",
    "password": "{password}",
    "prismaID": "{prismaID}"
    }}
    """

    # Set headers for request
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Accept": "application/json; charset=UTF-8"
    }

    # TODO Change this to retry_requests_with_backoff_pattern
    try: 
        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()
        token = response_data["token"]
        return token
    except: 
        return None

def extend_authn_token(token: str) -> bool: 
    """_summary_

    Args:
        token (str): _description_

    Raises:
        TypeError: _description_

    Returns:
        bool: _description_
    """
    success = False

    # Validate token
    # TODO: Make this validation more comprehensive by checking actual string contents to make sure they adhere to token requirements
    if not isinstance(token, str):
        # Log the error
        logging.error(f"Invalid token type: {type(token)}. Expected: str.")

        # Raise the TypeError
        raise TypeError("Authn token must be a str")

    # Extend session
    url = "https://api.ca.prismacloud.io/auth_token/extend"

    payload = {}
    headers = {
        "Accept": "application/json",
        "x-redlock-auth": token
    }

    # TODO Change this to retry_requests_with_backoff_pattern
    try: 
        response = requests.request("GET", url, headers=headers, data=payload)
        return True
    except: 
        return False