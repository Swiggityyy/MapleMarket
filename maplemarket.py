from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import numpy as np
from pandas import DataFrame as df

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
inventory_sheet = pd.read_excel("/home/swiggityyy/Desktop/mtest.xlsx", sheet_name="Sheet1")
df = pd.DataFrame(inventory_sheet)

driver.get("https://owlrepo.com/items")
wait = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(("xpath", "/html/body/main/div/div[1]/div[1]/div[2]/div[1]/div[2]/input"))

)
item_name = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div[2]/div[1]/div[2]/input")

# Single Item Search Test



item_name.send_keys(df.iloc[df.Name,0])
item_name.send_keys(Keys.RETURN)
price = driver.find_element(By.XPATH, "./html/body/main/div[1]/div[2]/div/div/div[7]")
df.iloc[7,1] = price.text
print(df.Name,price)

# Writes to an excel
df.to_excel("/home/swiggityyy/Desktop/mtest.xlsx", sheet_name = "Sheet1", index=False)

# Test Loop. didn't want to run this on a live site.
""" # while item_name != "nan":
#     x = 0
#     y = 0
#     item_name = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div[2]/div[1]/div[2]/input")
#     item_name.send_keys(df.iloc[x,y])

#     df.iloc.y = df.iloc.y + 1
 """
