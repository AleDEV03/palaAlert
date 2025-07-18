## Aplicación de alerta con Tkinter que muestra una imagen giratoria y reproduce música en bucle.
## Al presionar el botón, se detiene la música y se cierra la ventana.
## Requiere las bibliotecas tkinter, PIL (Pillow) y pygame instaladas.
## Requiere que los archivos "pala.png" y "cancion.mp3" estén en el mismo directorio del script.

import tkinter as tk
from PIL import Image, ImageTk
import pygame

class PalaAlertApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pala Alert")
        self.root.geometry("240x200")
        self.root.resizable(False, False)

        pygame.mixer.init()
        try:
            pygame.mixer.music.load("cancion.mp3")
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Error cargando música: {e}")

        self.image = Image.open("pala.png").resize((150, 150))
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(root, image=self.photo)
        self.label.pack()

        self.angle = 0
        self.rotate_image()

        button = tk.Button(root, text="Agarrá la pala gil!!", command=self.cerrar_alerta)
        button.pack()

    def rotate_image(self):
        rotated = self.image.rotate(self.angle)
        new_photo = ImageTk.PhotoImage(rotated)
        self.label.config(image=new_photo)
        self.label.image = new_photo
        self.angle = (self.angle + 10) % 360
        self.root.after(100, self.rotate_image)

    def cerrar_alerta(self):
        pygame.mixer.music.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PalaAlertApp(root)
    root.mainloop()

