
# 📝 Backend API de Tareas (Django REST Framework + Simple JWT)

Este proyecto es una API RESTful de gestión de tareas

---

## 🚀 Características

- Django + DRF.
- Autenticación con **JWT (access + refresh tokens)**.
- Gestión de usuarios con el modelo de usuario por defecto de Django.
- CRUD completo de tareas.
- Configuración de CORS habilitada para pruebas de frontend.


## ⚙️ Instalación y configuración

1. **Clona el repositorio:**

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

2. **Crea un entorno virtual:**

```bash
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate    # Windows
```

3. **Instala dependencias:**

```bash
pip install -r requirements/local.txt
```

4. **Configura las variables de entorno en `.env`:**

El ejemplo de las variables del .env esta en .env-example

5. **Aplica migraciones:**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crea un superusuario:**

```bash
python manage.py createsuperuser
```

7. **Ejecuta el servidor:**

```bash
python manage.py runserver
```

---

## 🔒 Endpoints de Autenticación (Simple JWT)

| Endpoint              | Método | Descripción                      |
|----------------------|--------|----------------------------------|
| `/api/token`         | POST   | Obtener Access y Refresh Token   |
| `/api/token/refresh`  | POST   | Obtener nuevo Access Token       |
| `/api/token/verify`   | POST   | Verificar validez de un Token    |

---

## 📝 Endpoints de Tasks (CRUD)

| Endpoint              | Método   | Descripción                 | Autenticación |
|----------------------|----------|-----------------------------|--------------|
| `/api/tasks/`        | GET      | Listar tareas (paginación)  | Sí (JWT)     |
| `/api/tasks/`        | POST     | Crear nueva tarea          | Sí (JWT)     |
| `/api/tasks/<id>/`   | GET      | Obtener detalle de tarea   | Sí (JWT)     |
| `/api/tasks/<id>/`   | PUT/PATCH| Actualizar tarea           | Sí (JWT)     |
| `/api/tasks/<id>/`   | DELETE   | Eliminar tarea             | Sí (JWT)     |

---

## ✅ Tecnologías utilizadas

- Python 3.10.x
- Django 5.x
- Django REST Framework
- Simple JWT (djangorestframework-simplejwt)
- PostgreSQL (u otra DB configurable por `.env`)
- Debug Toolbar (para entorno local)

