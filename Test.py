from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://minesweeper.online/ko/game/2437260880')
element = driver.find_element_by_id('cell_27_1')
element.click()