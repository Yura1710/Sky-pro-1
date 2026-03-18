# Урок 10: Allure + PageObject

## 📋 Описание проекта
Проект содержит автоматизированные тесты для веб-сайтов с использованием паттерна PageObject и Allure для отчетности.

### Тестируемые сайты:
- [Slow Calculator](https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html) - калькулятор с задержкой
- [Swag Labs](https://www.saucedemo.com/) - интернет-магазин

## 🛠️ Технологии
- Python 3.14+
- pytest
- Selenium WebDriver
- PageObject Pattern
- Allure Reports
- WebDriver Manager

## 📁 Структура проекта
lesson_10/
├── pages/ # PageObject классы
│ ├── init.py
│ ├── base_page.py # Базовый класс для всех страниц
│ ├── calculator_page.py # Страница калькулятора
│ ├── login_page.py # Страница авторизации
│ ├── inventory_page.py # Страница с товарами
│ ├── cart_page.py # Страница корзины
│ └── checkout_page.py # Страница оформления заказа
├── tests/ # Тесты
│ ├── init.py
│ ├── test_calculator.py # Тесты калькулятора
│ └── test_shop.py # Тесты магазина
├── conftest.py # Фикстуры pytest
├── requirements.txt # Зависимости проекта
└── README.md # Документация
## 🚀 Установка и настройка

### 1. Клонирование репозитория
```bash
git clone <url-репозитория>
cd lesson_10