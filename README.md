# Administración-de-archivos-CSV
Desarrollo de API que permite Listar, Descargar, Añadir y Eliminar un archivo csv. 
Adicionalmente permite consultar el contenido de un archivo CSV (Cargado mediante el API) yrealizar filtros, paginacion & ordenamiento

# Configuración

1. Instalar virtualenv ``` pip install virtualenv```
2. Instalar todas las dependencias  ```pip install -r requirements.txt```
3. Credeciales 
    > usuario : hazelpg
    > contraseña : hazelpg
    > token : 657c489147fa0aa15d1d77cc40ea84e8560df7fb   
4. Correr el servidor  ```python manage.py runserver```

# URL API

- lista los archivos creados
```/api/file/ ```
- Ejemplo 
```http://127.0.0.1:8000/api/file/```
Lista achivos pasandole un pk
```api/file/(?P<pk>[^/.]+)/```
Ejemplo
```http://127.0.0.1:8000/api/file/9/```

Detalla el contenido de un archivo csv pansando la pk del registro
```api/file/detail/(?P<pk>\d+)```
Ejemplo
```http://127.0.0.1:8000/api/file/detail/10```

Filtra por cualquier parametro
```api/file/detail/(?P<pk>\d+)?search=```
Ejemplo
```http://127.0.0.1:8000/api/file/detail/10?search=gonzales```
Ordenar por parametros
```api/file/detail/(?P<pk>\d+)?order=```
Ejemplo
```http://127.0.0.1:8000/api/file/detail/10?order=edad```

Ordenar por parametros y de forma desendente o ascendente 
```api/file/detail/(?P<pk>\d+)?order=&desc=```
Ejemplo
```http://127.0.0.1:8000/api/file/detail/10?order=apellidos&desc=True``` 
 
Paginacion
```/api/file/?page=```
Ejemplo
```http://127.0.0.1:8000/api/file/?page=2```
