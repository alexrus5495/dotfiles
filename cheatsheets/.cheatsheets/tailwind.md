# 🎨 Tailwind CSS v4.2+ Шпаргалка (Март 2026)

> Быстрый поиск классов прямо в терминале. Сохрани этот файл и используй `cat`, `less` или `grep` для поиска.

---

## 📐 Лейаут и позиционирование

### Flexbox
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Включить flex | `flex` | `display: flex;` |
| Направление: строка | `flex-row` | `flex-direction: row;` |
| Направление: строка (reverse) | `flex-row-reverse` | `flex-direction: row-reverse;` |
| Направление: колонка | `flex-col` | `flex-direction: column;` |
| Направление: колонка (reverse) | `flex-col-reverse` | `flex-direction: column-reverse;` |
| Главная ось: начало | `justify-start` | `justify-content: flex-start;` |
| Главная ось: конец | `justify-end` | `justify-content: flex-end;` |
| Главная ось: центр | `justify-center` | `justify-content: center;` |
| Главная ось: между | `justify-between` | `justify-content: space-between;` |
| Главная ось: вокруг | `justify-around` | `justify-content: space-around;` |
| Главная ось: равномерно | `justify-evenly` | `justify-content: space-evenly;` |
| Поперечная ось: начало | `items-start` | `align-items: flex-start;` |
| Поперечная ось: конец | `items-end` | `align-items: flex-end;` |
| Поперечная ось: центр | `items-center` | `align-items: center;` |
| Поперечная ось: базовая линия | `items-baseline` | `align-items: baseline;` |
| Поперечная ось: растянуть | `items-stretch` | `align-items: stretch;` |
| Зазоры | `gap-4` | `gap: 1rem;` |

### Grid
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Включить grid | `grid` | `display: grid;` |
| Колонки: 2 колонки | `grid-cols-2` | `grid-template-columns: repeat(2, minmax(0, 1fr));` |
| Колонки: 12 колонок | `grid-cols-12` | `grid-template-columns: repeat(12, minmax(0, 1fr));` |
| Колонки: автоматические | `grid-cols-none` | `grid-template-columns: none;` |
| Строки: 2 строки | `grid-rows-2` | `grid-template-rows: repeat(2, minmax(0, 1fr));` |
| Элемент: на 2 колонки | `col-span-2` | `grid-column: span 2 / span 2;` |
| Элемент: на 3 строки | `row-span-3` | `grid-row: span 3 / span 3;` |
| Элемент: начать с колонки 2 | `col-start-2` | `grid-column-start: 2;` |
| Элемент: закончить на колонке 4 | `col-end-4` | `grid-column-end: 4;` |

### Позиционирование
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Статичное | `static` | `position: static;` |
| Фиксированное | `fixed` | `position: fixed;` |
| Абсолютное | `absolute` | `position: absolute;` |
| Относительное | `relative` | `position: relative;` |
| Липкое | `sticky` | `position: sticky;` |
| Со всех сторон 0 | `inset-0` | `top: 0; right: 0; bottom: 0; left: 0;` |
| По горизонтали 0 | `inset-x-0` | `left: 0; right: 0;` |
| По вертикали 0 | `inset-y-0` | `top: 0; bottom: 0;` |
| Сверху 0 | `top-0` | `top: 0;` |
| Справа 0 | `right-0` | `right: 0;` |
| Снизу 0 | `bottom-0` | `bottom: 0;` |
| Слева 0 | `left-0` | `left: 0;` |
| Инлайн-начало 4 | `inset-s-4` | `inset-inline-start: 1rem;` |
| Инлайн-конец 4 | `inset-e-4` | `inset-inline-end: 1rem;` |
| Блок-начало 4 | `inset-bs-4` | `inset-block-start: 1rem;` |
| Блок-конец 4 | `inset-be-4` | `inset-block-end: 1rem;` |
| Z-index: 10 | `z-10` | `z-index: 10;` |
| Z-index: авто | `z-auto` | `z-index: auto;` |

---

## 📏 Размеры

| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Ширина: 1rem | `w-4` | `width: 1rem;` |
| Ширина: 50% | `w-1/2` | `width: 50%;` |
| Ширина: 100% | `w-full` | `width: 100%;` |
| Ширина: экран | `w-screen` | `width: 100vw;` |
| Ширина: авто | `w-auto` | `width: auto;` |
| Ширина: min-content | `w-min` | `width: min-content;` |
| Ширина: max-content | `w-max` | `width: max-content;` |
| Высота: 1rem | `h-4` | `height: 1rem;` |
| Высота: 100% | `h-full` | `height: 100%;` |
| Высота: экран | `h-screen` | `height: 100vh;` |
| Инлайн-размер: 1rem | `inline-4` | `inline-size: 1rem;` |
| Блок-размер: 1rem | `block-4` | `block-size: 1rem;` |
| Мин. ширина: 0 | `min-w-0` | `min-width: 0;` |
| Макс. ширина: md | `max-w-md` | `max-width: 28rem;` |
| Мин. высота: экран | `min-h-screen` | `min-height: 100vh;` |
| Макс. высота: полная | `max-h-full` | `max-height: 100%;` |

---

## 🎨 Отступы (Spacing)

### Padding
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Со всех сторон 1rem | `p-4` | `padding: 1rem;` |
| Горизонтально 1rem | `px-4` | `padding-left: 1rem; padding-right: 1rem;` |
| Вертикально 1rem | `py-4` | `padding-top: 1rem; padding-bottom: 1rem;` |
| Сверху 1rem | `pt-4` | `padding-top: 1rem;` |
| Снизу 1rem | `pb-4` | `padding-bottom: 1rem;` |
| Слева 1rem | `pl-4` | `padding-left: 1rem;` |
| Справа 1rem | `pr-4` | `padding-right: 1rem;` |
| Инлайн-начало 1rem | `pis-4` | `padding-inline-start: 1rem;` |
| Инлайн-конец 1rem | `pie-4` | `padding-inline-end: 1rem;` |
| Блок-начало 1rem | `pbs-4` | `padding-block-start: 1rem;` |
| Блок-конец 1rem | `pbe-4` | `padding-block-end: 1rem;` |

### Margin
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Со всех сторон 1rem | `m-4` | `margin: 1rem;` |
| Горизонтально 1rem | `mx-4` | `margin-left: 1rem; margin-right: 1rem;` |
| Вертикально 1rem | `my-4` | `margin-top: 1rem; margin-bottom: 1rem;` |
| Сверху 1rem | `mt-4` | `margin-top: 1rem;` |
| Снизу 1rem | `mb-4` | `margin-bottom: 1rem;` |
| Слева 1rem | `ml-4` | `margin-left: 1rem;` |
| Справа 1rem | `mr-4` | `margin-right: 1rem;` |
| Инлайн-начало 1rem | `mis-4` | `margin-inline-start: 1rem;` |
| Инлайн-конец 1rem | `mie-4` | `margin-inline-end: 1rem;` |
| Блок-начало 1rem | `mbs-4` | `margin-block-start: 1rem;` |
| Блок-конец 1rem | `mbe-4` | `margin-block-end: 1rem;` |

---

## 🖌️ Типографика

### Текст
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Размер: xs | `text-xs` | `font-size: 0.75rem;` |
| Размер: sm | `text-sm` | `font-size: 0.875rem;` |
| Размер: base | `text-base` | `font-size: 1rem;` |
| Размер: lg | `text-lg` | `font-size: 1.125rem;` |
| Размер: xl | `text-xl` | `font-size: 1.25rem;` |
| Размер: 2xl | `text-2xl` | `font-size: 1.5rem;` |
| Толщина: тонкий (100) | `font-thin` | `font-weight: 100;` |
| Толщина: светлый (300) | `font-light` | `font-weight: 300;` |
| Толщина: нормальный (400) | `font-normal` | `font-weight: 400;` |
| Толщина: средний (500) | `font-medium` | `font-weight: 500;` |
| Толщина: полужирный (600) | `font-semibold` | `font-weight: 600;` |
| Толщина: жирный (700) | `font-bold` | `font-weight: 700;` |
| Межстрочный интервал: 1 | `leading-4` | `line-height: 1rem;` |
| Межстрочный интервал: уплотненный | `leading-tight` | `line-height: 1.25;` |
| Межстрочный интервал: нормальный | `leading-normal` | `line-height: 1.5;` |
| Межбуквенный интервал: уже | `tracking-tight` | `letter-spacing: -0.025em;` |
| Межбуквенный интервал: нормальный | `tracking-normal` | `letter-spacing: 0em;` |
| Межбуквенный интервал: шире | `tracking-wide` | `letter-spacing: 0.025em;` |
| Выравнивание: влево | `text-left` | `text-align: left;` |
| Выравнивание: по центру | `text-center` | `text-align: center;` |
| Выравнивание: вправо | `text-right` | `text-align: right;` |
| Все заглавные | `uppercase` | `text-transform: uppercase;` |
| Подчеркнутый | `underline` | `text-decoration: underline;` |
| Зачеркнутый | `line-through` | `text-decoration: line-through;` |

### Цвета текста
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Серый 900 | `text-gray-900` | `color: #111827;` |
| Синий 500 | `text-blue-500` | `color: #3b82f6;` |
| Красный 500 | `text-red-500` | `color: #ef4444;` |
| Зеленый 500 | `text-green-500` | `color: #10b981;` |
| Прозрачность 50% | `text-black/50` | `color: rgb(0 0 0 / 0.5);` |

---

## 🎭 Фоны и границы

### Фон
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Белый фон | `bg-white` | `background-color: #fff;` |
| Серый 100 | `bg-gray-100` | `background-color: #f3f4f6;` |
| Синий 500 | `bg-blue-500` | `background-color: #3b82f6;` |
| Градиент: слева направо | `bg-gradient-to-r` | `background-image: linear-gradient(to right, ...);` |
| Градиент: от синего | `from-blue-500` | `--tw-gradient-from: #3b82f6;` |
| Градиент: до фиолетового | `to-purple-500` | `--tw-gradient-to: #a855f7;` |

### Скругление
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Без скругления | `rounded-none` | `border-radius: 0;` |
| Маленькое | `rounded-sm` | `border-radius: 0.125rem;` |
| Обычное | `rounded` | `border-radius: 0.25rem;` |
| Среднее | `rounded-md` | `border-radius: 0.375rem;` |
| Большое | `rounded-lg` | `border-radius: 0.5rem;` |
| Полное (круг) | `rounded-full` | `border-radius: 9999px;` |
| Сверху слева | `rounded-tl-lg` | `border-top-left-radius: 0.5rem;` |
| Сверху | `rounded-t-lg` | `border-top-left-radius: 0.5rem; border-top-right-radius: 0.5rem;` |

### Границы
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Тонкая граница | `border` | `border-width: 1px;` |
| Без границы | `border-0` | `border-width: 0;` |
| Толщина 2px | `border-2` | `border-width: 2px;` |
| Толщина 4px | `border-4` | `border-width: 4px;` |
| Сверху | `border-t` | `border-top-width: 1px;` |
| Снизу | `border-b` | `border-bottom-width: 1px;` |
| Слева | `border-l` | `border-left-width: 1px;` |
| Справа | `border-r` | `border-right-width: 1px;` |
| Инлайн-начало | `border-s` | `border-inline-start-width: 1px;` |
| Инлайн-конец | `border-e` | `border-inline-end-width: 1px;` |
| Цвет: серый 200 | `border-gray-200` | `border-color: #e5e7eb;` |
| Сплошная | `border-solid` | `border-style: solid;` |
| Пунктирная | `border-dashed` | `border-style: dashed;` |
| Точечная | `border-dotted` | `border-style: dotted;` |

---

## ✨ Эффекты

### Тени
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Без тени | `shadow-none` | `box-shadow: none;` |
| Очень маленькая | `shadow-xs` | `box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);` |
| Маленькая | `shadow-sm` | `box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);` |
| Средняя | `shadow-md` | `box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);` |
| Большая | `shadow-lg` | `box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);` |
| Внутренняя | `shadow-inner` | `box-shadow: inset 0 2px 4px 0 rgb(0 0 0 / 0.05);` |

### Размытие
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Очень маленькое | `blur-xs` | `filter: blur(4px);` |
| Маленькое | `blur-sm` | `filter: blur(8px);` |
| Обычное | `blur` | `filter: blur(12px);` |
| Среднее | `blur-md` | `filter: blur(16px);` |
| Большое | `blur-lg` | `filter: blur(24px);` |

### Другие
| Если надо | Tailwind класс | CSS-аналог |
|-----------|----------------|------------|
| Прозрачность 50% | `opacity-50` | `opacity: 0.5;` |
| Прозрачность 0% | `opacity-0` | `opacity: 0;` |
| Прозрачность 100% | `opacity-100` | `opacity: 1;` |
| Размытие фона | `backdrop-blur-sm` | `backdrop-filter: blur(8px);` |

---

## 🎯 Состояния (префиксы)

| Состояние | Префикс | Пример использования |
|-----------|---------|---------------------|
| При наведении | `hover:` | `<div class="hover:bg-blue-600">` |
| При фокусе | `focus:` | `<input class="focus:ring-2">` |
| При фокусе внутри | `focus-within:` | `<div class="focus-within:shadow-lg">` |
| При активации | `active:` | `<button class="active:scale-95">` |
| Посещенная ссылка | `visited:` | `<a class="visited:text-purple-600">` |
| Отключенный | `disabled:` | `<button class="disabled:opacity-50">` |
| Группа (при наведении) | `group-hover:` | `<div class="group">...<p class="group-hover:text-white">` |
| Псевдо-элемент до | `before:` | `<div class="before:content-['']">` |
| Псевдо-элемент после | `after:` | `<div class="after:content-['']">` |
| Темная тема | `dark:` | `<div class="dark:bg-gray-900">` |

---

## 📱 Адаптивность (медиа-запросы)

| Префикс | Минимальная ширина | Пример |
|---------|-------------------|--------|
| `sm:` | 640px | `<div class="text-base sm:text-lg">` |
| `md:` | 768px | `<div class="w-full md:w-1/2">` |
| `lg:` | 1024px | `<div class="p-4 lg:p-8">` |
| `xl:` | 1280px | `<div class="text-center xl:text-left">` |
| `2xl:` | 1536px | `<div class="max-w-md 2xl:max-w-xl">` |

---

## 🔧 Произвольные значения

| Синтаксис | Пример | CSS-результат |
|-----------|--------|---------------|
| Произвольная ширина | `w-[250px]` | `width: 250px;` |
| Произвольный цвет | `bg-[#bada55]` | `background-color: #bada55;` |
| Произвольный размер | `text-[22px]` | `font-size: 22px;` |
| Произвольное свойство | `[mask-type:luminance]` | `mask-type: luminance;` |
| CSS-переменная | `[--gutter:2rem]` | `--gutter: 2rem;` |
| Использование переменной | `w-(--gutter)` | `width: var(--gutter);` |

---

## 🚀 Быстрый grep по шпаргалке

```bash
# Показать все flex классы
grep -A5 "### Flexbox" tailwind-cheatsheet.md

# Найти конкретный класс
grep "justify-between" tailwind-cheatsheet.md

# Найти по CSS-свойству
grep "flex-direction" tailwind-cheatsheet.md

# Найти все классы для отступов
grep -E "(padding|margin):" tailwind-cheatsheet.md