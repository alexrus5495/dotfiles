#!/usr/bin/env python3

import sys
import subprocess
import html
import os

# Конфигурация
TERMINAL = ['kitty', '--']  # замените на ваш терминал

def main():
    # Получаем команду от Rofi
    command = html.unescape(' '.join(sys.argv[1:])).strip()
    
    if not command:
        return
    
    # Для zsh нужно:
    # 1. Использовать zsh -c для выполнения команды
    # 2. Алиасы по умолчанию НЕ доступны в не-интерактивном режиме
    # 3. Используем zsh -i -c для интерактивного режима (загружает .zshrc)
    
    subprocess.Popen(
        TERMINAL + ['zsh', '-i', '-c', command],
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.DEVNULL,
        start_new_session=True
    )

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(1)
