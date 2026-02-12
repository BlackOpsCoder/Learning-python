def desire_grade(grade, grade_needed, assignment_worth, assigment_weight, total_points, earned_points):
    category_grade = (earned_points/total_points) * assignment_weight
    grade -= category_grade
    result = (((grade_needed - grade) / assignment_weight) * (total_points + assignment_worth)) - earned_points
    return round(result, 2)


def assigment_affect(grade, assignment_total_points, assignment_earned_points, assignment_weight, total_points, earned_points):
    category_grade = (earned_points/total_points) * assignment_weight
    grade -= category_grade
    total_points += assignment_total_points
    earned_points += assignment_earned_points
    category_grade = (earned_points/total_points) * assignment_weight
    grade += category_grade
    return round(grade, 2)
    
   

print("""Welcome to grade system app:
      1 - Assignment Affect
      2 - Desire Grade
      """)
user_input = int(input("Enter number: "))

if user_input == 1:
    grade = float(input("What's your grade (%): "))
    total_points = float(input("Total points in assignment category: "))
    earned_points = float(input("Earned points in assignment category: "))
    assignment_weight = float(input("Weight of assignment (%): "))
    assignment_total_points = float(input("Assigment worth: "))
    assignment_earned_points = float(input("Assignment points earned: "))
    print(assigment_affect(grade, assignment_total_points, assignment_earned_points, assignment_weight, total_points, earned_points))

if user_input == 2:
    grade = float(input("What's your grade (%): "))
    grade_needed = float(input("Your desired grade (%): "))
    assignment_worth = float(input("Assignment points: "))
    assignment_weight = float(input("Weight of assignment category (%): "))
    total_points = float(input("Total points in category: "))
    earned_points = float(input("Earned points in category: "))
    print(desire_grade(grade, grade_needed, assignment_worth, assignment_weight, total_points, earned_points))

    
 