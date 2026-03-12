# 🤖 Moniteur d'Auto-gestion Pro (Bot Antigravity)

Ce bot est un système d'automatisation basé sur la reconnaissance visuelle. Il est conçu pour surveiller l'écran et réagir à l'apparition de boutons spécifiques ou effectuer des défilements automatiques s'il ne détecte aucune activité.

## 🚀 Prérequis

Pour que le bot fonctionne correctamente, vous devez avoir installé :
- **Python 3.10 ou supérieur** (Il est recommandé de cocher l'option "Add Python to PATH" pendant l'installation).

## 🛠️ Installation Rapide

1.  **Téléchargez le projet** dans un dossier de votre choix.
2.  **Lancez le script** : Double-cliquez sur le fichier `INICIAR_MOLTBOT.bat`.
    -   La première fois, le système créera automatiquement un environnement virtuel (`.venv`) et installera les bibliothèques nécessaires (`pyautogui`, `Pillow`, `opencv-python`).
    -   Pour les exécutions suivantes, le bot démarrera directement.

## 🕹️ Comment utiliser le Bot

1.  Ouvrez l'application ou la page web que vous souhaitez surveiller.
2.  Lancez `INICIAR_MOLTBOT.bat`.
3.  Appuyez sur le bouton **"ENCENDER BOT"** (Démarrer) sur l'interface.
4.  **Actions du Bot :**
    -   **Étape 1 (Run) :** Recherche le bouton bleu (basé sur `run_button.png`). S'il le trouve, il clique et attend 5 secondes.
    -   **Étape 2 (Flèche) :** S'il ne voit pas le bouton "Run", il cherche une flèche vers le bas (`down_arrow.png`). S'il la trouve, il clique pour faire défiler l'écran.
    -   **Étape 3 (Auto-Scroll) :** Si après 2 cycles il ne trouve rien, le bot effectuera un défilement (*scroll*) vers le bas automatiquement pour tenter de localiser les éléments.

## 📁 Fichiers Importants

-   `Boton_Run.py` : Le code principal du bot (Logique et GUI).
-   `INICIAR_MOLTBOT.bat` : Le lanceur qui prépare l'environnement et démarre le bot.
-   `requirements.txt` : Liste des bibliothèques nécessaires.
-   `images/` : Contient `run_button.png` et `down_arrow.png` (utilisés pour la reconnaissance visuelle).

## ⚠️ Notes Importantes

-   **Résolution** : Le bot dépend des images fournies. Si les boutons sur votre écran sont très différents des captures originales, vous devrez peut-être mettre à jour les images dans le dossier du projet.
-   **Sécurité** : Vous pouvez arrêter le bot à tout moment en appuyant sur le bouton **"DETENER BOT"** sur l'interface.

---
*Développé pour l'optimisation des flux de travail.*
