# Vartoviy

📚 [Read in English](./README.md) 🇬🇧 📚 [Read in Ukrainian](./README_UA.md) 🇺🇦

**Vartoviy** (рабочее название - "Вартовий") - это платформа с открытым исходным кодом, специально разработанная для создания собственной инфраструктуры контроля за животными на фермах, где они выпасаются на открытых пространствах. С помощью Vartoviy вы легко развернете сервер в Docker-контейнере или на собственном компьютере, обеспечивая высокий уровень конфиденциальности и полный контроль над вашими данными. Этот проект обеспечивает полную прозрачность с открытым доступом к исходному коду сервера, прошивке устройства и подробным схемам самого устройства, что дает пользователям возможность полностью понимать его работу.

**Отмечается, что "Vartoviy" в настоящее время находится в стадии разработки.**

### Скриншоты
<p align="center">
    <img src="https://github.com/SimonOriginal/Vartoviy-Server/assets/94782611/d7679b6d-4e78-4536-80cd-659e940ceb7a" width="320" alt="Главная">
    <img src="https://github.com/SimonOriginal/Vartoviy-Server/assets/94782611/95d0d654-f70b-4bf9-9783-73979313bdb5" width="320" alt="Настройка барьера">
    <img src="https://github.com/SimonOriginal/Vartoviy-Server/assets/94782611/7c7acb89-7f51-4ba6-ab2e-179ded193074" width="320" alt="История перемещений">
    <img src="https://github.com/SimonOriginal/Vartoviy-Server/assets/94782611/815bd067-afab-46eb-b2ee-e04097f52740" width="320" alt="Главная">
    <img src="https://github.com/SimonOriginal/Vartoviy-Server/assets/94782611/5e2b6bf8-a003-4556-b166-4a3450e944a9" width="320" alt="Добавить устройство">
    <img src="https://github.com/SimonOriginal/Vartoviy-Server/assets/94782611/29e11bd5-0fcd-48c1-b3d2-8a47aa56e9fb" width="320" alt="Уведомления">
    <img src="https://github.com/SimonOriginal/Vartoviy-Server/assets/94782611/2c912861-7d4a-4da3-bd7d-52d56e3253e6" width="320" alt="Таблицы">
    <img src="https://github.com/SimonOriginal/Vartoviy-Server/assets/94782611/d15c5bad-4f85-4b48-840a-7f414a0b2952" width="320" alt="О проекте">
</p>

### Функции
* **Локализация для разных языков:** Пользователи могут выбирать язык интерфейса из предложенных, включая "🇬🇧 Английский", "🇺🇦 Украинский" и "🇷🇺 Русский". 🌐
* **Уведомления о преодолении барьера:** Система предоставляет уведомления в случае преодоления заданного барьера, обеспечивая оперативное оповещение о событиях. 🚨
* **Уведомления о низком заряде батареи (20%):** Пользователи получают уведомления при достижении уровня заряда батареи на устройстве 20%, обеспечивая своевременное предупреждение о необходимости зарядки. 🔋
* **Смена темы:** Пользователи могут выбирать между "🌞 Светлой" и "🌚 Темной" темами интерфейса, обеспечивая комфортный опыт использования в различных условиях освещения. 🎨
* **Подключение устройства по MQTT:** Используется протокол MQTT для устойчивого и эффективного подключения устройств, обеспечивая надежную передачу данных. 📡
* **Отображение последних данных в дашборде:** Пользователи могут наглядно отслеживать последние данные устройства через интуитивно понятный и информативный дашборд. 📊
* **Показ всей истории перемещений:** Предоставляется возможность просмотра полной истории перемещений конкретного устройства, что позволяет более глубоко анализировать его активность. 🕰️
* **Отображение графиков и модальных окон:** Графическое представление данных и возможность подробного анализа через модальные окна обеспечивают более глубокое понимание информации. 📈
* **Создание и сохранение барьера для конкретного устройства:** Пользователи могут определить и сохранить барьер для конкретного устройства, что обеспечивает персонализированный и гибкий контроль. 🛡️
* **Отображение местоположения устройства и барьера на карте:** Наглядное отображение текущего местоположения устройства и установленного барьера на карте. 🗺️
* **Возможность скачивания GeoJson настроенного барьера:** Пользователи могут легко скачивать географические данные барьера в формате GeoJson для дальнейшего использования или анализа. 📤
* **Использование внешней базы данных PostgreSQL:** Пользователи могут настроить подключение к внешней базе данных PostgreSQL для хранения данных, что обеспечивает масштабируемость и надежность работы системы при больших объемах информации. 🗃️

### Варианты установки
* **[Docker 🐳](#docker-installation)**
* **[Альтернативная установка](#alternative-installation)**

### Быстрый старт с Docker 🐳 <a name="docker-installation"></a>

Чтобы запустить проект в Docker-контейнере, выполните следующие шаги:

1. **Построение Docker-образа**:

   ```
   docker build -t vartoviy .
   ```

2. **Запуск Docker-контейнера**:

   ```
   docker run -p 8000:8000 -d vartoviy
   ```

   Эта команда запустит контейнер в фоновом режиме, назначит порт 8000 на вашем хосте порту 8000 в контейнере и использует имя образа, которое вы указали ранее.

3. **Доступ к проекту**: Теперь вы можете открыть проект в вашем браузере по адресу http://localhost:8000/.

Конечно, вот исправленный текст с учетом грамматических ошибок, форматирования для GitHub и добавлением эмодзи:


### Вариант с использованием внешней базы данных PostgreSQL

Перед запуском сборки нужно изменить в файле settings.py привязки к базе данных.

1. **Построение Docker-образа**:

   ```bash
   docker-compose up -d
   ```

2. **Настройка базы данных**:
   
   Чтобы настроить базу данных и создать суперпользователя с данными авторизации, выполните следующие шаги:
   
   ```bash
   docker-compose exec web sh -c "python manage.py makemigrations && python manage.py migrate" &&
   docker-compose down &&
   docker-compose up --build -d &&
   docker-compose exec -e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_EMAIL=admin@example.com -e DJANGO_SUPERUSER_PASSWORD=adminpassword web bash -c "python manage.py createsuperuser --noinput"
   ```
   
   Эти команды обновят базу данных, перезапустят Docker-контейнеры, и создадут суперпользователя с именем "admin", электронной почтой "admin@example.com" и паролем "adminpassword" (пожалуйста, используйте более безопасные пароли в реальном применении).

🚀 Готово! Теперь у вас есть Docker-образ с настроенной базой данных и суперпользователем для вашего Django-приложения.

### Альтернативная установка 🚀 <a name="alternative-installation"></a>

1. **Создание виртуального окружения**:

   ```
   python -m venv venv
   ```

2. **Активация виртуального окружения**:

   ```
   .\venv\Scripts\Activate.ps1
   ```

3. **Установка зависимостей**:

   ```
   pip install -r "requirements.txt"
   ```

4. **Миграции**:

   ```
   python manage.py makemigrations
   ```

   ```
   python manage.py migrate
   ```

5. **Запуск сервера**:

   ```
   python manage.py runserver
   ```
Теперь вы можете открыть проект в вашем браузере по адресу http://127.0.0.1:8000/.

6. **Запуск скрипта для виртуальных датчиков (опционально)**:

   ```
   python mqtt_virtual_sensor.py
   ```

