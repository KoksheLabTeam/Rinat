# TIMPLOV

## Запуск проекта

### 1. Клонирование репозитория
```bash
git clone https://github.com/KoksheLabTeam/Rinat.git
cd Rinat
```

### 2. Установка зависимостей
Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv venv
venv\Scripts\activate 
pip install -r requirements.txt
```

### 3. Настройка переменных окружения
Создайте файл `.env` на основе `.env.example` и укажите нужные переменные, которые указаны в `.env.example` файле. (Проще говоря просто скопируйте все что находится внутри `.env.example` файлф в `.env` "`.env` файл вам надо создать"). 

### 4. Запуск приложения
```bash
uvicorn app.main:app --reload
```

## Запуск через Docker Compose
Если у вас установлен **Docker** и **Docker Compose**, можно запустить проект с помощью контейнеров в отдельном терминале, предворительно запустив DockerDesktop:
```bash
docker-compose up --build
```

## Структура проекта
```
Rinat/
│── app/
│   ├── apis/depends/  # Зависимости и сами эндпойнты
│   ├── core/          # Основные модули проекта
│   │   ├── database/  # Подключение к базе данных
│   │   ├── models/    # Определения моделей данных
│   │   ├── repos/     # Репозитории для работы с БД
│   │   ├── schemas/   # Схемы (Pydantic) для API
│   │   ├── services/  # Бизнес-логика
│   │   ├── .env.example       # Пример файла переменных окружения
│   │   │── config.py          # Основные настройки проекта
│   │── main.py            # Точка входа в приложение
│── docker-compose.yaml  # Конфигурация Docker Compose
│── requirements.txt   # Список зависимостей проекта
│── README.md          # ТЗ проекта
│── RUN.md             # Инструкция как запустить проект
```