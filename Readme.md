Entorno virtual

```
python -m venv venv
```

Instalar Django

```
py -m pip install Django
```

Ejecutar Server

```
python manage.py runserver
```

Crear Migraciones

```
python manage.py makemigrations
```

Aplicar la migración

```
python manage.py migrate
```

Crear un super admin

```
python manage.py createsuperuser
```

Crear App "Productos"

```
python manage.py startapp products
```

Shell de Django

```
python manage.py shell
```

Manejo de imagenes

```
pip install Pillow
```

Respaldar información

```
python manage.py dumpdata products.product --format=json --indent=4 > products/fixtures/products.json
```

Importar data de respaldo

```
python manage.py loaddata products.json
```
