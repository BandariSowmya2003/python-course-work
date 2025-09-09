from Programs import *

def main():
    while True:
        print("\n=== Python Function Bank ===")
        print("1. Clear Set")
        print("2. Display Current Date and Time")
        print("3. Display Current Year, Month, Day")
        print("4. Subtract Days from a Given Date")
        print("5. Find Age from Birthdate")
        print("6. Display Calendar for a Given Month/Year")
        print("7. Print Diamond Star Pattern")
        print("8. Print Hollow Square")
        print("9. BMI Calculator")
        print("10.Account Login Process")
        print("0. Exit\n")
        
        choice = input("Enter your choice (0-10): ")

        if choice == "1":
            clear_set()
        elif choice == "2":
            display_datetime()
        elif choice == "3":
            display_ymd()
        elif choice == "4":
            subtract_days_from_date()
        elif choice == "5":
            calculate_age()
        elif choice == "6":
            display_calendar()
        elif choice == "7":
            diamond_star()
        elif choice == "8":
            hollow_square()
        elif choice == "9":
            bmi_calculator()
        elif choice == "10":
            account_login()
        elif choice == "0":
            print("End Programs.Thank you!!!")
            break
        else:
            print("Invalid choice! Please enter a number between 0 to 10.")

main()

#Output:
'''
=== Python Function Bank ===
1. Clear Set
2. Display Current Date and Time
3. Display Current Year, Month, Day
4. Subtract Days from a Given Date
5. Find Age from Birthdate
6. Display Calendar for a Given Month/Year
7. Print Diamond Star Pattern
8. Print Hollow Square
9. BMI Calculator
10.Account Login Process
0. Exit

Enter your choice (0-10): 1

    Program:
    -----------
    set = {1, 2, 3, 4, 5}
    print("Original Set:", set)
    set.clear()
    print("After Clearing:", set)

    Testcases:
    -----------
    Test Case 1: {1, 2, 3} → {}
    Test Case 2: {10, 20} → {}

    Explanation:
    ------------
    The clear() method removes all elements from a set, leaving it empty.



=== Python Function Bank ===
1. Clear Set
2. Display Current Date and Time
3. Display Current Year, Month, Day
4. Subtract Days from a Given Date
5. Find Age from Birthdate
6. Display Calendar for a Given Month/Year
7. Print Diamond Star Pattern
8. Print Hollow Square
9. BMI Calculator
10.Account Login Process
0. Exit

Enter your choice (0-10): 2

    Program:
    -----------
    import datetime
    now = datetime.datetime.now()
    print(datetime.datetime.now())

    Testcases:
    ------------
    Test Case: Outputs current date and time, e.g., 2025-08-17 18:45:12

    Explanation:
    ------------
    datetime.now() returns the system’s current date and time.



=== Python Function Bank ===
1. Clear Set
2. Display Current Date and Time
3. Display Current Year, Month, Day
4. Subtract Days from a Given Date
5. Find Age from Birthdate
6. Display Calendar for a Given Month/Year
7. Print Diamond Star Pattern
8. Print Hollow Square
9. BMI Calculator
10.Account Login Process
0. Exit

Enter your choice (0-10): 3


    Program:
    ----------
    import datetime
    today = datetime.date.today()
    print("Year:", today.year)
    print("Month:", today.month)
    print("Day:", today.day)

    Testcases:
    -----------
    Test Case: 2025 8 17

    Explanation:
    --------------
    today.year, today.month, today.day extract parts of the date object.



=== Python Function Bank ===
1. Clear Set
2. Display Current Date and Time
3. Display Current Year, Month, Day
4. Subtract Days from a Given Date
5. Find Age from Birthdate
6. Display Calendar for a Given Month/Year
7. Print Diamond Star Pattern
8. Print Hollow Square
9. BMI Calculator
10.Account Login Process
0. Exit

Enter your choice (0-10): 4

    Program:
    -----------
    import datetime
    days_to_subtract = 5
    new_date = given_date - datetime.timedelta(days=days_to_subtract)
    print("Original Date:", given_date)
    print("After Subtracting 5 Days:", new_date)

    Testcases:
    -----------
    Test Case: 2025-08-17 minus 5 days → 2025-08-12

    Explanation:
    -------------
    timedelta allows subtracting days from a date object.



=== Python Function Bank ===
1. Clear Set
2. Display Current Date and Time
3. Display Current Year, Month, Day
4. Subtract Days from a Given Date
5. Find Age from Birthdate
6. Display Calendar for a Given Month/Year
7. Print Diamond Star Pattern
8. Print Hollow Square
9. BMI Calculator
10.Account Login Process
0. Exit

Enter your choice (0-10): 5

    Program:
    ---------
    import datetime
    def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

    Testcases:
    -----------
    Test Case: Birthdate 2000-05-20 → Age 25 (in 2025)

    Explanation:
    ------------
    Subtract years, then adjust if the birthday hasn’t occurred this year.



=== Python Function Bank ===
1. Clear Set
2. Display Current Date and Time
3. Display Current Year, Month, Day
4. Subtract Days from a Given Date
5. Find Age from Birthdate
6. Display Calendar for a Given Month/Year
7. Print Diamond Star Pattern
8. Print Hollow Square
9. BMI Calculator
10.Account Login Process
0. Exit

Enter your choice (0-10): 6

    Program:
    ------------
    import calendar
    year=2025
    month=8
    print(calendar.month(year, month))

    Testcases:
    ------------
    Test Case: August 2025 calendar printed

    Explanation:
    -------------
    calendar.month(year, month) prints formatted calendar text.



=== Python Function Bank ===
1. Clear Set
2. Display Current Date and Time
3. Display Current Year, Month, Day
4. Subtract Days from a Given Date
5. Find Age from Birthdate
6. Display Calendar for a Given Month/Year
7. Print Diamond Star Pattern
8. Print Hollow Square
9. BMI Calculator
10.Account Login Process
0. Exit

Enter your choice (0-10): 7

    Program:
    -----------
    n = 5
    for i in range(n):
        print(" " *(n-i-1) + "*" *(2*i+1))
    for i in range(n-2, -1, -1):
        print(" "*(n-i-1) + "*" *(2*i+1))

    Testcase:
    -----------
    Test Case :(n=5)
    ("    *    ")
    ("   ***   ")
    ("  *****  ")
    (" ******* ")
    ("*********")
    (" ******* ")
    ("  *****  ")
    ("   ***   ")
    ("    *    ")


    Explanation:
    -------------
    Uses two loops to print upper and lower halves of the diamond.



=== Python Function Bank ===
1. Clear Set
2. Display Current Date and Time
3. Display Current Year, Month, Day
4. Subtract Days from a Given Date
5. Find Age from Birthdate
6. Display Calendar for a Given Month/Year
7. Print Diamond Star Pattern
8. Print Hollow Square
9. BMI Calculator
10.Account Login Process
0. Exit

Enter your choice (0-10): 8

    Program:
    ----------
    n = 5
    for i in range(n):
        if i == 0 or i == n-1:
            print("*" * n)
        else:
            print("" + " "(n-2) + "*")

    Testcase:
    ------------
    Test Case :(n=5)
    (" * * * * * ")
    (" *       * ")
    (" *       * ")
    (" *       * ")
    (" * * * * * ")

    Explanation:
    -------------
    First and last rows full stars, middle rows with spaces inside.



=== Python Function Bank ===
1. Clear Set
2. Display Current Date and Time
3. Display Current Year, Month, Day
4. Subtract Days from a Given Date
5. Find Age from Birthdate
6. Display Calendar for a Given Month/Year
7. Print Diamond Star Pattern
8. Print Hollow Square
9. BMI Calculator
10.Account Login Process
0. Exit

Enter your choice (0-10): 9

    Program:
    ------------
    weight = int(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi = weight / (height ** 2)
    print("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Normal weight")
    elif 25 <= bmi < 29.9:
        print("Overweight")
    else:
        print("Obese")

    Testcases:
    ------------
    Test Case: weight=70kg, height=1.75m → BMI = 22.86

    Explanation:
    --------------
    Formula = weight / height², rounded to 2 decimals.



=== Python Function Bank ===
1. Clear Set
2. Display Current Date and Time
3. Display Current Year, Month, Day
4. Subtract Days from a Given Date
5. Find Age from Birthdate
6. Display Calendar for a Given Month/Year
7. Print Diamond Star Pattern
8. Print Hollow Square
9. BMI Calculator
10.Account Login Process
0. Exit

Enter your choice (0-10): 10

    Program:
    -------------
    username = "admin"
    password = "1234"
    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid login")

    Testcases:
    -----------
    Test Case 1: admin/1234 → Login successful
    Test Case 2: user/1111 → Invalid login

    Explanation:
    -------------
    Checks if username and password match predefined values.



=== Python Function Bank ===
1. Clear Set
2. Display Current Date and Time
3. Display Current Year, Month, Day
4. Subtract Days from a Given Date
5. Find Age from Birthdate
6. Display Calendar for a Given Month/Year
7. Print Diamond Star Pattern
8. Print Hollow Square
9. BMI Calculator
10.Account Login Process
0. Exit

Enter your choice (0-10): 0
End Programs.Thank you!!!
'''