It is a web page where courses with lessons and exercises are created. Students can register and purchase courses via PayPal.
This project is still under development.
Steps to get the application running:
- git clone https://github.com/marsil1990/Courses-page---Django.git
- cd Courses-page---Django
- python -m venv myenv
(windows)
- myenv\Scripts\activate
(linux or Mac)
- source myenv/bin/activate 
- pip install -r requirements.txt

Add the .env file with the following environment variables, replacing the placeholder values with the necessary information:

SECRET_KEY=''
DEBUG=True
ALLOWED_HOSTS=''
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_password
EMAIL_USE_TLS=True
PAYPAL_RECEIVER_EMAIL=''
PAYPAL_TEST=True
PAYPAL_BUY_BUTTON_IMAGE=''

- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

-----------------------------------------------------------------------------------------------------------------------------------------------------------
Es una pagina web, donde se crean cursos, con lecciones y ejercicios. Los estudiantes se pueden registrar y comprar los cursos mediante paypal.
Este proyecto aún esta en creación.
Pasos para que la aplicación funcione:
- git clone https://github.com/marsil1990/Courses-page---Django.git
- cd Courses-page---Django
- python -m venv myenv
(windows)
- myenv\Scripts\activate
(linux o Mac)
- source myenv/bin/activate 
- source myenv/bin/activate
- pip install -r requirements.txt
Agrega el archivo .env con los siguientes variables de ambiente y con los datos que sean necesarios en lugar de la comillas:
SECRET_KEY=''
DEBUG=True
ALLOWED_HOSTS= ""
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña
EMAIL_USE_TLS=True
PAYPAL_RECEIVER_EMAIL=""
PAYPAL_TEST=True
PAYPAL_BUY_BUTTON_IMAGE=""
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver



