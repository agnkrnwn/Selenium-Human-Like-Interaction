import json
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import time
from colorama import Fore, Style, Back
from tqdm import tqdm

# Function to get a random user agent from a JSON file
def get_random_user_agent():
    with open('user_agent.json', 'r') as file:
        user_agents_data = json.load(file)

    user_agents = [entry['ua'] for entry in user_agents_data]
    return random.choice(user_agents)

# Function to print colored messages
def colored_print(message, color=Fore.WHITE):
    print(f"{color}{message}{Style.RESET_ALL}")

# Function to set a random geolocation for the browser
def set_random_location(driver):
    # Rough estimate of latitude and longitude ranges for Asia
    latitude = random.uniform(0.0, 60.0)  
    longitude = random.uniform(30.0, 150.0)

    # indonesian region
    # latitude = random.uniform(-11.0, 6.0)
    # longitude = random.uniform(94.0, 141.0)

    #entire world
    #latitude = random.uniform(-90.0, 90.0)
    #longitude = random.uniform(-180.0, 180.0)

    colored_print(f"Setting random location: Latitude {latitude}, Longitude {longitude}", Fore.MAGENTA)

    location_script = f"navigator.geolocation.getCurrentPosition = function(callback) {{ callback({{'coords': {{'latitude': {latitude}, 'longitude': {longitude}}}}}); }};"
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": location_script})

# Function to simulate various human-like behaviors on the web page
def simulate_human_behavior(driver):
    actions = [
        ("tab", random.uniform(3, 5)),
        ("scroll", random.uniform(3, 5)),
        ("move_mouse", random.uniform(1, 3)),
        ("change_viewport", random.uniform(3, 5)),
        ("interruption", random.uniform(5, 10)),
    ]

    # Add Tab actions between 5 and 10 times
    tab_actions_count = random.randint(5, 10)
    actions.extend([("tab", random.uniform(1, 2)) for _ in range(tab_actions_count)])

    # Add scrolling actions with varying durations and dynamic scroll distances
    scrolling_actions_count = random.randint(5, 10)
    actions.extend([("scroll", random.uniform(2, 5)) for _ in range(scrolling_actions_count)])

    # Shuffle the list of actions for a random sequence
    random.shuffle(actions)

    for action, duration in actions:
        try:
            if action == "tab":
                colored_print("Simulating pressing Tab key...", Fore.YELLOW)
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
            elif action == "scroll":
                colored_print("Simulating scrolling...", Fore.YELLOW)
                dynamic_scroll(driver)
            elif action == "move_mouse":
                colored_print("Simulating mouse movement...", Fore.YELLOW)
                move_mouse(driver)
            elif action == "change_viewport":
                colored_print("Simulating viewport change...", Fore.YELLOW)
                change_viewport(driver)
            elif action == "interruption":
                colored_print("Simulating user-initiated interruption...", Fore.YELLOW)
                user_interruption()

            time.sleep(duration)

        except Exception as e:
            colored_print(f"An error occurred during '{action}' action: {str(e)}", Fore.RED)
            continue

        # Introduce a random delay between actions to simulate human-like pauses
        inter_action_delay = random.uniform(2, 5)
        time.sleep(inter_action_delay)

# Function for dynamic scrolling on the web page
def dynamic_scroll(driver):
    # Get the total height of the page content
    total_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

    # Calculate a random scroll distance based on the total height
    scroll_distance = random.randint(100, min(total_height, 500))

    # Use JavaScript to scroll by the calculated distance
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")

# Function to simulate mouse movement on the web page
def move_mouse(driver):
    try:
        # Get the size of the visible area of the page
        viewport_width = driver.execute_script("return Math.max(document.documentElement.clientWidth, window.innerWidth || 0);")
        viewport_height = driver.execute_script("return Math.max(document.documentElement.clientHeight, window.innerHeight || 0);")

        # Calculate a random position within the visible area
        target_x = random.randint(0, viewport_width)
        target_y = random.randint(0, viewport_height)

        # Use JavaScript to move the mouse to the calculated position
        driver.execute_script(f"window.scrollTo({target_x}, {target_y});")

    except Exception as e:
        colored_print(f"An error occurred during 'move_mouse' action: {str(e)}", Fore.RED)

# Function to simulate changes in viewport size
def change_viewport(driver):
    # Emulate viewport change by resizing the browser window
    new_width = random.randint(800, 1200)
    new_height = random.randint(600, 900)
    driver.set_window_size(new_width, new_height)

# Function to simulate a user-initiated interruption
def user_interruption():
    # Emulate a user-initiated interruption by pausing for a while
    time.sleep(random.uniform(13, 60))

# Function to perform a random search and scrolling on a website
def search_and_scroll_randomly(keyword, site, max_iterations=3):
    for iteration in range(max_iterations):
        # Set up Chrome options for headless browsing and random user-agent
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        user_agent = get_random_user_agent()
        chrome_options.add_argument(f"user-agent={user_agent}")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

        # Initialize a new Chrome WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        try:
            # Record the start time for measuring the total time spent on the website
            start_time = time.time()

            # Print a message indicating the start of the iteration
            colored_print(f"\nIteration {iteration + 1}: Opening Google page with User-Agent: {user_agent}...", Fore.GREEN)

            # Set a random geolocation for the browser
            set_random_location(driver)
            # Open the Google homepage
            driver.get("https://www.google.com")

            # Perform a Google search using the specified keyword and site
            colored_print(f"Performing search with keyword '{keyword}' and site '{site}'...", Fore.CYAN)
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys(f"{keyword} site:{site}")
            search_box.send_keys(Keys.RETURN)

            # Wait for a random duration to simulate a user viewing search results
            delay = random.uniform(5, 13)
            with tqdm(total=int(delay), desc="Waiting for search results", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} seconds") as pbar:
                while delay > 0:
                    time.sleep(1)
                    delay -= 1
                    pbar.update(1)

            # Search for links containing the specified text or link 'https://bikintas.online/'
            colored_print(f"Searching for links containing text or link 'https://bikintas.online/' on iteration {iteration + 1}...", Fore.MAGENTA)

            # Use WebDriverWait to wait for a clickable link with the specified XPath
            wait = WebDriverWait(driver, 10)
            link_to_click = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'https://bikintas.online/')]")))

            # Print the URL of the found link
            colored_print("Link found!:", Fore.YELLOW)
            print(link_to_click.get_attribute("href"))

            # Click the found link using JavaScript to simulate a user click
            colored_print("Clicking the corresponding link...", Fore.BLUE)
            driver.execute_script("arguments[0].click();", link_to_click)

            # Wait for a random duration to simulate the time taken for the page to open
            delay = random.uniform(3, 10)
            with tqdm(total=int(delay), desc="Waiting for the page to open", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} seconds") as pbar:
                while delay > 0:
                    time.sleep(1)
                    delay -= 1
                    pbar.update(1)

            # Print a message indicating the start of human-like behavior simulation
            colored_print("Page successfully opened! Simulating human-like behavior...", Fore.GREEN)

            # Simulate various human-like behaviors on the web page
            simulate_human_behavior(driver)

            # Print the total time spent on the website during the iteration
            colored_print(f"Total time spent on the website: {round(time.time() - start_time, 2)} seconds", Fore.CYAN)

        except KeyboardInterrupt:
            # Handle keyboard interrupt by printing a message
            colored_print("Stopped by the user.", Fore.RED)

        finally:
            # Print a message indicating the browser closure
            colored_print("Closing the browser...", Back.RED)
            # Quit the WebDriver to close the browser
            driver.quit()

# Run the search_and_scroll_randomly function with specified keyword, site, and max iterations
if __name__ == "__main__":
    search_and_scroll_randomly("konveksi tas", "https://bikintas.online", max_iterations=1)