def compute_grade(score):
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    elif score < 0.6:
        return 'F'
    else:
        return "Invalid score"

score = float(input("Enter Score: "))

grade = compute_grade(score)
print(grade)