import json
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style, Back
import time
from tqdm import tqdm
from urllib.parse import urlparse

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
    latitude = random.uniform(0.0, 60.0)
    longitude = random.uniform(30.0, 150.0)
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
    actions.extend([("scroll", random.uniform(1, 2)) for _ in range(scrolling_actions_count)])

    # Shuffle the list of actions for a random sequence
    random.shuffle(actions)

    for action, duration in actions:
        try:
            if action == "tab":
                colored_print("Simulating pressing Tab key...", Fore.YELLOW)
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
                tab_and_enter(driver)  # Call the function to simulate Tab and Enter actions
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
            colored_print(f"An error  '{action}' action: {str(e)} dont panic! continue.. ", Fore.RED)
            continue

        # Introduce a random delay between actions to simulate human-like pauses
        inter_action_delay = random.uniform(2, 5)
        time.sleep(inter_action_delay)

# Function for dynamic scrolling on the web page
def dynamic_scroll(driver):
    total_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    scroll_distance = random.randint(100, min(total_height, 500))
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")

# Function to simulate mouse movement on the web page
def move_mouse(driver):
    try:
        viewport_width = driver.execute_script("return Math.max(document.documentElement.clientWidth, window.innerWidth || 0);")
        viewport_height = driver.execute_script("return Math.max(document.documentElement.clientHeight, window.innerHeight || 0);")
        target_x = random.randint(0, viewport_width)
        target_y = random.randint(0, viewport_height)
        driver.execute_script(f"window.scrollTo({target_x}, {target_y});")
    except Exception as e:
        colored_print(f"An error occurred during 'move_mouse' action: {str(e)}", Fore.RED)

# Function to simulate changes in viewport size
def change_viewport(driver):
    new_width = random.randint(800, 1200)
    new_height = random.randint(600, 900)
    driver.set_window_size(new_width, new_height)

# Function to simulate a user-initiated interruption
def user_interruption():
    time.sleep(random.uniform(13, 30))

# Function to perform a random search and scrolling on a website
def search_and_scroll_randomly(keyword, site, max_iterations=3):
    for iteration in range(max_iterations):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        user_agent = get_random_user_agent()
        chrome_options.add_argument(f"user-agent={user_agent}")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Chrome(options=chrome_options)

        try:
            start_time = time.time()
            colored_print(f"\nIteration {iteration + 1}: Opening Google page with User-Agent: {user_agent}...", Fore.GREEN)
            set_random_location(driver)
            driver.get("https://www.google.com")
            colored_print(f"Performing search with keyword '{keyword}' and site '{site}'...", Fore.CYAN)
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys(f"{keyword} site:{site}")
            search_box.send_keys(Keys.RETURN)

            delay = random.uniform(5, 13)
            with tqdm(total=int(delay), desc="Waiting for search results", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} seconds") as pbar:
                while delay > 0:
                    time.sleep(1)
                    delay -= 1
                    pbar.update(1)

            colored_print(f"Searching for links containing text or link 'https://bikintas.online/' on iteration {iteration + 1}...", Fore.MAGENTA)

            wait = WebDriverWait(driver, 10)
            link_to_click = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'https://bikintas.online/')]")))
            colored_print("Link found!:", Fore.YELLOW)
            print(link_to_click.get_attribute("href"))

            colored_print("Clicking the corresponding link...", Fore.BLUE)
            driver.execute_script("arguments[0].click();", link_to_click)

            delay = random.uniform(3, 10)
            with tqdm(total=int(delay), desc="Waiting for the page to open", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} seconds") as pbar:
                while delay > 0:
                    time.sleep(1)
                    delay -= 1
                    pbar.update(1)

            colored_print("Page successfully opened! Simulating human-like behavior...", Fore.GREEN)
            simulate_human_behavior(driver)

            colored_print(f"Total time spent on the website: {round(time.time() - start_time, 2)} seconds", Fore.CYAN)

        except KeyboardInterrupt:
            colored_print("Stopped by the user.", Fore.RED)

        finally:
            colored_print("Closing the browser...", Back.RED)
            driver.quit()



# Function to check if a URL is within the specified website
def is_within_website(url):
    parsed_url = urlparse(url)
    return "bikintas.online" in parsed_url.netloc

# Function to close any tabs that are not within the specified website
def close_tabs_not_within_website(driver, original_tab):
    open_tabs = driver.window_handles

    for tab in open_tabs:
        if tab != original_tab:
            driver.switch_to.window(tab)
            current_url = driver.current_url

            if not is_within_website(current_url):
                driver.close()

    # Switch back to the original tab
    driver.switch_to.window(original_tab)

# Function to simulate pressing Tab key and Enter
def tab_and_enter(driver):
    tab_count = random.randint(2, 5)
    for _ in range(tab_count):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
        time.sleep(random.uniform(0.5, 1.5))  # Introduce a random delay between Tab presses

    print(f"Simulating pressing {tab_count} Tab{'s' if tab_count > 1 else ''}.")

    focused_element = driver.switch_to.active_element
    if focused_element.tag_name == "a":
        focused_element_url = focused_element.get_attribute("href")
        focused_element.send_keys(Keys.RETURN)
        print("Simulating pressing Enter on a link.")

        # Get the original tab
        original_tab = driver.current_window_handle

        # Wait for a new tab to be opened
        WebDriverWait(driver, 10).until(lambda d: len(set(d.window_handles) - {original_tab}) > 0)

        # Close any tabs that are not within the specified website
        close_tabs_not_within_website(driver, original_tab)

        # Switch back to the original tab
        driver.switch_to.window(original_tab)

        # Check if the current URL is within the original website
        current_url = driver.current_url
        if is_within_website(current_url):
            print(f"Successfully clicked on a link within the website. Current URL: {current_url}")
        else:
            print(f"Clicked on a link outside the website. Current URL: {current_url}")
            print("Unable to return to the original website. Exiting the script.")
            return
    else:
        try:
            if focused_element.tag_name == "button":
                focused_element.click()
                print("Simulating clicking on a button.")
            elif focused_element.tag_name == "input" and focused_element.get_attribute("type") == "submit":
                focused_element.click()
                print("Simulating clicking on a submit button.")
            elif focused_element.tag_name == "input" or focused_element.tag_name == "textarea":
                focused_element.send_keys(Keys.RETURN)
                print("Setting focus to an input or textarea.")
            elif focused_element.tag_name == "li" and focused_element.get_attribute("role") == "menuitem":
                focused_element.click()
                print("Simulating clicking on a menu item.")
            elif focused_element.tag_name == "div" and focused_element.get_attribute("class") == "custom-element":
                perform_custom_action(focused_element)
                print("Performing custom action on a specific type of element.")
            else:
                pass
        except Exception as e:
            colored_print(f"Unable to handle non-link element: {str(e)}", Fore.RED)

# Run the search_and_scroll_randomly function with specified keyword, site, and max iterations
if __name__ == "__main__":
    search_and_scroll_randomly("konveksi tas", "https://bikintas.online", max_iterations=1)
