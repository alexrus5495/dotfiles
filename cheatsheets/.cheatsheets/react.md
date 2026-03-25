# React + TypeScript Cheat Sheet (Terminal-Friendly)

---

## 1. Компоненты

```tsx
type Props = { title: string };

export function Header({ title }: Props) {
  return <h1>{title}</h1>;
}
```

- Компонент = чистая функция (в идеале), получает props → возвращает JSX
- Ререндер происходит при изменении props/state
- Типизация props обязательна для читаемости и безопасности

---

## 2. JSX / TSX особенности

```tsx
const name: string = "John";
return <div>Hello, {name}</div>;
```

- JSX = синтаксический сахар над `React.createElement`
- `{}` используется для выполнения JS/TS выражений
- Нельзя писать statements (`if`, `for`) — только expressions
- Все теги должны быть закрыты

---

## 3. Props (типизация)

```tsx
type ButtonProps = {
  text: string;
  onClick?: () => void;
};
```

- Props — входные данные, immutable
- Лучше явно описывать контракт компонента
- Можно комбинировать типы (`&`, `|`)

```tsx
function Button({ text, onClick }: ButtonProps) {
  return <button onClick={onClick}>{text}</button>;
}
```

---

## 4. State (useState)

```tsx
const [count, setCount] = useState<number>(0);
const [user, setUser] = useState<User | null>(null);
```

- State — внутреннее состояние компонента
- Изменение через setter → вызывает ререндер
- Обновления могут батчиться (асинхронность)

```tsx
setCount((prev) => prev + 1);
```

- Функциональный апдейт — безопаснее при зависимостях от предыдущего значения

---

## 5. События (типизация)

```tsx
const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {};
```

```tsx
const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
  setValue(e.target.value);
};
```

- SyntheticEvent — обёртка над нативными событиями
- Тип элемента важен (HTMLInputElement, HTMLButtonElement)

---

## 6. Условный рендеринг

```tsx
{
  isAuth ? <App /> : <Login />;
}
{
  isOpen && <Modal />;
}
```

- `&&` возвращает второй операнд, если первый truthy
- `false`, `null`, `undefined` не рендерятся
- Избегай сложной логики прямо в JSX

---

## 7. Списки

```tsx
items.map((item) => <li key={item.id}>{item.name}</li>);
```

- `key` нужен для reconciliation (сравнение дерева)
- Нельзя использовать index при изменяемых списках
- key влияет на сохранение состояния элементов

---

## 8. useEffect

```tsx
useEffect(() => {
  // side effect
}, []);
```

- Выполняется после рендера
- Используется для:
  - запросов
  - подписок
  - таймеров

```tsx
useEffect(() => {
  const id = setInterval(() => {}, 1000);
  return () => clearInterval(id);
}, []);
```

- cleanup вызывается при размонтировании или перед повторным вызовом эффекта
- зависимости определяют, когда эффект пересчитывается

---

## 9. Формы (controlled)

```tsx
const [value, setValue] = useState<string>("");

<input value={value} onChange={(e) => setValue(e.target.value)} />;
```

- Controlled компонент: React управляет значением
- Альтернатива: uncontrolled (через ref)
- Controlled проще валидировать и синхронизировать

---

## 10. Поднятие состояния

```tsx
function Parent() {
  const [value, setValue] = useState("");
  return <Child value={value} setValue={setValue} />;
}
```

- Если несколько компонентов используют одни данные → переносим state вверх
- Один источник истины (single source of truth)

---

## 11. useRef

```tsx
const inputRef = useRef<HTMLInputElement | null>(null);
inputRef.current?.focus();
```

- `.current` — изменяемое значение
- Не вызывает ререндер
- Используется для DOM и хранения значений между рендерами

---

## 12. Context

```tsx
type Theme = "light" | "dark";
const ThemeContext = createContext<Theme>("light");
```

```tsx
const theme = useContext(ThemeContext);
```

- Решает проблему глубокого проброса props
- Любое изменение value → ререндер всех подписчиков
- Часто комбинируется с useReducer

---

## 13. Оптимизация

```tsx
export default React.memo(Component);
```

- Мемоизация компонента по props (shallow compare)

```tsx
const value = useMemo(() => compute(a), [a]);
const fn = useCallback(() => doSomething(a), [a]);
```

- `useMemo` — кэш значения
- `useCallback` — кэш функции
- Использовать только при реальной необходимости (иначе overhead)

---

## 14. Кастомные хуки

```tsx
function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(null);

  useEffect(() => {
    fetch(url)
      .then((r) => r.json())
      .then(setData);
  }, [url]);

  return data;
}
```

- Вынос логики в переиспользуемую функцию
- Можно инкапсулировать состояние, эффекты, обработку ошибок

---

## 15. Частые ошибки

- ❌ мутация state (ломает предсказуемость)
- ❌ отсутствует key
- ❌ лишние эффекты / неправильные зависимости
- ❌ чрезмерный any
- ❌ логика + рендер вперемешку

---

## 16. Минимальный шаблон

```tsx
import { useState, useEffect } from "react";

export default function App() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    fetch("/api")
      .then((r) => r.json())
      .then(setData);
  }, []);

  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}
```

---

(Оптимизировано для быстрого просмотра через Glow)
