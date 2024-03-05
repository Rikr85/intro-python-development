# A student makes honour roll if their average is >= 75
# and their lowest grade is not below 75

# gpa = float(input('What was your Grade Point Average? '))
# lowest_grade = float(input('What was your lowest grade?'))

# if gpa >= .85:
#     if lowest_grade >= .70:
#         print('You made the honour roll')


gpa = float(input('What was your Grade Point Average? '))
lowest_grade = input('What was your lowest grade?')
lowest_grade = float(lowest_grade)

if gpa >= .85:
    if lowest_grade >= .70:
        print('You made the honour roll')
