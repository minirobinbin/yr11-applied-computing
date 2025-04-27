def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        if num > 50:
            total += num
            count += 1
    average = total / count
    return average

def main():
    grades = [85, 92, 78, 90, 88, 45, 30]
    result = calculate_average(grades)
    print("The average grade is: ", result)

    # Attempt to find the highest grade
    highest_grade = grades[0]
    for grade in grades:
        if grade > highest_grade: #swapped sign
            highest_grade = grade
    
    print("The highest grade is:", highest_grade)

    # Attempt to count passing grades (>= 60)
    passing_grades = 0
    for grade in grades:
        if grade >= 60:
            passing_grades += 1 #changed - to +
    
    print("Number of passing grades:", passing_grades)

if __name__ == "__main__":
    main()
