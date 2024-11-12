# coding-patterns
This repo contains common helper coding patterns including but not limited to retry with backoff.

---

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

---

## Project Description

retry_requests_with_backoff_pattern.py: Attempts to connect to a URL using the retry with backoff pattern in the case of a set of passed in errors.

---

## Installation

### Requirements

#### retry_requests_with_backoff_pattern.py
- Python 3.7 or higher
- requests
- urllib3

1. Clone the repository:
   ```bash
   git clone https://github.com/deepdivesecurity/coding-patterns.git
   cd coding-patterns
   ```

2. Create the virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the following in your terminal to start
    ```bash
    python retry_requests_with_backoff_pattern.py
    ```

## Features
- TBD