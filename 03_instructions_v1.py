
# checks for a yes / no response
def yes_no(question):

    response = ""
    while response.lower() != "xxx":    


        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"


        else: 
            print("please answer yes / no") 
                                                                                      

def instructions():
    print()
    print(""" **** How to play... *****
    
    this is where you write the instructions.
    1. do this
    2. do this
    3. do this
    
    """)

    print()

  # ***** Main Routine Starts here *****

show_instructions = yes_no("have you played this game before ")

if show_instructions == "no":
    instructions()

else:
    print("Game continues")