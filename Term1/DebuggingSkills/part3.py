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
        if grade > highest_grade:
            highest_grade = grade
    
    print("The highest grade is:", highest_grade)

 
    passing_grades = 0
    for grade in grades:
        if grade >= 60:
            passing_grades += 1
        print("Current passing grade count:", passing_grades)  

    print("Final number of passing grades:", passing_grades)

if __name__ == "__main__":
    main()

