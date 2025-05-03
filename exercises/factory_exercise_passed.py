from .models import Exercise_passed
class ExercisePassedFactory:
    @staticmethod
    def create_exercise_passed(exercise, student):
        try:
            ex = Exercise_passed.objects.create(exercise = exercise, CustomUser = student)
            return ex
        except Exception as e:
           print(f"Ocurrió un error inesperado: {e}")
           