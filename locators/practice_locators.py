from selenium.webdriver.common.by import By


home_menu_xpath = (By.XPATH, "//li[@id='menu-item-43']/a[text()='Home']")
practice_menu_xpath = (By.XPATH, "//li[@id='menu-item-20']/a[text()='Practice']")
test_login_page_link_xpath = (By.XPATH, "//a[text()='Test Login Page']")

username_xpath = (By.XPATH, "//input[@id='username']")
password_xpath = (By.XPATH, "//input[@id='password']")
submit_button_xpath = (By.XPATH, "//button[@id='submit']")

login_success_heading_xpath = (By.XPATH, "//h1[text()='Logged In Successfully']")
logout_button_xpath = (By.XPATH, "//a[text()='Log out']")
