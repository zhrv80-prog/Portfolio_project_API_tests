# Фреймворк для тестирования API Contact List App 

[English](./README.md) | **Русский**

[![Python](https://img.shields.io/badge/Python-3.14-blue)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-9.1-green)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-2.13-orange)](https://allurereport.org/)

![Python_icon.png](pictures/icons/Python_icon.png)
![Pytest_icon.png](pictures/icons/Pytest_icon.png)
![Allure_icon.png](pictures/icons/Allure_icon.png)
![GitHub_icon.png](pictures/icons/GitHub_icon.png)
![PyCharm_icon.png](pictures/icons/PyCharm_icon.png)
![Requests_icon.png](pictures/icons/Requests_icon.png)
![Jenkins_icon.png](pictures/icons/Jenkins_icon.png)

## 📖 Документация API

- [Postman Collection — Contact List App](https://documenter.getpostman.com/view/4012288/TzK2bEa8)

## ✅ Список проверок

- Создание пользователя
- Получение информации о пользователе
- Удаление пользователя

## 🛠 Стек технологий

| Технология | Назначение |
| :--- | :--- |
| **Python 3.14** | Язык программирования |
| **pytest** | Фреймворк для тестирования |
| **requests** | HTTP-клиент для API-запросов |
| **Allure** | Генерация отчётов |

## 🚀 Установка и запуск

### 💻 1. Клонировать репозиторий
#### - Ввести свой вариант пароля вместо "password" (optional)

```bash
git clone https://github.com/zhrv80-prog/PythonProject.git
cd Portfolio_project_tests
MY_APP_PASSWORD="password" pytest
```
## Allure отчет

![Allure.JPG](pictures/Allure.JPG)

## Jenkins

Проект интегрирован с Jenkins. 
Пайплайн автоматически запускает тесты при пуше в репозиторий. Конфигурация пайплайна находится в файле Jenkinsfile

![jenkins.JPG](pictures/Jenkins.JPG)

## Allure отчет в Jenkins 

![Allure.JPG](pictures/Allure_Jenkins.JPG)