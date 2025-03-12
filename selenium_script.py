from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time 
import argparse

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver


def cafe24_register(driver, id, pw, name, phone, mail):
    target_url = "https://suraktantan.cafe24.com/member/agreement.html"
    driver.get(target_url)
    time.sleep(8)

    driver.find_element(By.CSS_SELECTOR, ".agreeAll .ec-base-chk input").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div.ec-base-button.gBottom button").click()
    time.sleep(1)

    driver.find_element(By.ID, "member_id").send_keys(id)
    time.sleep(0.5)
    driver.find_element(By.ID, "passwd").send_keys(pw)
    time.sleep(0.5)
    driver.find_element(By.ID, "user_passwd_confirm").send_keys(pw)
    time.sleep(0.5)
    driver.find_element(By.ID, "name").send_keys(name)
    time.sleep(0.5)
    
    phone_parts = phone.split('-')
    driver.find_element(By.ID, "mobile2").send_keys(phone_parts[1])
    time.sleep(0.5)
    driver.find_element(By.ID, "mobile3").send_keys(phone_parts[2])
    time.sleep(0.5)

    driver.find_element(By.ID, "email1").send_keys(mail)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "div.ec-base-button.gBottom a:nth-child(2)").click()
    time.sleep(3)

def main():
    parser = argparse.ArgumentParser(description="Run Selenium script with arguments")
    parser.add_argument("--id", required=True, help="ID")
    parser.add_argument("--pw", required=True, help="Password")
    parser.add_argument("--name", required=True, help="Name")
    parser.add_argument("--phone", required=True, help="PhoneNumber")
    parser.add_argument("--mail", required=True, help="Email")
    args = parser.parse_args()

    driver = create_driver()
    try:
        test_id = args.id
        test_pw = args.pw
        test_name = args.name
        test_phone = args.phone
        test_mail = args.mail

        cafe24_register(driver, test_id, test_pw, test_name, test_phone, test_mail)
    except Exception as e:
        print(f"❌ Error: {str(e)}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
