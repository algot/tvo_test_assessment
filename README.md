# TVO Test Assessment

## Install

### Prerequisites

* Python 3.12  is installed
* git is installed

# Installation
* Run following commands:
  * `git clone https://github.com/algot/tvo_test_assessment`
  * `cd tvo_test_assessment`
  * `python3 -m venv .venv`
  * `.venv\Script\activate.bat` (Windows) or `source .venv/bin/activate` (MacOS/Linux) 
  * `pip install -r requirements.txt`
  * `playwright install`
  * `cp .env.example .env`

## Usage
Run the following command:

  `pytest`

It runs the test scripts in default configuration (Chromium, headless, 2 threads).

To run tests in headed mode add `--headed` argument to the run command:

`pytest --headed`

To run tests in Firefox add `--browser firefox` argument to the run command:

`pytest --browser firefox`