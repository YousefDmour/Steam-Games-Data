from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

website = 'https://steamdb.info/stats/gameratings/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# chrome_options.add_argument('--headless')
# chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(website)
time.sleep(5)

# button = driver.find_element(By.XPATH, '//div[@class="calendar-buttons"]/a[4]')
# button.click()
# time.sleep(5)

dropdown = driver.find_element(By.XPATH, '//select[@class="dt-input"]')
select = Select(dropdown)
select.select_by_visible_text("All")
time.sleep(5)

games_rank = driver.find_elements(By.XPATH, '//tr/td[1][@class="dt-type-numeric"]')
games_rank = [game_rank.text.strip('.') for game_rank in games_rank]

games_names = driver.find_elements(By.XPATH, '//tr/td[3]/div/a')
games_names = [game_name.text for game_name in games_names]

discount_percentge = driver.find_elements(By.XPATH, '//tr/td[4]')
discount_percentge = [discount.text if discount.text.strip() else "N/A"for discount in discount_percentge]

games_price = driver.find_elements(By.XPATH, '//tr/td[5]')
games_price = [price.text for price in games_price]

games_rating = driver.find_elements(By.XPATH, '//tr/td[6]')
games_rating = [rate.text for rate in games_rating]

release_date = driver.find_elements(By.XPATH, '//tr/td[7]')
release_date = [release.text for release in release_date]

followers = driver.find_elements(By.XPATH, '//tr/td[8]')
followers = [follow.text for follow in followers]

reviews = driver.find_elements(By.XPATH, '//tr/td[9]')
reviews = [review.text for review in reviews]

peak = driver.find_elements(By.XPATH, '//tr/td[10]')
peak = [p.text for p in peak]

top_rated_games = {'Rank': games_rank, 'Name': games_names,'Discount Percentage': discount_percentge,"Game Price": games_price, 'Game Rate':games_rating, "Release Date":release_date,
                     'Followes':followers, 'Reviews':reviews, 'Peak':peak}

# print(len(top_rated_games['Rank']))
# print(len(top_rated_games['Name']))
# print(len(top_rated_games['Discount Percentage']))
# print(len(top_rated_games['Game Price']))
# print(len(top_rated_games['Game Rate']))
# print(len(top_rated_games['Release Date']))
# print(len(top_rated_games['Followes']))
# print(len(top_rated_games['Reviews']))
# print(len(top_rated_games['Peak']))



df = pd.DataFrame(top_rated_games)

df.to_csv('data/Hot_Releases_2026_9_14.csv')