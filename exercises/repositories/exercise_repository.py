from exercises.models import ExerciseMultipleOption, Exercise_passed, Exercise_options
class ExerciseRepository:
    @staticmethod
    def exercises_completed_by_CustomUser(user, curso):
        query ="""SELECT ep.key, COUNT(ep.key) as total_exercise
                FROM exercises_exercise_passed ep
                INNER JOIN exercises_exercisemultipleoption ej ON ep.exercise_id = ej.id
                INNER JOIN lessons_lesson l ON l.id = ej.lessons_id
                WHERE l.course_id = %s and ep.CustomUser_id = %s"""
        result = Exercise_passed.objects.raw(query, [curso.id, user.ci])
        total = result[0].total_exercise 
        if result:
           pass
        else:
          total = 0
        return total
    
    @staticmethod
    def get_exercises_completed_by_CustomUser(CustomUser_ci):
        query ="""SELECT ep.key
                FROM exercises_exercise_passed ep
                WHERE ep.CustomUser_id = %s"""
        result = Exercise_passed.objects.raw(query, [CustomUser_ci])
        exerciseMultioptionsPassed = []
        for e in result:
            exerciseMultioptionsPassed.append(e.exercise)
       # print(exerciseMultioptionsPassed)
        return exerciseMultioptionsPassed
    def get_exercise(id):
       exercise =  ExerciseMultipleOption.objects.get(id=id)
       return exercise