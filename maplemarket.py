from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
import pandas as pd
import numpy as np
from pandas import DataFrame as df
from tabulate import tabulate
import time

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
inventory_sheet = pd.read_excel("/home/swiggityyy/Desktop/mtest.xlsx", sheet_name="Sheet1")
df = pd.DataFrame(inventory_sheet)

driver.get("https://owlrepo.com/items")
waitsearch = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(("xpath", "/html/body/main/div/div[1]/div[1]/div[2]/div[1]/div[2]/input"))

)

item_name = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div[2]/div[1]/div[2]/input")

x = 0
while x <38:
    item_name.clear()
    item_name.send_keys(df.iloc[x,0])
    time.sleep(1)
    item_name.send_keys(Keys.RETURN)
    try:
        price = driver.find_element(By.XPATH, "./html/body/main/div[1]/div[2]/div/div/div[7]")
        last_sold = driver.find_element(By.XPATH, "./html/body/main/div/div[2]/div/div[1]/div[1]")
        df.iloc[x,1] = price.text
        df.iloc[x,2] = last_sold.text
    except:
        df.iloc[x,1] = '0'
        df.iloc[x,2] = '0'
        print("no result. item price set to 0.")

    x = x + 1

print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

# Writes to an excel
df.to_excel("/home/swiggityyy/Desktop/mtest.xlsx", sheet_name = "Sheet1", index=False)