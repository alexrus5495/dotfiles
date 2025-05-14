#!/bin/bash

# Запускаем gnome-calendar в плавающем режиме с нужными параметрами
hyprctl dispatch exec "[float; size 300 400; move 100%-335 142] gnome-calendar"

# Альтернативный вариант (если не работает через hyprctl):
# gnome-calendar &
# sleep 0.5
# hyprctl dispatch togglefloating active
# hyprctl dispatch resizeactive 600 500
# hyprctl dispatch moveactive 100%-620 40
