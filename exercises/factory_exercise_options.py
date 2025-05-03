from .models import Exercise_options
class ExerciseOptionsFactory:
    @staticmethod
    def create_exercise_options(exercise, option_text):
        try: 
            ex = Exercise_options.objects.create(exerciseMultipleOption=exercise, answer_option=option_text)
            return ex
        except Exception as e:
           print(f"Ocurrió un error inesperado: {e}")
            
        
        