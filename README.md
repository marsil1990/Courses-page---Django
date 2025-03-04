🌍 Plataforma de Cursos - En Construcción

📌 Descripción (Español)

Esta es una plataforma educativa donde los profesores pueden registrarse, crear cursos con lecciones y ejercicios, y los estudiantes pueden inscribirse, completar ejercicios y finalizar los cursos.

🚧 El proyecto está en desarrollo. Algunas funcionalidades pueden no estar completamente implementadas.

🌍 Courses Platform - Under Construction

📌 Description (English)

This is an educational platform where teachers can register, create courses with lessons and exercises, and students can enroll, complete exercises, and finish courses.

🚧 This project is still in development. Some features may not be fully implemented.

📥 Instalación / Installation

Clonar el repositorio / Clone the repository:

git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

Crear un entorno virtual / Create a virtual environment:

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

Instalar dependencias / Install dependencies:

pip install -r requirements.txt

Configurar variables de entorno / Configure environment variables:

Renombra el archivo .env.example a .env y configura los valores necesarios.

Realizar migraciones / Run migrations:

python manage.py migrate

Ejecutar el servidor / Run the server:

python manage.py runserver

🛠 Uso / Usage

Accede al panel de administración / Access the admin panel:

http://127.0.0.1:8000/admin/

Registra un profesor y crea cursos / Register a teacher and create courses

Registra un estudiante y realiza los ejercicios / Register a student and complete exercises

⚠️ Notas / Notes

Este proyecto usa SQLite por defecto. Para cambiar a PostgreSQL o MySQL, edita settings.py.

Si tienes problemas con dependencias, revisa requirements.txt y usa versiones compatibles.

🛠 Tecnologías Usadas / Technologies Used

Django - Backend framework

Bootstrap - Frontend framework

SQLite - Base de datos por defecto

🏗 Estado del Proyecto / Project Status

🚧 Este proyecto está en desarrollo y nuevas funcionalidades se agregarán pronto.
🚧 This project is under development, and new features will be added soon.

📩 Contribuir / Contribute

Si quieres contribuir, abre un issue o envía un pull request.
If you want to contribute, open an issue or submit a pull request.

