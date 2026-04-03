from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uk.wikipedia.org/")

title = driver.title
print(title)
print()

sections = driver.find_elements(By.TAG_NAME, "h2")

print("=== СЕКЦІЇ ===")
for sec in sections:
    print("-", sec.text)
print()

print("=== ЦІКАВИНКИ ===")
do_you_know = driver.find_element(By.ID, "do-you-know")
facts = do_you_know.find_elements(By.TAG_NAME, "li")
for li in facts:
    print(li.text)

driver.quit()