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

lista los archivos creados
```/api/file/ ```

Lista achivos pasandole un pk
```api/file/(?P<pk>[^/.]+)/```

Detalla el contenido de un archivo csv pansando la pk del registro
```api/file/detail/(?P<pk>\d+)```
  
Filtra por cualquier parametro
```api/file/detail/(?P<pk>\d+)?search=```

Ordenar por parametros
```api/file/detail/(?P<pk>\d+)?order=apellidos```
```api/file/detail/(?P<pk>\d+)?order=nombre```
```api/file/detail/(?P<pk>\d+)?order=edad```

Ordenar por parametros y de forma desendente o ascendente 
```api/file/detail/(?P<pk>\d+)?order=apellidos&desc=True ```
```api/file/detail/(?P<pk>\d+)?order=nombre&desc=True ```
```api/file/detail/(?P<pk>\d+)?order=edad&desc=True ```
  
  
