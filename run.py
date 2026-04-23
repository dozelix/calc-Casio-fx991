import platform
import subprocess
import os

# Ruta absoluta de tu aplicación
script_path = "/home/dozelix/Documentos/vs/calc-Casio-fx991/main.py"

def abrir_terminal():
    os_name = platform.system()

    if os_name == "Linux":
        # Intenta usar el estándar de Debian/Ubuntu/Mint, si no, busca terminales comunes
        terminals = ["x-terminal-emulator", "gnome-terminal", "xfce4-terminal", "konsole", "xterm"]
        for term in terminals:
            if subprocess.run(["which", term], capture_output=True).returncode == 0:
                subprocess.Popen([term, "-e", f"python3 {script_path}"])
                return

    elif os_name == "Windows":
        # Abre una nueva ventana de CMD y ejecuta el script
        subprocess.Popen(["start", "cmd", "/k", f"python {script_path}"], shell=True)

    elif os_name == "Darwin":  # macOS
        # Usa AppleScript para abrir Terminal.app
        cmd = f'tell application "Terminal" to do script "python3 {script_path}"'
        subprocess.Popen(["osascript", "-e", cmd])

if __name__ == "__main__":
    abrir_terminal()
