 #Importar las funciones necesarias
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import io
from PIL import Image

# Definir la función para descargar imágenes
def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("Imagen descargada con éxito")
    except Exception as e:
        print('Error al descargar la imagen:', e)



        from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys

# Configuración de Selenium
driver_path = "C:/chromedriver-win64/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
url_pagina = 'https://dermnetnz.org/'

# Obtener el contenido de la página web con Selenium
driver.get(url_pagina)

# Esperar a que se cargue la página completamente
wait = WebDriverWait(driver, 10)

# Hacer clic en el botón "AGREE" de la ventana emergente de privacidad

agree_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class=" css-usek55"]')))
agree_button.click()

# Localizar el campo de búsqueda y enviar la consulta
box_search = wait.until(EC.presence_of_element_located((By.ID, 'site-search')))
box_search.clear()
# box_search.send_keys("melanoma")
box_search.send_keys('superficial spreading melanoma')
# box_search.send_keys('nodular melanoma')
# box_search.send_keys('lentigo maligna melanoma')
# box_search.send_keys('acral lentiginous melanoma')
# box_search.send_keys('amelanotic melanoma')

box_search.send_keys(Keys.ENTER)

# Recopilar enlaces de múltiples páginas de resultados
unique_links = {}
paso = True
while paso:
    # Esperar a que se carguen los resultados de la búsqueda
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "gs-title")))

    # Obtener el HTML de la página después de la búsqueda
    html = driver.page_source

    # Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Encontrar todos los elementos <a> que contienen enlaces y tienen la clase "gs-title"
    links = soup.find_all("a", class_="gs-title", href=True)

    # Agregar las URLs únicas al diccionario
    for link in links:
        href = link["href"]
        if href not in unique_links:
            unique_links[href] = True

    # Buscar y hacer clic en el siguiente elemento del paginador
    try:
        current_page_element = driver.find_element(By.XPATH, '//div[@class="gsc-cursor-page gsc-cursor-current-page"]')
        current_page = int(current_page_element.text)
        next_page_element = driver.find_element(By.XPATH, f'//div[@class="gsc-cursor-page" and text()="{current_page + 1}"]')
        next_page_element.click()
        
        # Esperar un tiempo para que la página cargue completamente
        time.sleep(5)
    except:
        print("Ya tenemos todas las páginas. Terminó el proceso.")
        paso = False

# Imprimir las URLs únicas encontradas
for link in unique_links:
    print(link)

# Cerrar el navegador
driver.quit()


# PASO 2
lista_imagenes = []

for url in unique_links:
    # Realizar la solicitud GET a la URL
    response = requests.get(url)

    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrar la sección con la clase "imageLinkBlock"
    image_section = soup.find("div", class_="gallery__slides")

    # Verificar si la sección existe antes de continuar
    if image_section:
        # Encontrar todas las etiquetas <img> dentro de la sección
        img_tags = image_section.find_all("img")
        
        # Recorrer todas las etiquetas <img> y extraer la URL
        for img_tag in img_tags:
            img_url = img_tag.get("src")
            print(f'Imagen encontrada: https://dermnetnz.org/{img_url}')
            lista_imagenes.append(f'https://dermnetnz.org/{img_url}')
    else:
        print(f"No se encontró ninguna sección con la clase 'gallery__slides' en {url}") 

        # PASO 3
carpeta_destino = "C:/Users/User/Desktop/Proyecto cancer/webscraping/melanoma/"
for index, url in enumerate(lista_imagenes, start=510):
    nombre_archivo = f"imagen_{index}.jpg"
    download_image(carpeta_destino, url, nombre_archivo) 