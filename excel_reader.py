import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')  
driver = webdriver.Chrome(options=chrome_options) 
driver.maximize_window()


def read_excel_file(file_name):

    df = pd.read_excel(file_name, engine='openpyxl')
    column_name = 'Links'

    for index, row in df.iterrows():
        link = row[column_name]
        if link.startswith('http'): 
            print(f"Opening link: {link}")
            driver.get(link)
            time.sleep(120)  # waiting for 2 minutes for each link
    driver.close()


read_excel_file('Urls.xlsx')
