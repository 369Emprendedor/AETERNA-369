import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Necesitaremos esta librería para ver imágenes
import os

class AeternaPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("AETERNA 369 - INTERFAZ VISUAL SOBERANA")
        self.root.geometry("900x700")
        self.root.configure(bg="#0a0a0a")

        # Título principal
        tk.Label(self.root, text="SISTEMA AETERNA 369", fg="#00ff00", bg="#0a0a0a", font=("Consolas", 24, "bold")).pack(pady=10)
        tk.Label(self.root, text="Arquitecto: YUNIERT MERINO ORO", fg="#ffffff", bg="#0a0a0a", font=("Consolas", 14)).pack()

        # --- SECCIÓN DE LA IMAGEN ---
        self.canvas = tk.Canvas(self.root, width=500, height=400, bg="#111111", highlightthickness=1, highlightbackground="#00ff00")
        self.canvas.pack(pady=20)

        try:
            # Intentamos cargar tu imagen
            ruta_imagen = os.path.join(os.path.dirname(__file__), "CUPULA_369.png")
            img = Image.open(ruta_imagen)
            img = img.resize((480, 380), Image.LANCZOS) # Ajustar tamaño al cuadro
            self.photo = ImageTk.PhotoImage(img)
            self.canvas.create_image(250, 200, image=self.photo)
            self.add_status("CÚPULA 369 CARGADA EXITOSAMENTE")
        except Exception as e:
            self.canvas.create_text(250, 200, text="IMAGEN NO ENCONTRADA\nVerifique CUPULA_369.png", fill="red", font=("Consolas", 12))
            print(f"Error cargando imagen: {e}")

        # Estado del Nodo
        self.status_label = tk.Label(self.root, text="ESTADO: NODO_001_PALMETTO_BAY LATIENDO", fg="#00ff00", bg="#0a0a0a", font=("Consolas", 12))
        self.status_label.pack(pady=10)

        # Botón de cierre
        tk.Button(self.root, text="FINALIZAR SESIÓN SOBERANA", command=self.root.destroy, bg="#00ff00", fg="black", font=("Consolas", 10, "bold")).pack(pady=20)

    def add_status(self, msg):
        print(f"[*] {msg}")

if __name__ == "__main__":
    root = tk.Tk()
    # Si te da error de 'PIL', abre una ventana negra y escribe: pip install Pillow
    try:
        app = AeternaPanel(root)
        root.mainloop()
    except Exception as e:
        print(f"Error en el sistema: {e}")
        input("Presiona Enter para ver el error...")