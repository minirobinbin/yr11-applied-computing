def calculate_average(numbers):
    total = 0 
    for num in numbers:
        total += num 
        average = total / len(numbers)
    return average 

def main(): 
    grades = [85, 92, 78, 90, 88] 
    result = calculate_average(grades) 
    print("The average grade is: ", result)
    
if __name__ == "__main__":
    main()