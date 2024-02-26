# #5. Dibuje el nombre de cada uno de los integrantes del grupo en un plot en 2D, teniendo en cuenta líneas rectas y/o curvas.
# from PIL import Image, ImageDraw, ImageFont

# # Crear una imagen vacía de color blanco
# img = Image.new("RGB", (500, 100), "white")

# # Crear un objeto para dibujar en la imagen
# draw = ImageDraw.Draw(img)

# # Cargar la fuente de texto
# font = ImageFont.truetype("arial.ttf", 72)

# # Escribir el nombre en la imagen con la fuente y el color elegidos
# draw.text((10, 10), "Cristian", font=font, fill="blue")

# # Mostrar la imagen
# img.show()

# # Guardar la imagen como un archivo PNG
# img.save("nombre.png")


# """modificar el tamaño y la posición del texto con los argumentos (10, 10) y 72 del método text.
# También puedes cambiar la fuente y el color con los argumentos font y fill. Si quieres usar otra fuente,
#  solo tienes que indicar el nombre del archivo .ttf que quieras usar."""



import matplotlib.pyplot as plt
# letra c
cx1 = [0, 1, 2]  
cy1 = [0, 0, 0]
cx2 = [0, 0, 0]
cy2 = [0, 1, 2]
cx3 = [2, 0, 0]
cy3 = [2, 2, 2] 
#letra r
rx1 = [3, 3, 3]    
ry1 = [0, 1, 1.75]
rx2 = [3, 4, 5]
ry2 = [1.75, 1.75, 1.55]
#letra i
ix1 = [6, 6, 6]  
iy1 = [0, 1, 1.75]
#letra s
sx1 = [7, 7, 7]  
sy1 = [1, 1, 1.75]
sx2 = [7, 8, 9]
sy2 = [1, 1, 1]
sx3 = [7, 8, 9]
sy3 = [1.75, 1.75, 1.75]
sx4 = [9, 9, 9]
sy4 = [1, 0.5, 0]
sx5 = [7, 8, 9]
sy5 = [0, 0, 0]
#letrat
tx1 = [10, 10, 10] 
ty1 = [0, 1, 1.75]
tx2 = [9.5, 10, 11] 
ty2 = [1, 1, 1]
tx3 = [10, 11, 11] 
ty3 = [0, 0, 0]
#letrai2
i2x1 = [12, 12, 12]  
i2y1 = [0, 1, 1.75]
#letraa
ax1 = [13, 13, 13]
ay1 = [0.15, 1, 1.75]
ax2 = [13, 14, 15]
ay2 = [1.75, 1.75, 1.75]
ax3 = [13, 14, 15]
ay3 = [0.15, 0.15, 0.15]
ax4 = [15, 15, 15]
ay4 = [0, 1, 1.75]
#letran
nx1 = [16, 16, 16]
ny1 = [0, 1, 1.75]
nx2 = [16, 17, 18]
ny2 = [1.75, 1.75, 1.75]
nx3 = [18, 18, 18]
ny3 = [0, 1, 2]


plt.plot(cx1,cy1,cx2,cy2,cx3,cy3,rx1,ry1,rx2,ry2,
         ix1,iy1,sx1,sy1,sx2,sy2,sx3,sy3,sx4,sy4,sx5,sy5,
         tx1,ty1,tx2,ty2,tx3,ty3,i2x1,i2y1,
         ax1,ay1,ax2,ay2,ax3,ay3,ax4,ay4,
         nx1,ny1,nx2,ny2,nx3,ny3)
plt.show()