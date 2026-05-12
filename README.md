# Tienda Flask

Pequeña aplicación Flask para gestionar productos.

Prerequisitos
- Python 3.8+
- MySQL (o ajustar `SQLALCHEMY_DATABASE_URI` en `config.py`)

Instalación rápida
1. Crear y activar entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Crear base de datos MySQL (ajusta usuario/contraseña si es necesario):

```bash
mysql -u root -p -e "CREATE DATABASE tienda_flask;"
```

4. Crear un fichero `.env` a partir de `.env.example` y editar la URI si hace falta.

Ejecución

```bash
python3 app.py
```

Notas
- `config.py` actualmente usa una URI en duro: edítala o cambia a lectura desde variables de entorno según prefieras.
- Si usas otro motor (SQLite, Postgres), actualiza `SQLALCHEMY_DATABASE_URI` en `config.py`.
