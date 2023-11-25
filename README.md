# Selenium Human-Like Interaction

This script uses Selenium to simulate human-like interactions with a web page. It includes actions such as tab pressing, scrolling, mouse movement, viewport changes, and interruptions. The goal is to mimic realistic user behavior on a website.

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

- Python 3.x
- Install the required packages using:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Adjust the `user_agent.json` file with a list of user agents.
2. Run the script:

    ```bash
    python selenium_human.py.py
    ```

Replace `selenium_human.py.py` with the actual name of your Python script.

## Customization

- Modify the latitude and longitude ranges in the `set_random_location` function for different geolocations.
- Adjust the parameters in the `simulate_human_behavior` function for personalized human-like interactions.

## Note

- This script is meant for educational and testing purposes only.
- Ensure compliance with the website's terms of service and legal regulations.
- Use responsibly and avoid causing disruptions or violating website policies.
