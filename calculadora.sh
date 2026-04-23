#!/bin/bash

# =================================================================
# Lanzador Universal para Calculadora Casio fx991
# Optimizado para distribución en GitHub
# =================================================================

# 1. Obtener la ruta absoluta del directorio donde se encuentra este script
# Esto permite que el usuario ejecute el script desde cualquier lugar.
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_PATH="$DIR/main.py"

# 2. Verificar si el archivo principal existe
if [ ! -f "$APP_PATH" ]; then
    echo "Error: No se encontró el archivo main.py en $DIR"
    exit 1
fi

# 3. Verificar si Python3 está instalado
if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: Python3 no está instalado. Por favor, instálalo para usar la calculadora."
    exit 1
fi

# 4. Lista de emuladores de terminal por orden de popularidad/calidad
TERMINALS=("kitty" "xfce4-terminal" "gnome-terminal" "konsole" "alacritty" "mate-terminal" "xterm")

# 5. Intentar abrir en una terminal externa
for term in "${TERMINALS[@]}"; do
    if command -v "$term" >/dev/null 2>&1; then
        case $term in
            kitty)
                exec "$term" --hold python3 "$APP_PATH" &
                exit 0
                ;;
            xfce4-terminal)
                exec "$term" --hold -x python3 "$APP_PATH" &
                exit 0
                ;;
            gnome-terminal | mate-terminal)
                # Estas terminales prefieren el uso de '--' para pasar comandos
                exec "$term" -- bash -c "python3 \"$APP_PATH\"; exec bash" &
                exit 0
                ;;
            konsole)
                exec "$term" --hold -e python3 "$APP_PATH" &
                exit 0
                ;;
            *)
                # Fallback genérico para terminales clásicas
                exec "$term" -e "python3 \"$APP_PATH\"" &
                exit 0
                ;;
        esac
    fi
done

# 6. Fallback final: Si no se detecta emulador gráfico, ejecutar en la terminal actual
echo "No se detectó un emulador de terminal compatible instalado."
echo "Iniciando calculadora en la sesión actual..."
python3 "$APP_PATH"
