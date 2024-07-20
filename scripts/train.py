# Importar pandas para la manipulación de datos tabulares
import pandas as pd
# Importar numpy para la manipulación de arreglos
import numpy as np
# Importar capas y modelos desde TensorFlow y Keras para construir el modelo de deep learning
from tensorflow.keras import layers, models
# Importar la función de división de datos de scikit-learn para crear conjuntos de entrenamiento y validación
from sklearn.model_selection import train_test_split
# Importar la función de preprocesamiento de imágenes desde el script preprocess.py
from preprocess import preprocess_image

# Cargar el CSV con las rutas de las imágenes y sus etiquetas
data = pd.read_csv('../data/data.csv')

# Preprocesar todas las imágenes y preparar las etiquetas
images = np.array([preprocess_image(img_path) for img_path in data['image_path']])
labels = data['label'].apply(lambda x: 1 if x == 'melanoma' else 0).values

# Definir el modelo de Deep Learning
def create_model():
    input_shape = (150, 150, 1)  # Imagen en escala de grises
    
    inputs = layers.Input(shape=input_shape)
    
    # Primera capa convolucional con 32 filtros y tamaño de kernel de 3x3
    x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)
    # Primera capa de pooling para reducir el tamaño de las dimensiones
    x = layers.MaxPooling2D((2, 2))(x)
    
    # Segunda capa convolucional con 64 filtros y tamaño de kernel de 3x3
    x = layers.Conv2D(64, (3, 3), activation='relu')(x)
    # Segunda capa de pooling
    x = layers.MaxPooling2D((2, 2))(x)
    
    # Tercera capa convolucional con 128 filtros y tamaño de kernel de 3x3
    x = layers.Conv2D(128, (3, 3), activation='relu')(x)
    # Tercera capa de pooling
    x = layers.MaxPooling2D((2, 2))(x)
    
    # Aplanar la salida para la capa completamente conectada
    x = layers.Flatten()(x)
    
    # Capas de salida para características ABCDE
    asymmetry_output = layers.Dense(1, activation='sigmoid', name='asymmetry_output')(x)
    border_output = layers.Dense(1, activation='sigmoid', name='border_output')(x)
    color_output = layers.Dense(1, activation='sigmoid', name='color_output')(x)
    diameter_output = layers.Dense(1, activation='sigmoid', name='diameter_output')(x)
    evolution_output = layers.Dense(1, activation='sigmoid', name='evolution_output')(x)
    
    # Definir el modelo
    model = models.Model(inputs=inputs, outputs=[asymmetry_output, border_output, color_output, diameter_output, evolution_output])
    
    # Compilar el modelo con optimizador Adam y función de pérdida binaria
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

# Crear el modelo
model = create_model()

# Dividir los datos en entrenamiento y validación
train_images, val_images, train_labels, val_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

# Entrenar el modelo
history = model.fit(train_images, 
                    {'asymmetry_output': train_labels,
                     'border_output': train_labels,
                     'color_output': train_labels,
                     'diameter_output': train_labels,
                     'evolution_output': train_labels},
                    epochs=30, 
                    validation_data=(val_images, 
                                     {'asymmetry_output': val_labels,
                                      'border_output': val_labels,
                                      'color_output': val_labels,
                                      'diameter_output': val_labels,
                                      'evolution_output': val_labels}))

# Guardar el modelo entrenado
model.save('../models/abcde_model.h5')
