from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Define credentials
url = "https://ecs-qa.kloudship.com"
username = "kloudship.qa.automation@mailinator.com"
password = "Password1"

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the window
driver.maximize_window()

# Step 01: Login to the application
driver.get(url)
driver.find_element_by_id("inputEmail").send_keys(username)
driver.find_element_by_id("inputPassword").send_keys(password)
driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()

# Step 02: Navigate to Package Types
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Package Types')]"))).click()

# Step 03: Click on Add Manually button
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add Manually')]"))).click()

# Step 04: Add a package with random dimensions
name = "FirstName_LastName"
dimensions = random.randint(1, 20)
driver.find_element_by_name("name").send_keys(name)
driver.find_element_by_name("dimensions").send_keys(dimensions)

# Click on Save button
driver.find_element_by_xpath("//button[contains(text(),'Save')]").click()

# Wait for the success message
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Package added successfully')]")))

# Step 05: Logout the application
driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()

# Step 06: Login again to verify the created package
driver.find_element_by_id("inputEmail").send_keys(username)
driver.find_element_by_id("inputPassword").send_keys(password)
driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()

# Step 07: Navigate to Package Types to verify the newly created package
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Package Types')]"))).click()

# Verify if the newly created package is present
package_present = driver.find_elements_by_xpath(f"//td[contains(text(),'{name}')]")
assert len(package_present) > 0, "Newly created package not found"

# Test Case 01 execution completed successfully

# Step 08: Delete the newly added package
package_present[0].find_element_by_xpath("..//td[last()]/button[contains(text(),'Delete')]").click()

# Confirm deletion
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Yes')]"))).click()

# Wait for success message
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Package deleted successfully')]")))

# Step 09: Logout the application
driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()

# Step 10: Login again to verify package deletion
driver.find_element_by_id("inputEmail").send_keys(username)
driver.find_element_by_id("inputPassword").send_keys(password)
driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()

# Step 11: Navigate to Package Types to verify the package deletion
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Package Types')]"))).click()

# Verify if the package is not present
package_not_present = driver.find_elements_by_xpath(f"//td[contains(text(),'{name}')]")
assert len(package_not_present) == 0, "Newly created package still found"

# Test Case 02 execution completed successfully

# Close the browser
driver.quit()
