# Selenium Human-Like Interaction

This script uses Selenium to simulate human-like interactions with a web page. It includes actions such as tab pressing, scrolling, mouse movement, viewport changes, and interruptions. The goal is to mimic realistic user behavior on a website.


## Overview
This Python script utilizes the Selenium WebDriver to simulate human-like behavior during web browsing. It performs a random search on Google, clicks on a search result link related to a specified website, and simulates various human interactions such as tabbing, scrolling, mouse movement, viewport changes, and interruptions.

## Features

### 1. User Agent Rotation
- Randomly selects a user agent from a provided list to simulate different browsers and devices.

### 2. Geolocation Spoofing
- Sets a random geolocation within the specified latitude and longitude range, emulating users from different locations.

### 3. Dynamic Search and Click
- Performs a Google search with a given keyword and site, then clicks on a randomly selected link containing specific text or URL.

### 4. Human-Like Behavior Simulation
- Simulates human-like behavior with a sequence of actions:
  - Pressing the Tab key
  - Scrolling the page
  - Simulating mouse movement
  - Changing the viewport size
  - Simulating user-initiated interruptions

### 5. Random Delays
- Introduces random delays between actions to mimic natural pauses in user behavior.

### 6. Headless Mode
- Runs the browser in headless mode, allowing the script to execute without displaying the browser window.

## Prerequisites
- Python 3
- Chrome WebDriver
- Selenium (`pip install selenium`)
- Colorama (`pip install colorama`)
- tqdm (`pip install tqdm`)

## Usage
1. Adjust the `user_agent.json` file with a list of user agents.
2. Run the script:

    ```bash
    python selenium_human.py
    ```


## Configuration
- **user_agent.json**: Contains a list of user agents used for random selection during each iteration. For updated user agents, you can find them [here](https://www.useragents.me/).
- **selenium_human.py**: Main Python script file.
- **requirements.txt**: Lists the required Python packages.

## Script Structure
- **get_random_user_agent**: Function to select a random user-agent from the provided list.
- **colored_print**: Function for printing colored console output.
- **set_random_location**: Function to set a random geolocation for the browser.
- **simulate_human_behavior**: Function to simulate various human-like behaviors.
- **dynamic_scroll**: Function for scrolling the page by a random distance.
- **move_mouse**: Function to simulate mouse movement within the viewport.
- **change_viewport**: Function to emulate changes in viewport size.
- **user_interruption**: Function to simulate user-initiated interruptions.
- **search_and_scroll_randomly**: Main function to perform a random search and scrolling on Google.

## Acknowledgments
- [Selenium](https://www.selenium.dev/)
- [Colorama](https://pypi.org/project/colorama/)
- [tqdm](https://pypi.org/project/tqdm/)

## Customization

- Modify the latitude and longitude ranges in the `set_random_location` function for different geolocations.
- Adjust the parameters in the `simulate_human_behavior` function for personalized human-like interactions.

## Note

- This script is meant for educational and testing purposes only.
- Ensure compliance with the website's terms of service and legal regulations.
- Use responsibly and avoid causing disruptions or violating website policies.

