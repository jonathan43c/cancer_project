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
│   └── data.csv            # Archivo CSV con las rutas y 
├── scripts/               # Scripts de Python
│   ├── modelo A.py        # Entrenamiento del modelo a
│   ├── modelo B.py        # Entrenamiento del modelo b
│   ├── modelo C.py        # Entrenamiento del modelo c
│   └── modelo D.py        # Entrenamiento del modelo d
├── requirements.txt        # Lista de dependencias
└── README.md               # Documentación del proyecto
