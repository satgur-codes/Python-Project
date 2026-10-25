#Students_Marks_Manager
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}

while True:
    print("\n--- Student Menu ---")
    print("1. Add student")
    print("2. View all Results)")
    print("3. Show topper")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        
        if name in students:
            print("Student already exists.")
            continue
            
        marks = []
        while len(marks) < 3:
            m = float(input(f"Enter mark {len(marks) + 1} (0-100): "))
            if m < 0 or m > 100:
                print("Invalid mark, try again.")
            else:
                marks.append(m)
                
        students[name] = marks
        print("Student added successfully!")
        
    elif choice == "2":
        print("\nStudent Averages and Grades:")
        for name in students:
            lst = students[name]
            total = 0
            for mark in lst:
                total = total + mark
            avg = total / 3
            
            # Grade calculation
            if avg >= 85:
                grade = "A"
            elif avg >= 70:
                grade = "B"
            elif avg >= 50:
                grade = "C"
            else:
                grade = "F"
                
            print(name, round(avg, 2), grade)
            
    elif choice == "3":
        highest_avg = 0
        topper_name = ""
        
        for name in students:
            lst = students[name]
            total = 0
            for mark in lst:
                total = total + mark
            avg = total / 3
            
            if avg > highest_avg:
                highest_avg = avg
                topper_name = name
                
        print("Topper:", topper_name)
        
    elif choice == "4":
        print("Thanks! for using our program.... See You Again...")
        break
        
    else:
        print("Invalid choice, please try again.")
