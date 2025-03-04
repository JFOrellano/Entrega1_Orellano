﻿# FinalProyect_Orellano_Reggiardo

El proyecto consta de un blog de la FIFA en la que se pueden agregar federaciones, equipos y jugadores cada uno mediante su propio formulario alojando los datos en la base de datos.

En la pagina home se encuentra un buscador de federaciones y arriba a la derecha el ingreso a las diferentes secciones especializadas en cada conjunto de datos que se puede guardar.

Al clickear en alguna de las opciones antes mencionadas se ingresa a una pagina donde muestra todas las instancias existentes de federaciones, equipos o jugadores dependiendo lo seleccionado.

Para hacer los html se emplea herencia en los templates partiendo siempre de index.html alojado en la aplicación home.

# Instrucciones para ejecutar este proyecto

- Crear Directorio del proyecto FinalProyect_Orellano_Reggiardo

### 1. Abrir Git Bash para `Windows` o una terminal para `Linux/Unix`.

### 2. Crear directorio donde se va a alojar el proyecto
En este caso en particular se alojaría en la carpeta final_proyect dentro de Documents
```bash
cd
mkdir -p Documents/final_proyect
cd Documents/final_proyect
ls 
```

- Clonar el proyecto
```bash
git clone https://github.com/JFOrellano/FinalProyect_Orellano_Reggiardo.git

cd FinalProyect_Orellano_Reggiardo
```

### 3. Crear y activar entorno virtual
(Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

(Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

### 5. Navegamos hacia la carpeta del proyecto `final_proyect`
```bash
cd my_blog
```

### 6. Se crean las migraciones que son una "plantilla" para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py makemigrations
```

### 7. Se ejecuta la migración para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py migrate
```

### 8. Se crea el super usuario para nuestro proyecto de Django, **Solo si no se ha creado**
```bash
python manage.py createsuperuser
```
Ingrese `Username`, `Email address` y `Password` 

### 9. Se levanta el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto `http://127.0.0.1:8000/`
```bash
python manage.py runserver
```
