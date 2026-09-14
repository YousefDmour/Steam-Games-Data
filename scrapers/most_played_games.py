from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

website = 'https://steamdb.info/charts/'

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
games_rank = [game_rank.text.strip('.') for game_rank in games_rank]

games_names = driver.find_elements(By.XPATH, '//tr/td/a[@class="b"]')
games_names = [game_name.text for game_name in games_names]

current_players = driver.find_elements(By.XPATH, '//tr/td[4]')
current_players = [current.text for current in current_players]

peak_24h = driver.find_elements(By.XPATH, '//tr/td[5]')
peak_24h = [peak.text for peak in peak_24h]

all_time_peak = driver.find_elements(By.XPATH, '//tr/td[6]')
all_time_peak = [time_peak.text for time_peak in all_time_peak]

most_played_games = {'Rank': games_rank, 'Name': games_names,'Current Players': current_players,"24h Peak": peak_24h, 'All Time Peak':all_time_peak}

df = pd.DataFrame(most_played_games)

df.to_csv('data/most_played_games_2026_9_14.csv')