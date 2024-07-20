# Detección de Melanoma y No Melanoma

Este proyecto utiliza técnicas de Deep Learning para la detección de melanoma y no melanoma en imágenes de la piel. El modelo se entrena utilizando un conjunto de datos de imágenes y se despliega a través de una API Flask para la predicción.

## Estructura del Proyecto

```plaintext
PROYECTO CANCER/
├── myenv/                  # Entorno virtual
├── data/
│   ├── train/              # Datos de entrenamiento
│   │   ├── melanoma/
│   │   ├── no_melanoma/
│   ├── validation/         # Datos de validación
│   │   ├── melanoma/
│   │   ├── no_melanoma/
│   └── data.csv            # Archivo CSV con las rutas y etiquetas
├── models/                 # Guardar modelos entrenados
│   ├── melanoma_model.h5
├── notebooks/              # Notebooks para experimentación y análisis
│   ├── EDA.ipynb
│   ├── training.ipynb
├── scripts/                # Scripts de Python
│   ├── preprocess.py       # Preprocesamiento de imágenes
│   ├── train.py            # Entrenamiento del modelo
│   ├── evaluate.py         # Evaluación del modelo
│   └── predict.py          # Predicciones con el modelo
├── uploads/                # Carpeta para guardar las imágenes subidas
├── app.py                  # API con Flask
├── requirements.txt        # Lista de dependencias
└── README.md               # Documentación del proyecto
