import json

title = '===student mark management system=== '.upper()
print(title)

def loadData():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def showMenu():
	menu = ["Add Student ",
	"Delete student",
	"Update student",
	"Search student",	
	"Display all students",
	" Exit"]
	
	count = 0
	for item in menu:		
		count +=1
		print(count,'.', item)

print("_"*55)	
showMenu()

        						
students=loadData()
        
def saveData():
	with open("students.json" , 'w') as file:
		json.dump( students, file, indent = 4)

        
while True:
        try:
        	print("_" * 55)
        	usersChoice = int(input("\nEnter your choice form menu using the numbers from (1 to 6): "))                       
        
        except ValueError:
         	  print("Enter only numbers not letters")
         	  continue
        
        
     #ADD STUDENT
        if usersChoice == 1:
                        
                        name = input("\ntype student name: ").lower()
                        if name in students:
                        	print("\nStudent already exists!".upper())
                        	continue
                        try:
                        	age = int(input("enter student age: "))
                        	grade = int(input("enter student grade: "))
                        except ValueError:
                        	print("Only numbers allowed !!".upper())
                        	continue
                        
                        students[name] = {
                                  "age" : age,
                                  "grade": grade,
                                  "marks" : {"maths" : 0,
                                                    "siswati" : 0
                                  }}
                        saveData()
                                  
                        print("Student added to system".upper())
                        for name, details in students.items():
                        	print("\nStudent:", name.upper())
                        	print("Age:", details["age"])
                        	print("Grade:", details["grade"])
                        	print("Maths:", details["marks"]["maths"])
                        	print("Siswati:", details["marks"]["siswati"])
                        	print("-" * 30)
                        
                           
    #DELETE STUDENT       
        elif usersChoice == 2:
                                  name = input("enter student to delete: ").lower()
                                  if name in students:
                                  	del students[name]
                                  	print("student deleted".upper())
                                  	saveData()
                                  else:
                                  	print("student not found".upper())
                                  	
      # UPDATE STUDENT
        elif usersChoice == 3:
                name = input("\nEnter student you want to update: ").lower()
                if name in students:
                        try:
                            choice = int(input(
                "\nWhat do you want to update?\n"
                "1. Age\n"
                "2. Grade\n"
                "3. Marks\n"
                "Enter your choice: "
            ))
                        except ValueError:
                            print("Enter only a number!".upper())
                            continue

                        if choice == 1:
                            		try:
                            			new_age = int(input("Enter new age: "))
                            			students[name]["age"] = new_age
                            			print("Age updated successfully!".upper())
                            			saveData()
                            		except ValueError:
                            			print("Age must be a number!".upper())

                        elif choice == 2:
                            		try:
                            			new_grade = int(input("Enter new grade: "))
                            			students[name]["grade"] = new_grade
                            			print("Grade updated successfully!".upper())
                            			saveData()
                            		except ValueError:
                            			print("Grade must be a number!".upper())

                        elif choice == 3:
                            	subject = input("Enter subject name: ").lower()
                            	try:
                            			mark = int(input("Enter new mark: "))
                            			students[name]["marks"][subject] = mark
                            			print("Mark updated successfully!".upper())
                            			saveData()
                            	except ValueError:
                            		print("Mark must be a number!".upper())

                        else:
                            	print("Only numbers 1 to 3 are allowed!".upper())
                else:
                      print("student not found !!!".upper())               	              	
              	          	              	       	      
              	          	             	       	       
     #SEARCH STUDENT       
        elif usersChoice == 4:
                                  name = input("\nEnter student to search: ").lower()
                                  if name in students:
                                  	print("\nStudent found".upper())
                                  	print("\n....._Details_.....")
                                  	print('\nName: ',name.title())
                                  	print("Age :",students[name]["age"])
                                  	print("Grade:", students[name]["grade"])
                                  	print("Marks")
                                  	for subject, mark in students[name]["marks"].items():
                                  		print(subject.capitalize(), ":", mark)
                                  	
                                  else:
                                  	print("Sorry, student not found".upper())
        
        
     #DISPLAY ALL STUDENTS DETAILS
        elif usersChoice == 5:
        	if not students:
        		print("No students found".upper())
        	else:
        		print("\n_____ALL STUDENTS_____")
        		
        		for name, details in students.items():
        		  print("\nStudent:", name.upper())
        		  print("Age:", details["age"])
        		  print("Grade:", details["grade"])
        		  print("Maths:", details["marks"]["maths"])
        		  print("Siswati:", details["marks"]["siswati"])
        		  print("-" * 30)
        		   
  #EXIT 		  		  
        elif usersChoice == 6:              
        	print("thank you for using the system \n good bye !!!".upper())
        	break
   
   #INVALID SYNTAX   	
        else:
        	print("Please enter number from 1 to 6 only")