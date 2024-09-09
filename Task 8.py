grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
names = sorted(students)
print(names)
middle_grade = [sum(grades [0])/ len(grades [0]), sum(grades [1])/ len(grades [1]),sum(grades [2])/ len(grades [2]),sum(grades [3])/ len(grades [3]),sum(grades [4])/ len(grades [4])]
print (middle_grade)
students_middle_grades = {names[0]: middle_grade[0], names[1]: middle_grade[1], names[2]: middle_grade[2], names[3]: middle_grade[3], names[4]: middle_grade[4]}
print(students_middle_grades)
