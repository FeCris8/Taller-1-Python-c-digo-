import cv2
import numpy as np
# Cargar la imagen
imagen = cv2.imread('ford.png', 1)
# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# Aplicar suavizado Gaussiano
suavizado = cv2.GaussianBlur(imagen, (5, 5), 0)
# Detectar los bordes usando Canny
bordes = cv2.Canny(suavizado, 30, 200)
# Encontrar los contornos en la imagen de bordes
contornos, _ = cv2.findContours(bordes.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Ordenar los contornos por área y mantener los más grandes
contornos = sorted(contornos, key=cv2.contourArea, reverse=True)[:10]
for cnt in contornos:
    # Aproximar el contorno
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    # Dibujar el contorno en la imagen original
    cv2.drawContours(imagen, [approx], -1, (0, 255, 0), 2)
for cnt in contornos:
    # Obtener las coordenadas del contorno
    x, y, w, h = cv2.boundingRect(cnt)
    print(f'Coordenadas: X={x}, Y={y}')
    # Dibujar el contorno en la imagen original
    cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 2)
# Mostrar la imagen con los contornos dibujados
cv2.imshow('Contornos', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

