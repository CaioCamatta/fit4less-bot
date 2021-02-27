import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# LOAD ENVIRONMENT
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = os.getenv("FIT4LESS_LOGIN_URL")
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
TIME = os.getenv("TIME")
BOOKING_DATE = str(datetime.now().date() +
                   timedelta(days=int(os.getenv("BOOKING_DAYS_FROM_NOW"))))

# CONFIGURE ENVIRONMENT
if not (EMAIL):
    print('Enter your email: ', end="")
    EMAIL = input()

if not (PASSWORD):
    print('Enter your password: ', end="")
    PASSWORD = input()

if not (BOOKING_DATE):
    print('How many days from now would you like to book? (0=today, 1=tomorrow, 2=two days from now): ', end="")
    BOOKING_DATE = input()

if not (TIME):
    print('What time would you like to book? e.g. "10:00 AM": ', end="")
    TIME = input()

# START DRIVER
chrome_options = Options()
# Add "headless" to hide actual screen
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)
driver.get(LOGIN_URL)

try:
    # LOGIN
    email_input = driver.find_element_by_id("emailaddress")
    password_input = driver.find_element_by_id("password")
    driver.implicitly_wait(5)
    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)
    driver.implicitly_wait(5)
    password_input.send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    print("Logged In!")

    # BOOK
    driver.find_element_by_id("btn_date_select").click()
    driver.implicitly_wait(3)
    driver.find_element_by_id("date_" + BOOKING_DATE).click()
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(3)

    # Use second `available-slots`. First one is for times already booked.
    available_slots = driver.find_elements_by_class_name("available-slots")[1].find_elements_by_class_name(
        "time-slot-box")

    for slot in available_slots:
        if (TIME in str(slot.text)):
            print("Found time slot ", TIME)
            # Get the parent of the parent of the "time-slot-box"
            slot.find_element_by_xpath('..').click()
            driver.implicitly_wait(5)
            driver.find_element_by_id("dialog_book_yes").click()
            driver.implicitly_wait(5)
            print("Done! Your time was booked.")
            break
    else:
        print(
            "Could not find a time slot. Please make sure you entered your info correctly.")

except Exception as e:
    print(e)
finally:
    driver.quit()
