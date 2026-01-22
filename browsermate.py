print(r"""
██████╗ ██████╗  ██████╗ ██╗    ██╗███████╗███████╗██████╗ ███╗   ███╗ █████╗ ████████╗███████╗
██╔══██╗██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔════╝██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║   ██║██║ █╗ ██║███████╗█████╗  ██████╔╝██╔████╔██║███████║   ██║   █████╗  
██╔══██╗██╔══██╗██║   ██║██║███╗██║╚════██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║   ██║   ██╔══╝  
██████╔╝██║  ██║╚██████╔╝╚███╔███╔╝███████║███████╗██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
""")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(" BROWSERMATE v1.0 | Navigation rapide depuis Terminal")
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
        print("Impossible de trouver la zone de chat. Vérifie que tu es connecté.")

    return driver

UserInput = input("BROWSERMATE ➜ Plateforme à ouvrir : ")
B = UserInput.lower()

driver = None  

if B == "youtube":
    Chercher = input("BROWSERMATE ➜ Que veux-tu rechercher ? : ")
    driver = Youtube(Chercher)

elif B == "wikipedia":
    Chercher = input("BROWSERMATE ➜ Que veux-tu rechercher ? : ")
    driver = Wikipedia(Chercher)

elif B == "chatgpt":
    Chercher = input("BROWSERMATE ➜ Que veux-tu demander à ChatGPT ? : ")
    driver = ChatGPT(Chercher)


else:
    print("Plateforme non disponible actuellement.")
    print("Cette plateforme sera ajoutée bientôt.")


input("Appuie sur Entrée pour fermer le navigateur...")

if driver is not None:
    driver.quit()
