from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# #access to data from external files
# def returnText(text):
#     return text

# Ścieżka do chromedriver (upewnij się, że masz poprawnie zainstalowany chromedriver)
chrome_driver_path = 'F:\Programy\Instalatory\chromedriver-win64\chromedriver.exe'  # Zmień na lokalizację swojego chromedriver

# Opcje przeglądarki (opcjonalne)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Uruchamia przeglądarkę w trybie bezgłowym (bez GUI)

# Inicjalizacja drivera
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Otwieramy stronę
url = "https://osdr.nasa.gov/bio/repo/data/studies/OSD-379"
driver.get(url)

# Czekamy na pełne załadowanie strony
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Pełne przewinięcie strony, aby załadować ukryte elementy
scroll_pause_time = 2  # Czas pauzy między przewinięciami

# Pobieramy wysokość strony
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Przewijamy stronę w dół
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Czekamy, aż strona się załaduje
    time.sleep(scroll_pause_time)

    # Ponownie sprawdzamy wysokość strony
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # Koniec przewijania
    last_height = new_height

# Pobieramy tekst tylko z wybranych tagów: <h1>, <h2>, <h3>, <p>, <label>
tags = ['h1', 'h2', 'h3', 'p', 'label']
all_text = ""

# Iterujemy przez wybrane tagi i zbieramy tekst
for tag in tags:
    elements = driver.find_elements(By.TAG_NAME, tag)
    for element in elements:
        all_text += element.text + "\n"

# Usuwanie duplikatów w tekście (dzielimy tekst na słowa, usuwamy duplikaty, łączymy)
text_list = all_text.split()
unique_text = ' '.join(dict.fromkeys(text_list))

# Wypisujemy cały unikalny tekst
print(unique_text)

# Zamykanie przeglądarki
driver.quit()

