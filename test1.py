from selenium import webdriver
driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("https://hub.knime.com/")
driver.find_element_by_class_name("accept-button").click()
driver.find_element_by_css_selector('#__layout > div > div.sticky-footer > header > nav > div.login > button').click()
driver.find_element_by_id("edit-name").send_keys("faizanbukhari")
driver.find_element_by_id("edit-pass").send_keys("123.Qwertyuiop")
driver.find_element_by_css_selector("#edit-submit").click()
driver.find_element_by_class_name("avatar-profile").click()
driver.find_element_by_css_selector("div[class='login'] li:nth-child(2)").click()
driver.find_element_by_css_selector("main button:nth-child(2)").click()
driver.find_element_by_xpath("//button[@title='Save']//*[name()='svg']").click()
driver.close()
print("space created")