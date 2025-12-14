# Selenium WebDriver Python - Lab 6

Повний набір автоматизованих тестів з використанням Selenium WebDriver для Python, який демонструє основні можливості автоматизації веб-браузера.

## 📋 Зміст

- [Опис проєкту](#опис-проєкту)
- [Структура проєкту](#структура-проєкту)
- [Встановлення](#встановлення)
- [Використання](#використання)
- [Модулі та їх функції](#модулі-та-їх-функції)
- [Технології](#технології)
- [Автор](#автор)

## 📖 Опис проєкту

Цей проєкт містить набір скриптів для автоматизації веб-тестування з використанням Selenium WebDriver. Кожен скрипт демонструє різні аспекти роботи з веб-елементами, навігацією та взаємодією з браузером.

### Основні функції:

- ✅ Автоматизація пошуку в Google
- ✅ Автоматизація заповнення форм
- ✅ Демонстрація роботи з CSS та XPath селекторами
- ✅ Демонстрація навігації браузера
- ✅ Автоматичне створення скріншотів
- ✅ Логування всіх операцій
- ✅ Обробка помилок
- ✅ Звітність про виконання тестів

## 📁 Структура проєкту

```
yaptz_lab6/
├── .gitignore              # Файли для ігнорування Git
├── requirements.txt        # Python залежності
├── config.py              # Конфігураційні налаштування
├── screenshot_utils.py    # Утиліти для скріншотів
├── google_search.py       # Автоматизація пошуку Google
├── form_automation.py     # Автоматизація форм
├── selectors_demo.py      # Демонстрація селекторів
├── navigation_demo.py     # Демонстрація навігації
├── main.py               # Головний скрипт
├── README.md             # Документація (цей файл)
├── REPORT.md             # Звіт про виконання
└── screenshots/          # Папка для скріншотів (створюється автоматично)
```

## 🔧 Встановлення

### Передумови

Перед початком переконайтеся, що у вас встановлено:

- Python 3.8 або вище
- pip (менеджер пакетів Python)
- Google Chrome браузер

### Крок 1: Клонування репозиторію

```bash
git clone https://github.com/ar4lin/yaptz_lab6.git
cd yaptz_lab6
```

### Крок 2: Встановлення залежностей

```bash
pip install -r requirements.txt
```

Це встановить:
- `selenium` - бібліотека для автоматизації браузера
- `webdriver-manager` - автоматичне управління драйверами браузера

### Крок 3: Перевірка встановлення

```bash
python --version
pip list | grep selenium
```

## 🚀 Використання

### Вибір браузера

За замовчуванням використовується headless режим Chrome. Для зміни налаштувань використовуйте змінні оточення:

**Використати Firefox:**
```bash
export BROWSER=firefox
python main.py
```

**Вимкнути headless режим:**
```bash
export HEADLESS=false
python main.py
```

**Комбінація налаштувань:**
```bash
export BROWSER=firefox
export HEADLESS=false
python main.py
```

### Встановлення браузерів

**Ubuntu/Debian:**
```bash
# Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f

# Firefox
sudo apt install firefox
```

### Запуск всіх тестів

Для запуску всього набору тестів використовуйте головний скрипт:

```bash
python main.py
```

Цей скрипт послідовно запустить всі тести та згенерує детальний звіт.

### Запуск окремих тестів

#### 1. Google Search Automation

Автоматизує пошук в Google та виводить перший результат:

```bash
python google_search.py
```

**Що робить:**
- Відкриває Google Chrome
- Переходить на google.com
- Вводить запит "Selenium WebDriver Python"
- Виконує пошук
- Виводить заголовок першого результату
- Робить скріншот результатів

#### 2. Form Automation

Автоматизує заповнення веб-форми:

```bash
python form_automation.py
```

**Що робить:**
- Переходить на тестову форму Selenium
- Заповнює всі поля (текст, пароль, textarea, dropdown, checkbox, radio, datepicker)
- Відправляє форму
- Перевіряє успішну відправку
- Робить скріншоти до та після

#### 3. Selectors Demonstration

Демонструє різні типи селекторів:

```bash
python selectors_demo.py
```

**Що робить:**
- Показує CSS селектори (ID, class, attribute, type)
- Показує XPath селектори (absolute, relative, by text, contains)
- Порівнює швидкість різних селекторів
- Пояснює переваги кожного типу

#### 4. Navigation Demonstration

Демонструє навігацію браузера:

```bash
python navigation_demo.py
```

**Що робить:**
- Навігація по сторінках (forward/back)
- Оновлення сторінки (refresh)
- Робота з вкладками
- Робота з вікнами
- Перемикання між вікнами

## 📚 Модулі та їх функції

### config.py

Центральний файл конфігурації з налаштуваннями:

```python
# Налаштування браузера
BROWSER = os.getenv('BROWSER', 'auto')  # 'chrome', 'firefox', 'auto'
HEADLESS = os.getenv('HEADLESS', 'true').lower() == 'true'
BROWSER_WINDOW_SIZE = (1920, 1080)

# Timeout налаштування
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15
PAGE_LOAD_TIMEOUT = 30

# URLs для тестування
GOOGLE_URL = "https://www.google.com"
SELENIUM_FORM_URL = "https://www.selenium.dev/selenium/web/web-form.html"

# Налаштування скріншотів
SCREENSHOT_DIR = "screenshots"
SCREENSHOT_FORMAT = "%Y%m%d_%H%M%S"
```

Функція `get_webdriver()` автоматично:
- Спробує Chrome, потім Firefox
- Виправляє баг з неправильним шляхом до chromedriver
- Підтримує headless режим
- Налаштовує всі необхідні параметри

### screenshot_utils.py

Утиліти для роботи зі скріншотами:

**Функції:**
- `ensure_screenshot_dir()` - створює папку для скріншотів
- `generate_filename()` - генерує унікальне ім'я з timestamp
- `take_screenshot()` - робить скріншот всієї сторінки
- `take_element_screenshot()` - робить скріншот окремого елемента
- `take_multiple_screenshots()` - робить кілька скріншотів

### google_search.py

Автоматизація пошуку в Google:

**Ключові функції:**
- `setup_driver()` - налаштовує WebDriver
- `google_search_automation()` - основна логіка пошуку
- Обробка cookie consent діалогів
- Різні стратегії пошуку search box
- Explicit waits для стабільності

### form_automation.py

Автоматизація роботи з формами:

**Типи елементів:**
- Text input
- Password field
- Textarea
- Dropdown (Select)
- Checkboxes
- Radio buttons
- Date picker
- Color picker

### selectors_demo.py

Демонстрація роботи з селекторами:

**CSS Selectors:**
- By ID: `#my-id`
- By Class: `.my-class`
- By Attribute: `[name='value']`
- Descendant: `parent child`
- Child: `parent > child`
- Pseudo-class: `:first-of-type`

**XPath Selectors:**
- By ID: `//*[@id='my-id']`
- By Attribute: `//tag[@attr='value']`
- By Text: `//tag[text()='value']`
- Contains: `//tag[contains(@attr, 'value')]`
- Starts-with: `//tag[starts-with(@attr, 'value')]`
- Following-sibling: `//tag/following-sibling::tag`

### navigation_demo.py

Демонстрація навігації:

**Операції:**
- `driver.get(url)` - відкриття URL
- `driver.back()` - назад
- `driver.forward()` - вперед
- `driver.refresh()` - оновлення
- `driver.switch_to.new_window('tab')` - нова вкладка
- `driver.switch_to.new_window('window')` - нове вікно
- `driver.switch_to.window(handle)` - перемикання між вікнами

### main.py

Головний скрипт для запуску всіх тестів:

**Функціональність:**
- Послідовний запуск всіх тестів
- Збір результатів
- Обробка помилок
- Детальна звітність
- Логування в файл
- Exit codes для CI/CD

## 🛠 Технології

- **Python 3.8+** - мова програмування
- **Selenium 4.x** - фреймворк для автоматизації браузера
- **WebDriver Manager** - автоматичне управління драйверами
- **Chrome/ChromeDriver** - браузер для тестування

### Чому Selenium?

✅ Підтримка всіх основних браузерів  
✅ Потужний API для взаємодії з веб-елементами  
✅ Широка спільнота та документація  
✅ Безкоштовний та open-source  
✅ Інтеграція з testing frameworks  

### Чому WebDriver Manager?

✅ Автоматичне завантаження потрібної версії драйвера  
✅ Немає потреби вручну оновлювати драйвери  
✅ Підтримка кешування  
✅ Кросплатформність  

## 📊 Приклади виводу

### Успішне виконання тесту:

```
================================================================================
Running: Google Search Automation
================================================================================
✓ WebDriver initialized successfully
✓ Navigated to https://www.google.com
✓ Search box found
✓ Search query entered: Selenium WebDriver Python
✓ Search results loaded
============================================================
First Search Result: Selenium with Python - Read the Docs
============================================================
✓ Screenshot saved: screenshots/google_search_results_20241214_123045.png
✓ Google search automation completed successfully!
```

### Звіт виконання:

```
================================================================================
TEST EXECUTION REPORT
================================================================================
Execution Time: 2024-12-14 12:30:00 - 12:35:45
Total Duration: 345.67 seconds

Total Tests: 4
Passed: 4 ✓
Failed: 0 ✗
Errors: 0 ⚠

--------------------------------------------------------------------------------
Individual Test Results:
--------------------------------------------------------------------------------

✓ Google Search Automation
  Status: PASSED
  Duration: 15.32s

✓ Form Automation
  Status: PASSED
  Duration: 12.45s

✓ Selectors Demonstration
  Status: PASSED
  Duration: 8.76s

✓ Navigation Demonstration
  Status: PASSED
  Duration: 23.14s
================================================================================
✓ ALL TESTS PASSED!
================================================================================
```

## 🐛 Усунення несправностей

### Проблема: ChromeDriver не знайдено

**Рішення:** WebDriver Manager повинен автоматично завантажити драйвер. Переконайтеся, що:
- У вас встановлено Google Chrome
- Є підключення до інтернету
- `webdriver-manager` встановлено правильно

### Проблема: Timeout помилки

**Рішення:** Збільште timeout значення в `config.py`:

```python
IMPLICIT_WAIT = 20
EXPLICIT_WAIT = 20
PAGE_LOAD_TIMEOUT = 60
```

### Проблема: Елементи не знайдено

**Рішення:** 
- Перевірте селектори (можливо, сторінка змінилася)
- Використовуйте explicit waits
- Перевірте чи завантажився JavaScript

### Проблема: Headless режим не працює

**Рішення:** Деякі тести можуть не працювати в headless режимі. Встановіть в `config.py`:

```python
BROWSER_HEADLESS = False
```

## 📝 Логування

Всі тести генерують детальні логи:

- **Console output** - виводиться в реальному часі
- **test_execution.log** - зберігається в файл (при запуску main.py)
- **Screenshots** - зберігаються в папці `screenshots/`

## 🔒 Безпека

- Не використовуйте реальні паролі в тестах
- Не commit credentials в репозиторій
- Використовуйте `.gitignore` для виключення чутливих файлів
- В production використовуйте environment variables

## 📈 Розширення функціональності

### Додавання нового тесту:

1. Створіть новий файл `my_test.py`
2. Реалізуйте функцію з логікою тесту
3. Додайте import в `main.py`
4. Додайте тест в список `tests` в `main.py`

### Використання в CI/CD:

```yaml
# .github/workflows/tests.yml
name: Run Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt
      - run: python main.py
```

## 🤝 Внесок

Якщо ви хочете покращити проєкт:

1. Fork репозиторій
2. Створіть feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit зміни (`git commit -m 'Add some AmazingFeature'`)
4. Push в branch (`git push origin feature/AmazingFeature`)
5. Відкрийте Pull Request

## 📄 Ліцензія

Цей проєкт створено в освітніх цілях для Лабораторної роботи №6.

## 👤 Автор

**ar4lin**
- GitHub: [@ar4lin](https://github.com/ar4lin)

## 🔗 Корисні посилання

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Selenium with Python](https://selenium-python.readthedocs.io/)
- [WebDriver Manager for Python](https://github.com/SergeyPirogov/webdriver_manager)
- [CSS Selectors Reference](https://www.w3schools.com/cssref/css_selectors.asp)
- [XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)

## 📞 Підтримка

Якщо у вас виникли питання або проблеми:

1. Перевірте розділ [Усунення несправностей](#усунення-несправностей)
2. Перегляньте логи виконання
3. Створіть Issue в репозиторії з детальним описом проблеми

---

**Дякуємо за використання цього проєкту! 🚀**