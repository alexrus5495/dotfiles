#!/bin/bash

# Конфигурация вашего игрового монитора Samsung
MAIN_MONITOR="DVI-D-1"
MAIN_RESOLUTION="1920x1080"
MAIN_REFRESH="74.97"
MAIN_SCALE="1.0"

# Смещение для блокировки (100px вправо от текущего положения)
LOCK_OFFSET=600

# Получаем текущее положение X
curr_x=$(hyprctl -j monitors | jq -r ".[] | select(.name == \"$MAIN_MONITOR\") | .x")

if [ $curr_x -eq 3212 ]; then
  # Блокируем мышь - смещаем монитор вправо
  new_x=$((3212 + LOCK_OFFSET))
  echo "Активация блокировки: смещение до $new_x"
else
  # Разблокируем - возвращаем исходное положение
  new_x=3212
  echo "Деактивация блокировки: возврат на $new_x"
fi

# Применяем изменения
hyprctl keyword monitor $MAIN_MONITOR,${MAIN_RESOLUTION}@${MAIN_REFRESH},${new_x}x421,${MAIN_SCALE}

# Даем время на применение изменений монитора
sleep 0.2

# Перезапуск waybar (аккуратный способ)
if pgrep -x "waybar" > /dev/null; then
  # Проверяем, поддерживает ли waybar сигнал для перезагрузки
  pkill -SIGUSR2 waybar 2>/dev/null || {
    # Если не поддерживает - перезапускаем полностью
    pkill waybar
    sleep 0.1
    waybar &
  }
fi

