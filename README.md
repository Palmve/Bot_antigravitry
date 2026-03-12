# 🤖 Monitor de Autogestión Pro (Bot Antigravity)

Este bot es un sistema de automatización basado en reconocimiento visual. Está diseñado para monitorear la pantalla y reaccionar ante la aparición de botones específicos o realizar desplazamientos automáticos si no detecta actividad.

## 🚀 Requisitos previos

Para que el bot funcione correctamente, necesitas tener instalado:
- **Python 3.10 o superior** (Se recomienda marcar la opción "Add Python to PATH" durante la instalación).

## 🛠️ Instalación rápida

1.  **Descarga el proyecto** en una carpeta de tu preferencia.
2.  **Ejecuta el lanzador**: Haz doble clic en el archivo `INICIAR_MOLTBOT.bat`.
    -   La primera vez, el sistema creará automáticamente un entorno virtual (`.venv`) e instalará las librerías necesarias (`pyautogui`, `Pillow`, `opencv-python`).
    -   En ejecuciones posteriores, el bot se iniciará directamente.

## 🕹️ Cómo usar el Bot

1.  Abre la aplicación o página web que deseas monitorear.
2.  Ejecuta `INICIAR_MOLTBOT.bat`.
3.  Presiona el botón **"ENCENDER BOT"** en la interfaz.
4.  **Acciones del Bot:**
    -   **Paso 1 (Run):** Busca el botón azul (basado en `run_button.png`). Si lo encuentra, hace clic y espera 5 segundos.
    -   **Paso 2 (Flecha):** Si no ve el botón "Run", busca una flecha hacia abajo (`down_arrow.png`). Si la encuentra, hace clic para desplazar la pantalla.
    -   **Paso 3 (Auto-Scroll):** Si después de 2 ciclos no encuentra nada, el bot realizará un *scroll* hacia abajo automáticamente para intentar localizar los elementos.

## 📁 Archivos importantes

-   `Boton_Run.py`: El código principal del bot (Lógica y GUI).
-   `INICIAR_MOLTBOT.bat`: El lanzador que prepara el entorno y arranca el bot.
-   `requirements.txt`: Lista de librerías necesarias.
-   `images/`: Contiene `run_button.png` y `down_arrow.png` (usados para el reconocimiento visual).

## ⚠️ Notas importantes

-   **Resolución**: El bot depende de las imágenes proporcionadas. Si los botones en tu pantalla lucen muy diferentes a las capturas originales, es posible que debas actualizar las imágenes en la carpeta del proyecto.
-   **Seguridad**: Puedes detener el bot en cualquier momento presionando el botón **"DETENER BOT"** en la interfaz.

---
*Desarrollado para optimización de flujos de trabajo.*
