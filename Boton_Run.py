import pyautogui
import tkinter as tk
import threading
import time
import os
import traceback

# Configurar ruta base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BotAntigravityFinal:
    def __init__(self, root):
        self.root = root
        self.root.title("Bot Antigravity - Control")
        self.root.attributes("-topmost", True)
        self.root.geometry("400x320")
        self.root.resizable(False, False)

        self.running = False
        self.ciclo = 1 

        # --- Interfaz ---
        tk.Label(root, text="BOT ANTIGRAVITY v1.5", font=("Arial", 11, "bold")).pack(pady=10)
        
        self.paso_label = tk.Label(root, text="Estado: Apagado", font=("Arial", 10, "bold"), fg="red")
        self.paso_label.pack(pady=5)

        self.detalle_label = tk.Label(root, text="Listo para iniciar el ciclo.", 
                                      font=("Arial", 9), wraplength=350, justify="center", fg="black")
        self.detalle_label.pack(pady=15, padx=10)

        self.btn_control = tk.Button(root, text="ENCENDER BOT", command=self.toggle_bot, 
                                     bg="#4CAF50", fg="white", width=25, height=2, font=("Arial", 10, "bold"))
        self.btn_control.pack(pady=10)

    def actualizar(self, paso, detalle, color="black"):
        self.paso_label.config(text=paso, fg=color)
        self.detalle_label.config(text=detalle)
        self.root.update()

    def toggle_bot(self):
        if not self.running:
            self.running = True
            self.ciclo = 1
            self.btn_control.config(text="DETENER BOT", bg="#f44336")
            threading.Thread(target=self.hilo_logico, daemon=True).start()
        else:
            self.detener_bot("Estado: Apagado", "Vigilancia desactivada por usuario.", "red")

    def detener_bot(self, paso, detalle, color):
        self.running = False
        self.btn_control.config(text="REINICIAR BOT", bg="#4CAF50")
        self.actualizar(paso, detalle, color)

    def buscar_seguro(self, nombre):
        """Busca la imagen sin dejar que el programa se cierre si no la ve."""
        ruta = os.path.join(BASE_DIR, nombre)
        if not os.path.isfile(ruta):
            # Este SI es un error real: el archivo no existe
            raise FileNotFoundError(f"Falta el archivo: {nombre}")
        
        try:
            # Intentamos localizar la imagen
            return pyautogui.locateCenterOnScreen(ruta, confidence=0.8)
        except Exception:
            # Si da ImageNotFoundException o cualquier error de 'no visto', devolvemos None
            return None

    def hilo_logico(self):
        try:
            while self.running:
                self.actualizar(f"CICLO {self.ciclo}", "Iniciando nueva búsqueda...", "black")
                time.sleep(1)

                # --- PASO 1: BUSCAR BOTÓN AZUL ---
                self.actualizar(f"Ciclo {self.ciclo} - Paso 1", "Buscando botón Azul (Run)...", "blue")
                pos_run = self.buscar_seguro('run_button.png')

                if pos_run:
                    self.actualizar("¡ACCIÓN!", "¡Botón Run encontrado! Pulsando...", "green")
                    pyautogui.click(pos_run)
                    self.ciclo = 1 # Reiniciamos ciclos al tener éxito
                    self.actualizar("Éxito", "Esperando 5s para que la app procese...", "#2e7d32")
                    time.sleep(5) 
                    continue

                # Si no hay Run, pausa de 3 segundos
                self.actualizar("Espera", "Run no visto. Pausando 3s para buscar Expand...", "orange")
                time.sleep(3)

                # --- PASO 1.5: BUSCAR BOTÓN EXPAND ---
                self.actualizar(f"Ciclo {self.ciclo} - Paso 1.5", "Buscando botón Expand...", "#8e44ad")
                pos_expand = self.buscar_seguro('Expand.png')
                if pos_expand:
                    self.actualizar("¡ACCIÓN!", "Botón Expand detectado. Pulsando...", "green")
                    pyautogui.click(pos_expand)
                    self.ciclo = 1
                    time.sleep(3)
                    continue

                # --- PASO 2: BUSCAR FLECHA ---
                self.actualizar(f"Ciclo {self.ciclo} - Paso 2", "Buscando Flecha (down_arrow)...", "purple")
                pos_flecha = self.buscar_seguro('down_arrow.png')

                if pos_flecha:
                    self.actualizar("¡ACCIÓN!", "Flecha detectada. Bajando pantalla...", "green")
                    pyautogui.click(pos_flecha)
                    self.ciclo = 1 # Reiniciamos ciclos
                    self.actualizar("Éxito", "Pantalla desplazada. Esperando 3s...", "#2e7d32")
                    time.sleep(3)
                    continue

                # --- PASO 2.5: BUSCAR ACCEPT ALL (Solo cada 2 ciclos) ---
                if self.ciclo % 2 == 0:
                    self.actualizar(f"Ciclo {self.ciclo} - Paso 2.5", "Buscando botón Accept all...", "#2980b9")
                    pos_accept = self.buscar_seguro('Accept_all.png')
                    if pos_accept:
                        self.actualizar("¡ACCIÓN!", "Botón Accept all detectado. Pulsando...", "green")
                        pyautogui.click(pos_accept)
                        self.ciclo = 1
                        time.sleep(3)
                        continue

                # --- PASO 3: LÓGICA DE SCROLL (Solo en Ciclo 2 o más) ---
                if self.ciclo >= 2:
                    self.actualizar("Paso 3: Auto-Scroll", "Nada visto en 2 ciclos. Bajando pantalla solo...", "#e67e22")
                    pyautogui.scroll(-600)
                    time.sleep(3)
                    self.ciclo = 1 # Reiniciamos tras el scroll para volver a empezar
                else:
                    self.ciclo += 1
                    self.actualizar("Fin de Ciclo 1", "No encontré nada. Subiendo nivel de búsqueda en 3s...", "gray")
                    time.sleep(3)

        except Exception as e:
            # Si ocurre un error REAL (ej. falta un archivo), el bot se detiene
            detalle = f"Error crítico: {type(e).__name__}\n{str(e)}"
            self.detener_bot("¡BOT DETENIDO!", detalle, "red")
            print(traceback.format_exc())

if __name__ == "__main__":
    root = tk.Tk()
    app = BotAntigravityFinal(root)
    root.mainloop()