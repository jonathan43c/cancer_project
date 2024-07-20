# Importar Flask para crear la API
from flask import Flask, request, jsonify
# Importar la función para cargar modelos entrenados desde TensorFlow y Keras
from tensorflow.keras.models import load_model
# Importar funciones de preprocesamiento y visualización de imágenes desde el script preprocess.py
from preprocess import preprocess_image, draw_asymmetry, draw_border, draw_color, draw_diameter, draw_evolution
# Importar os para manejo de rutas y archivos
import os
# Importar cv2 para guardar imágenes
import cv2

app = Flask(__name__)

# Cargar el modelo entrenado
model = load_model('models/abcde_model.h5')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Recibir la imagen desde el cliente
    file = request.files['image']
    file_path = f'./uploads/{file.filename}'
    file.save(file_path)
    
    # Preprocesar la imagen
    image = preprocess_image(file_path)
    
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

    # Visualizar y guardar las características ABCDE
    img_asymmetry = draw_asymmetry(image)
    img_asymmetry_path = os.path.join('uploads', 'asymmetry.png')
    cv2.imwrite(img_asymmetry_path, img_asymmetry)

    img_border = draw_border(image)
    img_border_path = os.path.join('uploads', 'border.png')
    cv2.imwrite(img_border_path, img_border)

    img_color = draw_color(image)
    img_color_path = os.path.join('uploads', 'color.png')
    cv2.imwrite(img_color_path, img_color)

    img_diameter = draw_diameter(image)
    img_diameter_path = os.path.join('uploads', 'diameter.png')
    cv2.imwrite(img_diameter_path, img_diameter)

    img_evolution = draw_evolution(image)
    img_evolution_path = os.path.join('uploads', 'evolution.png')
    cv2.imwrite(img_evolution_path, img_evolution)

    response = {
        'Results': results,
        'Images': {
            'Asymmetry': img_asymmetry_path,
            'Border': img_border_path,
            'Color': img_color_path,
            'Diameter': img_diameter_path,
            'Evolution': img_evolution_path
        }
    }
    
    return jsonify(response)

if __name__ == '__main__':
    # Crear el directorio de subidas si no existe
    os.makedirs('./uploads', exist_ok=True)
    app.run(debug=True)
