# OpenCV-FaceRecognition

# Dispositivo de seguridad con reconocimiento facial y detección de arma (OpenCV + MediaPipe)

## Introducción
Ecuador atraviesa una problemática sostenida de inseguridad, lo que ha incrementado la necesidad de sistemas de vigilancia accesibles para instituciones y entornos cerrados. Este proyecto implementa un prototipo de bajo costo capaz de **detectar rostros**, **registrar evidencia (capturas)** y **detectar un arma tipo pistola** en tiempo real a partir de una cámara, con el objetivo de apoyar la **prevención** y la **recolección de evidencia** para análisis posterior.

La solución se implementa en **Python**, usando **MediaPipe** para detección facial y **OpenCV** con un clasificador tipo **Haar Cascade** (archivo `pistoladetect.xml`) para detección de arma.

---

## Metodología aplicada

### 1. Herramientas y tecnologías
- **Lenguaje:** Python
- **Visión por computador:** OpenCV (`cv2`)
- **Detección facial:** MediaPipe (`mp.solutions.face_detection`)
- **Utilidades:** `imutils` (redimensionamiento), `datetime` (timestamp)
- **Modelo arma:** Haar Cascade (`pistoladetect.xml`)

### 2. Flujo del sistema (pipeline)
1. Captura de video en tiempo real desde cámara (`cv2.VideoCapture`).
2. Preprocesamiento del frame (resize, flip, conversiones RGB/GRAY).
3. Detección de rostro con MediaPipe:
   - Se obtiene bounding box del rostro.
   - Se recorta el rostro, se alinea/tamaño fijo (300x300).
   - Se agrega timestamp a la evidencia visual.
4. Detección de arma con Haar Cascade (`pistoladetect.xml`):
   - Se detecta en escala de grises (`detectMultiScale`).
   - Se dibuja bounding box y se muestra un recorte del objeto detectado.
5. Registro de evidencia:
   - Cada ~1 segundo se guarda una imagen del rostro en `Rostros detectados/rostro_#.jpg`.

![Arquitectura del sistema](docs/img/arquitectura_bravo.png)

---

## Resultados

### Resultados funcionales observables
- **Detección facial en tiempo real:** el sistema identifica un rostro y dibuja la región detectada.
- **Evidencia del rostro:** se genera un recorte `aligned_face` con timestamp y se guarda automáticamente en disco.
- **Detección de arma (pistola):** cuando el clasificador encuentra un patrón compatible, se dibuja la región detectada y se muestra el recorte `arma_detectada`.

### Evidencias (capturas recomendadas para el informe)
Incluye capturas reales ejecutando el programa:
1. Ventana principal `BRAVO` con bbox de rostro y arma.
2. Ventana `aligned_face` (rostro recortado con fecha/hora).
3. Ventana `arma_detectada` (recorte del objeto).
4. Carpeta `Rostros detectados/` mostrando varios archivos guardados.

![Ejemplo de evidencias](docs/img/guardadas.png)

---

## Requisitos
- Python 3.9+ (recomendado)
- OpenCV
- MediaPipe
- imutils

Instalación:
```bash
pip install opencv-python mediapipe imutils
pip install opencv-python
