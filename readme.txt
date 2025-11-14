TRPO_WEB/                          # корень проекта
│
├── venv/                         # виртуальное окружение
│   ├── Scripts/                  
│   ├── Lib/
│   └── pyvenv.cfg
│
├── manage.py                      # утилита управления проектом
│
├── culinary_compass/              # конфигурация проекта (главный пакет)
│   ├── __init__.py
│   ├── settings.py                # НАСТРОЙКИ: приложения, БД, шаблоны, статика
│   ├── urls.py                    # МАРШРУТЫ: подключает urls из приложений
│   ├── asgi.py
│   └── wsgi.py
│
├── recipes/                       # ПРИЛОЖЕНИЕ: основная логика рецептов
│   ├── __init__.py
│   ├── admin.py                   # РЕГИСТРАЦИЯ МОДЕЛЕЙ в админке
│   ├── apps.py                    # конфигурация приложения
│   ├── models.py                  # МОДЕЛИ: Recipe, Ingredient
│   ├── views.py                   # ПРЕДСТАВЛЕНИЯ: home, search, all_recipes, recipe_detail
│   ├── urls.py                    # МАРШРУТЫ: /, /search/, /recipes/, /recipe/<id>/
│   ├── forms.py                   # ФОРМЫ: IngredientSearchForm
│   ├── tests.py
│   └── migrations/                # МИГРАЦИИ БД (создаются автоматически)
│       └── __init__.py
│
├── favorites/                     # ПРИЛОЖЕНИЕ: избранные рецепты пользователей
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                  # МОДЕЛЬ: Favorite (связь User-Recipe)
│   ├── views.py                   # ПРЕДСТАВЛЕНИЯ: favorite_recipes, add/remove
│   ├── urls.py                    # МАРШРУТЫ: /favorites/, /favorites/add/<id>/
│   ├── tests.py
│   └── migrations/
│       └── __init__.py
│
├── users/                         # ПРИЛОЖЕНИЕ: регистрация пользователей
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── views.py                   # ПРЕДСТАВЛЕНИЕ: register
│   ├── urls.py                    # МАРШРУТЫ: /users/register/
│   ├── forms.py                   # ФОРМА: CustomUserCreationForm
│   ├── tests.py
│   └── migrations/
│       └── __init__.py
│
├── templates/                     # ГЛОБАЛЬНЫЕ ШАБЛОНЫ (указывается в settings.py)
│   ├── base.html                  # БАЗОВЫЙ ШАБЛОН: навигация, стили
│   ├── recipes/                   # ШАБЛОНЫ для приложения recipes
│   │   ├── home.html              # главная страница
│   │   ├── search.html            # форма поиска по ингредиентам
│   │   ├── search_results.html    # результаты поиска
│   │   ├── all_recipes.html       # все рецепты
│   │   └── recipe_detail.html     # детальная страница рецепта
│   ├── favorites/                 # ШАБЛОНЫ для приложения favorites
│   │   └── favorite_recipes.html  # избранные рецепты пользователя
│   └── users/                     # ШАБЛОНЫ для приложения users
│       ├── register.html          # регистрация
│       └── login.html             # вход (или в registration/login.html)
│
├── static/                        # СТАТИЧЕСКИЕ ФАЙЛЫ (CSS, JS, изображения)
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
│