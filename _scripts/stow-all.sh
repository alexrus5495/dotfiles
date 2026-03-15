#!/bin/bash
# Скрипт для стоувинга всех пакетов в dotfiles

cd "$(dirname "$0")/../.." || exit 1 # Переходим в корень dotfiles

echo "📦 Стоувлю все пакеты..."
for package in */; do
  # Пропускаем папку scripts
  if [[ "$package" != "_scripts/" ]]; then
    package=${package%/}
    echo "  ➜ $package"
    stow "$package"
  fi
done
echo "✅ Готово!"
