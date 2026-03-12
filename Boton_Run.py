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
        self.root.title("Bot Antigravity - Contrôle")
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.90) # Translucidité à 90%
        self.root.geometry("400x320")
        self.root.resizable(False, False)

        # Bordure de la fenêtre
        self.main_frame = tk.Frame(root, bd=2, relief="solid", highlightbackground="gray", highlightthickness=1)
        self.main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.running = False
        self.ciclo = 1 

        # --- Interface ---
        tk.Label(self.main_frame, text="BOT ANTIGRAVITY v1.5", font=("Arial", 11, "bold")).pack(pady=10)
        
        # Conteneur pour étiquettes avec hauteur fixe pour la stabilité
        self.info_container = tk.Frame(self.main_frame, height=100)
        self.info_container.pack(fill="x", pady=5)
        self.info_container.pack_propagate(False)

        self.paso_label = tk.Label(self.info_container, text="État: Éteint", font=("Arial", 10, "bold"), fg="red")
        self.paso_label.pack(pady=2)

        self.detalle_label = tk.Label(self.info_container, text="Prêt à démarrer le cycle.", 
                                      font=("Arial", 9), wraplength=350, justify="center", fg="black")
        self.detalle_label.pack(pady=5, padx=10)

        self.btn_control = tk.Button(self.main_frame, text="ALLUMER LE BOT", command=self.toggle_bot, 
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
            self.btn_control.config(text="ARRÊTER LE BOT", bg="#f44336")
            threading.Thread(target=self.hilo_logico, daemon=True).start()
        else:
            self.detener_bot("État: Éteint", "Surveillance désactivée par l'utilisateur.", "red")

    def detener_bot(self, paso, detalle, color):
        self.running = False
        self.btn_control.config(text="REDÉMARRER LE BOT", bg="#4CAF50")
        self.actualizar(paso, detalle, color)

    def buscar_seguro(self, nombre):
        """Recherche l'image sans planter si elle n'est pas trouvée."""
        ruta = os.path.join(BASE_DIR, nombre)
        if not os.path.isfile(ruta):
            raise FileNotFoundError(f"Fichier manquant: {nombre}")
        
        try:
            # Intentamos localizar la imagen
            return pyautogui.locateCenterOnScreen(ruta, confidence=0.8)
        except Exception:
            # Si da ImageNotFoundException o cualquier error de 'no visto', devolvemos None
            return None

    def hilo_logico(self):
        try:
            while self.running:
                self.actualizar(f"CYCLE {self.ciclo}", "Démarrage d'une nouvelle recherche...", "black")
                time.sleep(1)

                # --- PASO 1: BUSCAR BOTÓN AZUL ---
                self.actualizar(f"Cycle {self.ciclo} - Étape 1", "Recherche du bouton Bleu (Run)...", "blue")
                pos_run = self.buscar_seguro('run_button.png')

                if pos_run:
                    self.actualizar("¡ACTION!", "Bouton Run trouvé ! Clic en cours...", "green")
                    pyautogui.click(pos_run)
                    self.ciclo = 1 # Reiniciamos ciclos al tener éxito
                    self.actualizar("Succès", "Attente de 5s pour le traitement...", "#2e7d32")
                    time.sleep(5) 
                    continue

                # Si no hay Run, pausa de 3 segundos
                self.actualizar("Attente", "Run non trouvé. Attente de 3s pour Expand...", "orange")
                time.sleep(3)

                # --- PASO 1.5: BUSCAR BOTÓN EXPAND ---
                self.actualizar(f"Cycle {self.ciclo} - Étape 1.5", "Recherche du bouton Expand...", "#8e44ad")
                pos_expand = self.buscar_seguro('Expand.png')
                if pos_expand:
                    self.actualizar("¡ACTION!", "Bouton Expand détecté. Clic en cours...", "green")
                    pyautogui.click(pos_expand)
                    self.ciclo = 1
                    time.sleep(3)
                    continue

                # --- PASO 2: BUSCAR FLECHA ---
                self.actualizar(f"Cycle {self.ciclo} - Étape 2", "Recherche de la flèche (down_arrow)...", "purple")
                pos_flecha = self.buscar_seguro('down_arrow.png')

                if pos_flecha:
                    self.actualizar("¡ACTION!", "Flèche détectée. Défilement de l'écran...", "green")
                    pyautogui.click(pos_flecha)
                    self.ciclo = 1 # Reiniciamos ciclos
                    self.actualizar("Succès", "Écran déplacé. Attente de 3s...", "#2e7d32")
                    time.sleep(3)
                    continue

                # --- PASO 2.5: BUSCAR ACCEPT ALL (Solo cada 2 ciclos) ---
                if self.ciclo % 2 == 0:
                    self.actualizar(f"Cycle {self.ciclo} - Étape 2.5", "Recherche du bouton Accept all...", "#2980b9")
                    pos_accept = self.buscar_seguro('Accept_all.png')
                    if pos_accept:
                        self.actualizar("¡ACTION!", "Bouton Accept all détecté. Clic en cours...", "green")
                        pyautogui.click(pos_accept)
                        self.ciclo = 1
                        time.sleep(3)
                        continue

                # --- PASO 3: LÓGICA DE SCROLL (Solo en Ciclo 2 o más) ---
                if self.ciclo >= 2:
                    self.actualizar("Étape 3: Auto-Scroll", "Rien vu en 2 cycles. Défilement forcé...", "#e67e22")
                    pyautogui.scroll(-600)
                    time.sleep(3)
                    self.ciclo = 1 # Reiniciamos tras el scroll para volver a empezar
                else:
                    self.ciclo += 1
                    self.actualizar("Fin du Cycle 1", "Rien trouvé. Augmentation du niveau de recherche dans 3s...", "gray")
                    time.sleep(3)

        except Exception as e:
            # Si ocurre un error REAL (ej. falta un archivo), el bot se detiene
            detalle = f"Erreur critique: {type(e).__name__}\n{str(e)}"
            self.detener_bot("¡BOT ARRÊTÉ!", detalle, "red")
            print(traceback.format_exc())

if __name__ == "__main__":
    root = tk.Tk()
    app = BotAntigravityFinal(root)
    root.mainloop()