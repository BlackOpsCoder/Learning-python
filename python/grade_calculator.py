category_list = []
weights_list = []
total_points_list = []
earned_points_list = []
categories = int(input("How many categories do you have: "))
for i in range(categories):
    total_points = float(input(f"Category {i+1}: Total points: "))
    earned_points = float(input(f"Category {i+1}: Earned points: "))
    weight = float(input("Category weight (%): "))
    category_list.append((earned_points / total_points) * weight)
    weights_list.append(weight)
    total_points_list.append(total_points)
    earned_points_list.append(earned_points)


grade_needed = float(input("Your desired grade (%): "))
assignment_worth = float(input("Assignment points: "))
category = int(input("Which category # (above): "))
total_points = total_points_list[category - 1]
earned_points = earned_points_list[category - 1]
weight = weights_list[category - 1]
category_list.remove(category_list[category - 1])
category_list = sum(category_list)
result = (((grade_needed - category_list) / weight) * (total_points + assignment_worth)) - earned_points
print(round(result, 2))
