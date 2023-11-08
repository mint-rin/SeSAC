from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option('detach', True) #브라우저 바로꺼짐 방지

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://n.news.naver.com/mnews/article/277/0005337370?sid=105')
driver.implicitly_wait(10)

# 기사 제목
# find_element(하나만), find_elements(전부 다)
# print(driver.find_element(By.CSS_SELECTOR, "h2#title_area").text)
# time.sleep(5)

for li in driver.find_elements(By.CSS_SELECTOR, "u_likeit_list"):
    print(li.find_element(By.CSS_SELECTOR, ".u_likeit_list_name").text)
    print(li.find_element(By.CSS_SELECTOR, ".u_likeit_list_count").text)

driver.find_element(By.CSS_SELECTOR, ".Nicon_search").click()
driver.find_element(By.CSS_SELECTOR, ".u_it._search_input").send_keys("지드래곤")
driver.find_element(By.CSS_SELECTOR, ".u_hssbt_us._total_search_btn").click()