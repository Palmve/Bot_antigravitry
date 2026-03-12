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
        self.root.attributes("-alpha", 0.90) # 90% Translucency
        self.root.geometry("400x320")
        self.root.resizable(False, False)

        # Window Border
        self.main_frame = tk.Frame(root, bd=2, relief="solid", highlightbackground="gray", highlightthickness=1)
        self.main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.running = False
        self.ciclo = 1 

        # --- Interface ---
        tk.Label(self.main_frame, text="BOT ANTIGRAVITY v1.5", font=("Arial", 11, "bold")).pack(pady=10)
        
        # Container for labels with fixed height for stability
        self.info_container = tk.Frame(self.main_frame, height=100)
        self.info_container.pack(fill="x", pady=5)
        self.info_container.pack_propagate(False)

        self.paso_label = tk.Label(self.info_container, text="Status: Off", font=("Arial", 10, "bold"), fg="red")
        self.paso_label.pack(pady=2)

        self.detalle_label = tk.Label(self.info_container, text="Ready to start the cycle.", 
                                      font=("Arial", 9), wraplength=350, justify="center", fg="black")
        self.detalle_label.pack(pady=5, padx=10)

        self.btn_control = tk.Button(self.main_frame, text="TURN ON BOT", command=self.toggle_bot, 
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
            self.btn_control.config(text="STOP THE BOT", bg="#f44336")
            threading.Thread(target=self.hilo_logico, daemon=True).start()
        else:
            self.detener_bot("Status: Off", "Surveillance disabled by user.", "red")

    def detener_bot(self, paso, detalle, color):
        self.running = False
        self.btn_control.config(text="RESTART THE BOT", bg="#4CAF50")
        self.actualizar(paso, detalle, color)

    def buscar_seguro(self, nombre):
        """Search for the image without crashing if not found."""
        ruta = os.path.join(BASE_DIR, nombre)
        if not os.path.isfile(ruta):
            raise FileNotFoundError(f"Missing file: {nombre}")
        
        try:
            # Intentamos localizar la imagen
            return pyautogui.locateCenterOnScreen(ruta, confidence=0.8)
        except Exception:
            # Si da ImageNotFoundException o cualquier error de 'no visto', devolvemos None
            return None

    def hilo_logico(self):
        try:
            while self.running:
                self.actualizar(f"CYCLE {self.ciclo}", "Starting a new search...", "black")
                time.sleep(1)

                # --- STEP 1: SEARCH FOR BLUE RUN BUTTON ---
                self.actualizar(f"Cycle {self.ciclo} - Step 1", "Searching for Blue Button (Run)...", "blue")
                pos_run = self.buscar_seguro('run_button.png')

                if pos_run:
                    self.actualizar("ACTION!", "Run Button found! Clicking...", "green")
                    pyautogui.click(pos_run)
                    self.ciclo = 1 # Reset cycles on success
                    self.actualizar("Success", "Waiting 5s for processing...", "#2e7d32")
                    time.sleep(5) 
                    continue

                # Pause if Run is not found
                self.actualizar("Waiting", "Run not found. Waiting 3s for Expand...", "orange")
                time.sleep(3)

                # --- STEP 1.5: SEARCH FOR EXPAND BUTTON ---
                self.actualizar(f"Cycle {self.ciclo} - Step 1.5", "Searching for Expand Button...", "#8e44ad")
                pos_expand = self.buscar_seguro('Expand.png')
                if pos_expand:
                    self.actualizar("ACTION!", "Expand Button detected. Clicking...", "green")
                    pyautogui.click(pos_expand)
                    self.ciclo = 1
                    time.sleep(3)
                    continue

                # --- STEP 2: SEARCH FOR ARROW ---
                self.actualizar(f"Cycle {self.ciclo} - Step 2", "Searching for Arrow (down_arrow)...", "purple")
                pos_flecha = self.buscar_seguro('down_arrow.png')

                if pos_flecha:
                    self.actualizar("ACTION!", "Arrow detected. Scrolling down screen...", "green")
                    pyautogui.click(pos_flecha)
                    self.ciclo = 1 # Reset cycles
                    self.actualizar("Success", "Screen moved. Waiting 3s...", "#2e7d32")
                    time.sleep(3)
                    continue

                # --- STEP 2.5: SEARCH FOR ACCEPT ALL (Every 2 cycles) ---
                if self.ciclo % 2 == 0:
                    self.actualizar(f"Cycle {self.ciclo} - Step 2.5", "Searching for Accept all Button...", "#2980b9")
                    pos_accept = self.buscar_seguro('Accept_all.png')
                    if pos_accept:
                        self.actualizar("ACTION!", "Accept all Button detected. Clicking...", "green")
                        pyautogui.click(pos_accept)
                        self.ciclo = 1
                        time.sleep(3)
                        continue

                # --- STEP 3: AUTO-SCROLL LOGIC (Cycle 2 or more) ---
                if self.ciclo >= 2:
                    self.actualizar("Step 3: Auto-Scroll", "Nothing seen in 2 cycles. Forced scroll...", "#e67e22")
                    pyautogui.scroll(-600)
                    time.sleep(3)
                    self.ciclo = 1 # Reset after scroll to start over
                else:
                    self.ciclo += 1
                    self.actualizar("End of Cycle 1", "Nothing found. Increasing search level in 3s...", "gray")
                    time.sleep(3)

        except Exception as e:
            # Fatal error (e.g., missing file) stops the bot
            detalle = f"Critical Error: {type(e).__name__}\n{str(e)}"
            self.detener_bot("BOT STOPPED!", detalle, "red")
            print(traceback.format_exc())

if __name__ == "__main__":
    root = tk.Tk()
    app = BotAntigravityFinal(root)
    root.mainloop()