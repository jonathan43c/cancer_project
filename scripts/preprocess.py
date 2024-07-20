# Importar la biblioteca NumPy para la manipulación de arreglos
import numpy as np
# Importar OpenCV para el procesamiento de imágenes
import cv2
# Importar Pillow para la manipulación de imágenes
from PIL import Image
# Importar Matplotlib para la visualización de imágenes
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    # Cargar la imagen desde el archivo usando Pillow
    img = Image.open(image_path)
    # Redimensionar la imagen a 150x150 píxeles
    img = img.resize((150, 150))
    # Convertir la imagen a un arreglo numpy y normalizar los valores de los píxeles a un rango de 0 a 1
    img_array = np.array(img) / 255.0
    # Expandir las dimensiones del arreglo para que sea compatible con el modelo
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def draw_asymmetry(image_array):
    # Convertir la imagen preprocesada de regreso a una imagen visualizable
    img = image_array[0] * 255
    img = img.astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Obtener las dimensiones de la imagen
    height, width, _ = img.shape
    # Dibujar una línea vertical en el medio de la imagen para evaluar la asimetría
    cv2.line(img, (width // 2, 0), (width // 2, height), (255, 0, 0), 2)
    return img

def draw_border(image_array):
    # Convertir la imagen preprocesada de regreso a una imagen visualizable
    img = image_array[0] * 255
    img = img.astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Convertir la imagen a escala de grises y detectar bordes
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 30, 200)
    # Resaltar los bordes en la imagen
    img[edges != 0] = [255, 0, 0]
    return img

def draw_color(image_array):
    # Convertir la imagen preprocesada de regreso a una imagen visualizable
    img = image_array[0] * 255
    img = img.astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def draw_diameter(image_array):
    # Convertir la imagen preprocesada de regreso a una imagen visualizable
    img = image_array[0] * 255
    img = img.astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Obtener las dimensiones de la imagen y calcular el centro y el radio
    height, width, _ = img.shape
    center = (width // 2, height // 2)
    radius = min(width, height) // 4
    # Dibujar un círculo en el centro de la imagen para evaluar el diámetro
    cv2.circle(img, center, radius, (255, 0, 0), 2)
    return img

def draw_evolution(image_array):
    # Convertir la imagen preprocesada de regreso a una imagen visualizable
    img = image_array[0] * 255
    img = img.astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def display_image_with_title(img, title):
    # Mostrar la imagen con un título usando Matplotlib
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    plt.show()
