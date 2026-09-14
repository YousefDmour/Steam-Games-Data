from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

website = 'https://steamdb.info/stats/trendingfollowers/'

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

dropdown = driver.find_element(By.XPATH, '//select[@class="dt-input"]')
select = Select(dropdown)
select.select_by_visible_text("All")
time.sleep(10)

games_rank = driver.find_elements(By.XPATH, '//tr/td[1]')
games_rank = [game_rank.text.strip('.') for game_rank in games_rank[:-7]]

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

last_7d_gain = driver.find_elements(By.XPATH, '//tr/td[9]')
last_7d_gain = [last_7d.text for last_7d in last_7d_gain]

Trend_games = {'Rank': games_rank, 'Name': games_names,'Discount Percentage': discount_percentge,"Game Price": games_price, 'Game Rate':games_rating, "Release Date":release_date,
                     'Followes':followers, '7d Gain':last_7d_gain}

# print(len(Trend_games['Rank']))
# print(len(Trend_games['Name']))
# print(len(Trend_games['Discount Percentage']))
# print(len(Trend_games['Game Price']))
# print(len(Trend_games['Game Rate']))
# print(len(Trend_games['Release Date']))
# print(len(Trend_games['Followes']))
# print(len(Trend_games['7d Gain']))



df = pd.DataFrame(Trend_games)

df.to_csv('data/Trend_games_2026_9_14.csv')