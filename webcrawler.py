# part of an fst machine translator

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://blogs.transparent.com/french/french-numbers-1-100/')
table = browser.find_element(
    By.XPATH, "/html/body/main/div[2]/div[2]/div[1]/div[1]/table")
rows = table.find_elements(By.TAG_NAME, "tr")
outfile = open('numbers.txt', 'w')
for row in rows:
    num = row.find_elements(By.TAG_NAME, "td")[0]  # the number
    name = row.find_elements(By.TAG_NAME, "td")[1]  # its name in french
    # we gon re this bitch up later
    outfile.write(num.text + '\t' + name.text + '\n')
