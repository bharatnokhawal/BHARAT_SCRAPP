# import all the libraries like csv , selenium , BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#define a funtion for login purpose 
#define a funtion for login purpose 
def login():
    driver.get("https://www.linkedin.com/login")
    time.sleep(1)
    email = "bharatnokhawal201920@gmail.com"  #  LinkedIn email
    password = "Bharat@456"  #   password

    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button").click()
    time.sleep(3)
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(5)
#search using first name and last name like fo search box and search Bharat kumawat and enter
def search_user(first_name, last_name):
    driver.get("https://www.linkedin.com/search/results/people/")
    time.sleep(2)

    search_bar = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
    search_bar.send_keys(first_name + " " + last_name)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)
#go to all search name one by one store in to the csv file (first 10)
def scrape_profile_data():
    profiles = []
    try:
        profile_cards = driver.find_elements(By.CLASS_NAME,'search-results-container')
        for profile_card in profile_cards[:10]:  # Loop through the first 10 profiles
            profile = {}
            try:
                name_element = profile_card.find_element(By.XPATH, ".//a[contains(@class, 'app-aware-link')]")
                name = name_element.text.strip()

                headline_element = profile_card.find_element(By.CLASS_NAME, "entity-result_primary-subtitle t-14 t-black t-normal")
                headline = headline_element.text.strip()

                location_element = profile_card.find_element(By.CLASS_NAME, "entity-result_secondary-subtitle t-14 t-normal")
                location = location_element.text.strip()

                profile['Name'] = name
                profile['Headline'] = headline
                profile['Location'] = location

                profiles.append(profile)
            except Exception as e:
                print(f"Error scraping profile: {e}")
        
        # Store data in CSV
        df = pd.DataFrame(profiles)
        df.to_csv('linkedin_profiles.csv', index=False)
        print("Data scraped and stored in linkedin_profiles.csv")
    except Exception as e:
        print(f"Error scraping profiles: {e}")


if __name__ == "__main__":
    login()
    first_name = "Bharat"  # the first name of the user you want to search
    last_name = "kumawat"  # the last name of the user you want to search
    search_user(first_name, last_name)
    scrape_profile_data()
    print("Data scraped and stored in linkedin_profiles.csv")
