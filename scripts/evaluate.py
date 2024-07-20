# Importar pandas para la manipulación de datos tabulares
import pandas as pd
# Importar numpy para la manipulación de arreglos
import numpy as np
# Importar la función para cargar modelos entrenados desde TensorFlow y Keras
from tensorflow.keras.models import load_model
# Importar la función de reporte de clasificación desde scikit-learn para evaluar el rendimiento del modelo
from sklearn.metrics import classification_report
# Importar la función de preprocesamiento de imágenes desde el script preprocess.py
from preprocess import preprocess_image

# Cargar el modelo entrenado
model = load_model('../models/melanoma_model.h5')

# Cargar los datos de validación
data = pd.read_csv('../data/data.csv')
validation_data = data[data['split'] == 'validation']  # Asegúrate de tener una columna 'split' en tu CSV
images = np.array([preprocess_image(img_path) for img_path in validation_data['image_path']])
labels = validation_data['label'].apply(lambda x: 1 if x == 'melanoma' else 0).values

# Realizar predicciones en el conjunto de validación
predictions = model.predict(images)
predicted_labels = (predictions > 0.5).astype(int)

# Generar un reporte de clasificación
report = classification_report(labels, predicted_labels, target_names=['no_melanoma', 'melanoma'])
print(report)
