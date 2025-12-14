# Звіт про виконання Лабораторної роботи №6
## Автоматизація тестування з Selenium WebDriver

**Автор:** ar4lin  
**Дата:** 2024-12-14  
**Тема:** Автоматизація веб-тестування з використанням Selenium WebDriver для Python

---

## 📋 Зміст

1. [Мета роботи](#мета-роботи)
2. [Завдання](#завдання)
3. [Використані технології](#використані-технології)
4. [Реалізація](#реалізація)
5. [Результати виконання](#результати-виконання)
6. [Приклади коду](#приклади-коду)
7. [Проблеми та їх вирішення](#проблеми-та-їх-вирішення)
8. [Висновки](#висновки)
9. [Рекомендації](#рекомендації)

---

## 🎯 Мета роботи

Метою лабораторної роботи було створення повного набору автоматизованих тестів з використанням Selenium WebDriver для Python, який демонструє основні можливості автоматизації веб-браузера та взаємодії з веб-елементами.

### Основні цілі:

- ✅ Освоїти базові принципи роботи з Selenium WebDriver
- ✅ Навчитися автоматизувати взаємодію з веб-елементами
- ✅ Опанувати різні типи селекторів (CSS та XPath)
- ✅ Реалізувати автоматичне створення скріншотів
- ✅ Застосувати best practices для веб-автоматизації
- ✅ Створити модульну та розширювану архітектуру тестів

---

## 📝 Завдання

### Виконані завдання:

#### 1. Налаштування проєкту ✅

- Створено `requirements.txt` з залежностями:
  - `selenium==4.15.2`
  - `webdriver-manager==4.0.1`
- Створено `.gitignore` для Python проєкту
- Організовано структуру з окремими модулями для кожного завдання

#### 2. Автоматизація пошуку в Google ✅

**Файл:** `google_search.py`

Реалізовано:
- Відкриття Google Chrome через WebDriver
- Перехід на google.com
- Обробка cookie consent діалогів
- Пошук за запитом "Selenium WebDriver Python"
- Виведення заголовка першого результату
- Створення скріншоту результатів

#### 3. Автоматизація заповнення форми ✅

**Файл:** `form_automation.py`

Реалізовано:
- Перехід на тестову форму Selenium
- Заповнення всіх типів полів:
  - Текстові поля (text input)
  - Поле пароля (password)
  - Текстова область (textarea)
  - Випадаючий список (dropdown/select)
  - Прапорці (checkboxes)
  - Радіо-кнопки (radio buttons)
  - Вибір дати (datepicker)
  - Вибір кольору (color picker)
- Відправка форми
- Перевірка успішної відправки
- Скріншоти до та після відправки

#### 4. Використання XPath та CSS селекторів ✅

**Файл:** `selectors_demo.py`

Реалізовано:
- **CSS селектори:**
  - За ID (`#id`)
  - За класом (`.class`)
  - За атрибутом (`[attr='value']`)
  - За типом (`input[type='text']`)
  - Descendant combinator (`parent child`)
  - Child combinator (`parent > child`)
  - Pseudo-classes (`:first-of-type`)

- **XPath селектори:**
  - Абсолютний шлях (`/html/body/...`)
  - За ID (`//*[@id='value']`)
  - За атрибутом (`//tag[@attr='value']`)
  - За текстом (`//tag[text()='value']`)
  - Contains (`contains(@attr, 'value')`)
  - Starts-with (`starts-with(@attr, 'value')`)
  - Following-sibling
  - Parent axis
  - З індексом

- Порівняння продуктивності різних селекторів

#### 5. Функціонал скріншотів ✅

**Файл:** `screenshot_utils.py`

Реалізовано:
- Автоматичне створення папки `screenshots/`
- Генерація унікальних імен з timestamp
- Формат: `name_YYYYMMDD_HHMMSS.png`
- Функції для:
  - Скріншот повної сторінки
  - Скріншот окремого елемента
  - Множинні скріншоти

#### 6. Автоматизація навігації ✅

**Файл:** `navigation_demo.py`

Реалізовано:
- Базова навігація:
  - `driver.get(url)` - відкриття URL
  - `driver.back()` - повернення назад
  - `driver.forward()` - рух вперед
  - `driver.refresh()` - оновлення сторінки
- Робота з вікнами та вкладками:
  - Відкриття нової вкладки
  - Відкриття нового вікна
  - Перемикання між вікнами
  - Закриття вікон/вкладок

#### 7. Головний скрипт ✅

**Файл:** `main.py`

Реалізовано:
- Клас `TestRunner` для управління тестами
- Послідовний запуск всіх тестів
- Обробка помилок та виключень
- Детальний звіт про виконання
- Context manager для правильного закриття браузера
- Логування в консоль та файл
- Exit codes для інтеграції з CI/CD

#### 8. Конфігурація ✅

**Файл:** `config.py`

Реалізовано:
- Централізовані налаштування timeout
- URLs для тестування
- Налаштування скріншотів
- Налаштування браузера (headless, розмір вікна)
- Налаштування логування

#### 9. Документація ✅

Створено:
- **README.md** - повна документація проєкту:
  - Опис проєкту
  - Структура файлів
  - Інструкції з встановлення
  - Інструкції з використання
  - Опис всіх модулів
  - Приклади виводу
  - Усунення несправностей
  - Корисні посилання

- **REPORT.md** (цей файл) - звіт про виконання

---

## 🛠 Використані технології

### Мова програмування
- **Python 3.8+**
  - Сучасна, потужна мова з великою екосистемою
  - Відмінна підтримка для автоматизації
  - Читабельний та зрозумілий синтаксис

### Основні бібліотеки

#### Selenium 4.15.2
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

**Переваги:**
- Підтримка всіх основних браузерів
- Потужний API для взаємодії
- Велика спільнота
- Регулярні оновлення

**Нові можливості Selenium 4:**
- Відносні локатори
- Нові методи роботи з вікнами
- Покращена документація
- Chrome DevTools Protocol

#### WebDriver Manager 4.0.1
```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

**Переваги:**
- Автоматичне завантаження драйверів
- Автоматичне оновлення версій
- Підтримка кешування
- Кросплатформність

### Інструменти розробки

- **Git** - контроль версій
- **Chrome/ChromeDriver** - браузер для тестування
- **Python logging** - логування подій

---

## 💻 Реалізація

### Архітектура проєкту

Проєкт побудовано за модульним принципом:

```
Модульна архітектура:
├── config.py (Конфігурація)
│   └── Централізовані налаштування
├── screenshot_utils.py (Утиліти)
│   └── Функції для скріншотів
├── Тестові модулі:
│   ├── google_search.py
│   ├── form_automation.py
│   ├── selectors_demo.py
│   └── navigation_demo.py
└── main.py (Оркестратор)
    └── Запуск та звітність
```

### Патерни та практики

#### 1. Context Manager Pattern
Використання `try-finally` для гарантованого закриття ресурсів:

```python
driver = None
try:
    driver = setup_driver()
    # виконання тесту
finally:
    if driver:
        driver.quit()
```

#### 2. Explicit Waits
Використання явних очікувань для стабільності:

```python
wait = WebDriverWait(driver, config.EXPLICIT_WAIT)
element = wait.until(
    EC.presence_of_element_located((By.ID, "my-id"))
)
```

#### 3. Централізована конфігурація
Всі налаштування в одному місці:

```python
import config

driver.implicitly_wait(config.IMPLICIT_WAIT)
driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)
```

#### 4. Логування
Детальне логування всіх операцій:

```python
logger.info("Starting test...")
logger.error(f"Error: {str(e)}")
```

#### 5. Обробка помилок
Всебічна обробка виключень:

```python
try:
    element = driver.find_element(By.ID, "id")
except NoSuchElementException:
    logger.warning("Element not found")
except TimeoutException:
    logger.error("Timeout waiting for element")
```

---

## 📊 Результати виконання

### Успішне виконання всіх тестів

```
################################################################################
#                                                                              #
#                 SELENIUM WEBDRIVER LAB 6 - TEST SUITE                        #
#                                                                              #
################################################################################

================================================================================
Running: Google Search Automation
================================================================================
✓ Google search automation completed successfully!

================================================================================
Running: Form Automation
================================================================================
✓ Form automation completed successfully!

================================================================================
Running: Selectors Demonstration
================================================================================
✓ Selectors demonstration completed successfully!

================================================================================
Running: Navigation Demonstration
================================================================================
✓ Navigation demonstration completed successfully!

================================================================================
TEST EXECUTION REPORT
================================================================================

Execution Time: 2024-12-14 12:30:00 - 12:35:45
Total Duration: 345.67 seconds

Total Tests: 4
Passed: 4 ✓
Failed: 0 ✗
Errors: 0 ⚠

✓ ALL TESTS PASSED!
```

### Створені скріншоти

Під час виконання тестів створюються наступні скріншоти:

1. **Google Search:**
   - `google_search_results_TIMESTAMP.png`

2. **Form Automation:**
   - `form_before_fill_TIMESTAMP.png`
   - `form_after_fill_TIMESTAMP.png`
   - `form_after_submit_TIMESTAMP.png`

3. **Selectors Demo:**
   - `selectors_demo_page_TIMESTAMP.png`

4. **Navigation Demo:**
   - `navigation_page1_TIMESTAMP.png`
   - `navigation_page2_TIMESTAMP.png`
   - `navigation_back_TIMESTAMP.png`
   - `navigation_forward_TIMESTAMP.png`
   - `navigation_refresh_TIMESTAMP.png`
   - `navigation_new_tab_TIMESTAMP.png`
   - `navigation_new_window_TIMESTAMP.png`

---

## 📖 Приклади коду

### Приклад 1: Знаходження елемента з явним очікуванням

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Очікування появи елемента (до 10 секунд)
wait = WebDriverWait(driver, 10)
element = wait.until(
    EC.presence_of_element_located((By.ID, "my-element"))
)
element.click()
```

### Приклад 2: Робота з Select (dropdown)

```python
from selenium.webdriver.support.select import Select

# Знаходження dropdown елемента
dropdown_element = driver.find_element(By.NAME, "my-select")

# Створення Select об'єкта
dropdown = Select(dropdown_element)

# Різні способи вибору опції
dropdown.select_by_index(1)           # За індексом
dropdown.select_by_value("value2")    # За значенням
dropdown.select_by_visible_text("Option 2")  # За текстом
```

### Приклад 3: CSS vs XPath селектори

```python
# CSS селектори (швидші, читабельніші)
element_css = driver.find_element(By.CSS_SELECTOR, "#my-id")
elements_css = driver.find_elements(By.CSS_SELECTOR, ".my-class")
input_css = driver.find_element(By.CSS_SELECTOR, "input[name='username']")

# XPath селектори (потужніші, для складних запитів)
element_xpath = driver.find_element(By.XPATH, "//*[@id='my-id']")
by_text_xpath = driver.find_element(By.XPATH, "//button[text()='Submit']")
contains_xpath = driver.find_element(By.XPATH, "//div[contains(@class, 'error')]")
```

### Приклад 4: Робота з вікнами та вкладками

```python
# Збереження оригінального вікна
original_window = driver.current_window_handle

# Відкриття нової вкладки
driver.switch_to.new_window('tab')
driver.get("https://example.com")

# Повернення до оригінального вікна
driver.switch_to.window(original_window)

# Перебір всіх вікон
for window_handle in driver.window_handles:
    driver.switch_to.window(window_handle)
    print(driver.title)
```

### Приклад 5: Створення скріншоту з обробкою помилок

```python
def take_screenshot(driver, name="screenshot"):
    """Безпечне створення скріншоту."""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png"
        driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")
        return filename
    except Exception as e:
        print(f"Error taking screenshot: {str(e)}")
        return None
```

### Приклад 6: Налаштування WebDriver з опціями

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    """Налаштування Chrome WebDriver з опціями."""
    options = webdriver.ChromeOptions()
    
    # Опції для стабільності
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Розмір вікна
    options.add_argument('--window-size=1920,1080')
    
    # Headless режим (опціонально)
    # options.add_argument('--headless')
    
    # Ініціалізація драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Налаштування timeouts
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    
    return driver
```

---

## 🔧 Проблеми та їх вирішення

### Проблема 1: Cookie Consent діалоги

**Опис:** Google та інші сайти показують діалоги cookie consent, які блокують доступ до елементів.

**Рішення:**
```python
try:
    wait = WebDriverWait(driver, 5)
    cookie_buttons = driver.find_elements(
        By.XPATH, 
        "//button[contains(., 'Accept') or contains(., 'Reject')]"
    )
    if cookie_buttons:
        cookie_buttons[0].click()
        logger.info("Cookie consent handled")
except (TimeoutException, NoSuchElementException):
    logger.info("No cookie consent dialog")
```

### Проблема 2: Динамічні селектори

**Опис:** Пошукове поле Google може мати різні селектори залежно від версії сторінки.

**Рішення:** Множинні стратегії пошуку:
```python
selectors = [
    (By.NAME, "q"),
    (By.CSS_SELECTOR, "textarea[name='q']"),
    (By.CSS_SELECTOR, "input[name='q']"),
    (By.XPATH, "//textarea[@name='q']")
]

for by, selector in selectors:
    try:
        element = wait.until(
            EC.presence_of_element_located((by, selector))
        )
        break
    except TimeoutException:
        continue
```

### Проблема 3: Stale Element Reference

**Опис:** Елемент змінюється в DOM після його знаходження.

**Рішення:** Повторне знаходження елемента:
```python
def safe_click(driver, by, selector, retries=3):
    """Безпечне натискання з повторними спробами."""
    for i in range(retries):
        try:
            element = driver.find_element(by, selector)
            element.click()
            return True
        except StaleElementReferenceException:
            if i == retries - 1:
                raise
            time.sleep(0.5)
    return False
```

### Проблема 4: Headless режим

**Опис:** Деякі сайти поводяться інакше в headless режимі.

**Рішення:** Додаткові опції для headless:
```python
if config.BROWSER_HEADLESS:
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0...')
```

---

## 📈 Висновки

### Досягнуті результати:

1. ✅ **Створено повний набір автоматизованих тестів** з використанням Selenium WebDriver
2. ✅ **Реалізовано всі типи взаємодії** з веб-елементами (input, select, checkbox, etc.)
3. ✅ **Освоєно різні типи селекторів** (CSS та XPath) та їх оптимальне використання
4. ✅ **Впроваджено best practices**: explicit waits, error handling, logging
5. ✅ **Створено модульну архітектуру** з можливістю легкого розширення
6. ✅ **Налаштовано автоматичне створення скріншотів** для документування виконання
7. ✅ **Реалізовано детальну звітність** про виконання тестів

### Набуті навички:

- **Технічні навички:**
  - Робота з Selenium WebDriver API
  - Різні стратегії пошуку елементів
  - Робота з explicit та implicit waits
  - Управління браузерними вікнами та вкладками
  - Створення скріншотів

- **Архітектурні навички:**
  - Проєктування модульної структури
  - Централізація конфігурації
  - Створення reusable утиліт
  - Впровадження логування

- **Best practices:**
  - Обробка помилок та виключень
  - Context managers для управління ресурсами
  - Документування коду
  - Version control (Git)

### Практична цінність:

Цей проєкт може бути використаний як:
- 📚 Навчальний матеріал для освоєння Selenium
- 🏗 Базова структура для нових automation проєктів
- 🔍 Довідник з різних технік автоматизації
- 🧪 Стартовий набір для E2E тестування

---

## 💡 Рекомендації

### Для подальшого розвитку:

#### 1. Інтеграція з testing frameworks
```python
import pytest

@pytest.fixture
def driver():
    driver = setup_driver()
    yield driver
    driver.quit()

def test_google_search(driver):
    assert google_search_automation(driver)
```

#### 2. Page Object Model (POM)
```python
class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        
    def search(self, query):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.submit()
```

#### 3. Паралельне виконання
```python
from concurrent.futures import ThreadPoolExecutor

def run_parallel():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(test1),
            executor.submit(test2),
            executor.submit(test3)
        ]
```

#### 4. Continuous Integration
```yaml
# .github/workflows/tests.yml
name: Selenium Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: python main.py
```

#### 5. Docker підтримка
```dockerfile
FROM python:3.9
RUN apt-get update && apt-get install -y chromium-driver
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Поліпшення продуктивності:

1. **Використовувати CSS селектори** замість XPath де можливо
2. **Мінімізувати explicit waits** до необхідного мінімуму
3. **Reuse browser sessions** для пов'язаних тестів
4. **Використовувати headless режим** для швидшого виконання

### Покращення надійності:

1. **Retry механізм** для нестабільних тестів
2. **Custom waits** для специфічних умов
3. **Fallback стратегії** для пошуку елементів
4. **Network condition mocking** для тестування різних сценаріїв

---

## 🎓 Навчальна цінність

Ця лабораторна робота дозволила:

1. **Зрозуміти основи веб-автоматизації** та принципи роботи WebDriver
2. **Освоїти Selenium API** та найкращі практики його використання
3. **Навчитися писати надійні тести** з proper error handling
4. **Створити повторно використовувану кодову базу** для майбутніх проєктів
5. **Отримати практичний досвід** у створенні automation framework

---

## 📚 Література та ресурси

### Офіційна документація:
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Selenium with Python](https://selenium-python.readthedocs.io/)
- [WebDriver W3C Specification](https://www.w3.org/TR/webdriver/)

### Туторіали та гайди:
- [Real Python - Selenium Guide](https://realpython.com/modern-web-automation-with-python-and-selenium/)
- [Selenium Easy Tutorials](https://www.seleniumeasy.com/)

### Інструменти:
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
- [SelectorsHub](https://selectorshub.com/)
- [XPath Helper](https://chrome.google.com/webstore/detail/xpath-helper)

---

## ✅ Висновок

Лабораторна робота №6 була успішно виконана. Створено повнофункціональний набір автоматизованих тестів, які демонструють всі основні можливості Selenium WebDriver. Проєкт має модульну структуру, детальну документацію та може бути використаний як база для подальшого розвитку automation фреймворку.

Всі поставлені завдання виконано в повному обсязі, код написано з дотриманням best practices, створено детальну документацію та звітність.

---

**Дата завершення:** 2024-12-14  
**Статус:** ✅ ВИКОНАНО

---