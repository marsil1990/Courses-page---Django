from .models import Course

class CourseFactory:
    @staticmethod
    def create_course(name, subject, difficulty="Easy", description=None, img=None):
        """
        Factory Method para crear instancias del modelo Course con reglas de negocio específicas.
        """
        # Validación de dificultad
        if difficulty not in ["Easy", "Medium", "Difficult"]:
            raise ValueError("Difficulty must be 'Easy', 'Medium', or 'Difficult'.")

        # Valor predeterminado para la descripción si no se proporciona
        if description is None:
            description = f"{name} - A course on {subject}."

        # Crear y devolver la instancia
        course = Course(
            name=name,
            subject=subject,
            difficulty=difficulty,
            descrption=description,
            img=img,
        )
        # Guardar en la base de datos
        course.save()
        return course
