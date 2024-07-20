# Importar sys para manejar argumentos de línea de comandos
import sys
# Importar la función para cargar modelos entrenados desde TensorFlow y Keras
from tensorflow.keras.models import load_model
# Importar funciones de preprocesamiento y visualización de imágenes desde el script preprocess.py
from preprocess import preprocess_image, draw_asymmetry, draw_border, draw_color, draw_diameter, draw_evolution, display_image_with_title

def predict(image_path):
    # Cargar el modelo entrenado
    model = load_model('../models/abcde_model.h5')

    # Preprocesar la imagen
    image = preprocess_image(image_path)

    # Realizar la predicción
    predictions = model.predict(image)
    
    # Interpretar las predicciones
    results = {
        'Asymmetry': 'Yes' if predictions[0][0] > 0.5 else 'No',
        'Border': 'Irregular' if predictions[1][0] > 0.5 else 'Regular',
        'Color': 'Multiple' if predictions[2][0] > 0.5 else 'Single',
        'Diameter': 'More than 6mm' if predictions[3][0] > 0.5 else 'Less than 6mm',
        'Evolution': 'Yes' if predictions[4][0] > 0.5 else 'No'
    }

    # Visualizar las características ABCDE
    img_asymmetry = draw_asymmetry(image)
    display_image_with_title(img_asymmetry, f"Asymmetry: {results['Asymmetry']}")

    img_border = draw_border(image)
    display_image_with_title(img_border, f"Border: {results['Border']}")

    img_color = draw_color(image)
    display_image_with_title(img_color, f"Color: {results['Color']}")

    img_diameter = draw_diameter(image)
    display_image_with_title(img_diameter, f"Diameter: {results['Diameter']}")

    img_evolution = draw_evolution(image)
    display_image_with_title(img_evolution, f"Evolution: {results['Evolution']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python predict.py <image_path>")
    else:
        image_path = sys.argv[1]
        predict(image_path)
