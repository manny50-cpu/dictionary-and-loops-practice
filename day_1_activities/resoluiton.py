# -----------------------------------------
# Existing student data (example starter)
# -----------------------------------------
students = [
    {
        "cps_id": "123456",
        "name": "Lopez, Maria",
        "middle_name": "Isabel",
        "homeroom": "301",
        "grade": 7,
        "primary_email": "mlopez@cps.edu",
        "secondary_email": "mlopez2@cps.edu"
    },
    {
        "cps_id": "789012",
        "name": "Johnson, Malik",
        "middle_name": "Andre",
        "homeroom": "204",
        "grade": 8,
        "primary_email": "mjohnson@cps.edu",
        "secondary_email": "mjohnson2@cps.edu"
    }
]


# -----------------------------------------
# SEARCH FUNCTION
# -----------------------------------------
def search_student(full_name):
    """
    Students must be able to describe this process:
    - Loop through the list of student dictionaries
    - Compare the 'name' field to the search term
    - If found, return the dictionary
    - If not found, return None
    """
    # first step: 
    # create a loop to loop throughthe students

    for student in students:
        if student["name"].lower() == full_name.lower()
        
    # then compare the name field to the search term
       
            # if found, return the dictionary
            
    # if not found, return None
    


# -----------------------------------------
# ADD NEW STUDENT FUNCTION
# -----------------------------------------
def add_student():
    print("\n--- Add a New Student ---")

    # Get user input for all required fields
    cps_id = input("Cps ID:")

    # Check for duplicate CPS ID
    # Loop through existing students to see if cps_id already exists
    for student in students:
        if student["cps_id"] == cps_id:
            print('Error, this cps id is already in use')
            return
        # Check if the current student's cps_id matches the new cps_id
        
            # If a match is found, print an error and exit the function
            
            # Exit the function early to prevent adding a duplicate
            

    # Continue gathering the rest of the information
    # Prompt the user for each piece of information
    first = input("First Name: ")
    last = input("Last Name: ")
    middle = input("Middle Name: ")
    homeroom = input("Homeroom: ")
    grade = int(input("Grade Level: "))
    primary = input("Primary Email: ")
    secondary = input("Secondary Email: ") 

    full_name = f"{last},{first}"


    # Format name as "Last, First"
    

    # Build the dictionary
    # Create a new dictionary with all the collected information from the user inputs
    new_student = {
        "cps_id": cps_id,
        "name": full_name,
        "middle_name": middle,
        "homeroom": homeroom,
        "grade": grade,
        "primary_email": primary,
        "secondary_email": secondary
    }

    # Add to the list
    students.append(new_student)

    # Confirmation
   print(f"/nstudent {full_name} added succesfully!")
print(new_student
)
print("Total students in the system:", len(students))
print("new record accded:", new_student)

# -----------------------------------------
# MAIN PROGRAM LOOP
# this is where the program starts running

# -----------------------------------------
while True:
    # Menu
    print("\n===== STUDENT LOOKUP TOOL =====")
    print("1. Search for a student")
    print("2. Add a new student")
    print("3. Quit")

    # Get user choice
    choice = input("Choose an option: ")
    # Handle user choice
    if choice == "1":
        # Search for a student
        choice_name = input("\nEnter the student's full name(Last,first)")
        # Call the search function and store the result
        
        

        # Display results
        if result:
        print(f"Cps ID:{result['cps_id']})
        print(f"first name:"{result}{'full_name'})
        print(f"middle name: {result {'middle_name'}}")
        print(f"homeroom: {result {'homeroom'}}")
        print(f"grade: {result {'grade'}}")
        print(f"primary email: {result {'primary_email'}}")
        print(f"secondary email: {result {'secondary_email'}}")




        else:
            # Inform the user if the student was not found
            print("\nStudent not found.")

    elif choice == "2":
         add_student()
        
        

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")