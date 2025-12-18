# FastAPI Products CRUD

Proyecto base **productivo** de CRUD de productos usando:

- **FastAPI**
- **Jinja2**
- **TailwindCSS**
- **MySQL 8**
- **SQLAlchemy**
- **Docker + Docker Compose**

Incluye manejo correcto de:
- Inicialización de MySQL en Docker
- Race conditions
- Formularios (`python-multipart`)
- Autenticación MySQL moderna (`cryptography`)

---

## 📦 Stack Tecnológico

| Componente | Tecnología |
|----------|-----------|
| Backend | FastAPI |
| Templates | Jinja2 |
| UI | TailwindCSS (CDN) |
| ORM | SQLAlchemy |
| DB | MySQL 8 |
| Driver DB | PyMySQL |
| Contenedores | Docker |
| Orquestación | Docker Compose |

---

## 📁 Estructura del Proyecto

```
fastapi-products/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── templates/
│       ├── base.html
│       ├── products.html
│       └── product_form.html
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Variables de Entorno

Archivo `.env`:

```
DATABASE_URL=mysql+pymysql://appuser:apppass@db:3306/products_db
```

---

## 🐳 Comandos Docker

### Construir y levantar

```
docker compose up --build
```

### Detener contenedores

```
docker compose down
```

### Reset total (borra datos)

```
docker compose down -v
```

### Ver logs

```
docker compose logs -f
```

---

## 🌐 Acceso

```
http://localhost:8000
```

---

## 🧾 Funcionalidad

- Listar productos
- Crear producto
- Editar producto
- Eliminar producto
- Persistencia en MySQL

---

## 📋 Dependencias Clave

```
python-multipart
cryptography
```

---

## 🚀 Extensiones Futuras

- Alembic
- Auth
- API REST
- CI/CD
- Deploy Cloud
