import sys

def initial_phonebook():
    rows, cols = int(input("PLease enter initial number of contacts:")), 5

    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):") %(i + 1)
        print("NOTE: * indicates mandatory fields")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name*: ")))


                if temp[j] == '' or temp[j] == '':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
                
                if j == 1:
                    temp.append(int(input("Enter number* :")))

                if j == 2:
                    temp.append(str(input("Enter date of e-mail address")))

                if temp[j] == '' or temp[j] == '':
                    temp[j] = None

                if j == 3:
                    temp.append(str(input("Enter date of birth(dd/mm/yy)")))

                    if temp[j] == '' or temp[j] == '':
                        temp[j] = None

                if j == 4:
                    temp.append(str(input("Enter category(Family/Friends/Work/Others)")))

                if temp[j] == "" or temp[j] == '':
                    temp[j] = None

        print(phone_book)
        return phone_book
    
    def menu():
        print("**************************************")
        print("\t\t\tSMARTPHONE DIRECTORY", flush = False)
        print("**************************************")
        print("\tYou can now perform the following operations on this phonebook\n")
        print("1. Add a new contact")
        print("2. Remove an existing contact")
        print("3. Delete all contacts")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Exit phonebook")

        choice = int(input("Please enter your choice"))

        return choice
    
    def add_contact(pb):

        dip = []
        for i in range(len(pb[0])):
            if i == 0:
                dip.append(str(input("Enter name: ")))
            if i == 1:
                dip.append(str(input("Enter number")))
            if i == 2:
                dip.append(str(input("Enter e-mail address")))
            if i == 3:
                dip.append(str(input("Enter date of birth(dd/mm/yy)")))
            if i == 4:
                dip.append(str(input("Enter category(Family/Friends/Work/Others)")))
            pb.append(dip)

            return pb
        def remove_existing(pb):

            query = str(str(input("Please enter the name of the contact you wish to remove: ")))

            temp = 0

            for i in range(len(pb)):
                if query == pb[i][0]:
                    temp += 1

                    print(pb.pop(i))

                    print("This query has been now removed")

                    return pb
                if temp == 0:

                    print("Sorry, you have entered an invalid query.\nPlease recheck and try again later.")
                    return pb
                
                def delete_all(pb):

                    return pb.clear()
                
                def search_existing(pb):

                    choice = int(input("Enter search criteria\n\n\n 1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category (Family/Friends/Work/Others)\ \nPlease enter: "))

                    temp = []
                    check = -1

                    if choice == 1:

                        query = str(input("Please enter the name of the contact you wish to search: "))

                        for i in range(len(pb)):
                            if query == pb[i][0]:
                                check = i 
                                temp.append(pb[1])

            elif choice == 2:
query = int(input("Please enter the number of the contact you wish to search: "))

for i in range(len(pb)):
                      
        if query == pb[i][1]:
            check = i
            temp.append(pb[1])

    elif choice == 3:

query = str(input("Please enter the e-mail ID\ of the contact you wish to search"))
for i in range(len(pb)):
    if query == pb[i][2]:
        check = i
        temp.append(pb(i))

    elif choice == 4

    query = str(input("Please enter the DOB (in dd/mm/yyy format ONLY)\ of the contact you wish to search: "))

    for i in range(len(pb))
    if query == pb[i][3]:
        check = i
        temp.append(pb[i])

    else:

        print("invalid search criteria")
        return -1
    
else:
    display_all(temp)
    return check

def display_all(pb):
    if not pb:

        print("List is empty: []")
