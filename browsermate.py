print(r"""
██████╗ ██████╗  ██████╗ ██╗    ██╗███████╗███████╗██████╗ ███╗   ███╗ █████╗ ████████╗███████╗
██╔══██╗██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔════╝██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║   ██║██║ █╗ ██║███████╗█████╗  ██████╔╝██╔████╔██║███████║   ██║   █████╗  
██╔══██╗██╔══██╗██║   ██║██║███╗██║╚════██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║   ██║   ██╔══╝  
██████╔╝██║  ██║╚██████╔╝╚███╔███╔╝███████║███████╗██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
""")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("BROWSERMATE v1.0 | Quick navigation from the terminal")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def Youtube(A):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    
    time.sleep(2)
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys(A)
    search_box.send_keys(Keys.ENTER)

    return driver  

def Wikipedia(A):
    driver = webdriver.Chrome()
    driver.get("https://fr.wikipedia.org/")
    
    time.sleep(2)
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(A)
    search_box.send_keys(Keys.ENTER)

    return driver  

def ChatGPT(A):
    driver = webdriver.Chrome()
    driver.get("https://chat.openai.com/")
    time.sleep(5)

    try:
        # zone de saisie (souvent un textarea)
        input_box = driver.find_element(By.TAG_NAME, "textarea")
        input_box.send_keys(A)
        input_box.send_keys(Keys.ENTER)
    except:
        print("Unable to find the chat area. Please check that you are logged in.")

    return driver

UserInput = input("BROWSERMATE ➜ Platform to open : ")
B = UserInput.lower()

driver = None  

if B == "youtube":
    Chercher = input("BROWSERMATE ➜ What would you like to search for ? : ")
    driver = Youtube(Chercher)

elif B == "wikipedia":
    Chercher = input("BROWSERMATE ➜ What would you like to search for ? : ")
    driver = Wikipedia(Chercher)

elif B == "chatgpt":
    Chercher = input("BROWSERMATE ➜ What would you like to ask ChatGPT ? : ")
    driver = ChatGPT(Chercher)


else:
    print("Platform currently unavailable.")
    print("This platform will be added soon.")


input("Press Enter to close the browser...")

if driver is not None:
    driver.quit()
