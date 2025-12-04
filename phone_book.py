import sys

def initial_phonebook():
        rows,cols = int(input("Please enter initial number of contacts: ")),5
        phone_book=[]
        print(phone_book)
        for i in range(rows):
               print("\nEnter contact %d details in the following order (ONLY):"% (i+1))
               print("NOTE: *indicates mandotary feilds")
               print(".............................................................")
               temp=[]
               for j in range(cols):
                       if j == 0:
                         temp.append(str("enter a number* :  "))

    