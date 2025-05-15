# input_processing.py
# Manuja Senanayake, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light = "green"
        self.pedestrian="no"
        self.vehicle="no"

    # function that updates the associated memeber variable provided during call 
    def update_status(self,light=None,pedestrian=None,vehicle=None): 
            
        # if statements used to update the only the specific member var value provided during function call
        # nested ifs catch any invlaid vlaues inputted and return invalid vision change message, return to end method call
        if light is not None:
            if light not in ("red", "yellow", "green"):
                print("Invalid Vision Change")
                return
            self.light = light
        if  pedestrian is not None:
            if pedestrian not in ("yes", "no"):
                print("Invalid Vision Change")
                return
            self.pedestrian = pedestrian
        if vehicle is not None:
            if vehicle not in ("yes", "no"):
                print("Invalid Vision Change")
                return
            self.vehicle = vehicle



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    # Any scenario where a red light, a pedestrian or a vehicle are detected will display the message "STOP"
    if sensor.light=="red" or sensor.pedestrian=="yes" or sensor.vehicle=="yes" :
         print('\nSTOP\n')
         print("Light= ",sensor.light,", Pedestrian= ", sensor.pedestrian,", Vehicle= ",sensor.vehicle,"\n" )
    # A green light with no pedestrian or vehicle detected will display the message "Proceed
    elif sensor.light=="Yellow" and sensor.pedestrian=="no" and sensor.vehicle=="no" :
         print('\nPROCEED\n')
         print("Light= ",sensor.light,", Pedestrian= ", sensor.pedestrian,", Vehicle= ",sensor.vehicle,"\n" )
    # A yellow light with no pedestrian or vehicle detected will display the message "Caution"
    elif sensor.light=="yellow" and sensor.pedestrian=="no" and sensor.vehicle=="no" :
         print('\nCAUTION\n')
         print("Light= ",sensor.light,", Pedestrian= ", sensor.pedestrian,", Vehicle= ",sensor.vehicle,"\n" )
    # for when the vlaues of the memeber variables do not match any of the above scenarios
    else:
         print("Invlaid Vision Change")


# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    # declaring and initilizing choice (loop control var)
    choice = 99999999
    # instantiating object 
    state = Sensor()

    # while loop for rudimentary menu (uses choice as control var)
    # loop will stop and program will end if the value of choice is set to 0
    while choice != '0':
        # Display initial message and prompt for user input
        print("Are changes deteted in the vision input?")
        choice = input("Select 1 to update the detected traffic light colour, 2 to update whether a pedestrian is detected, 3 to update whether a vehicle is detected, 0 to end the program: ").strip()
        # catch invalid inputs, prints message to let user know, go to next iteration of loop
        if choice not in ("1","2","3","0"):
                print("INVALID INPUT!!!!" )
                continue
        # if input is 1; prompt for value, call update_status to update the light var of the object to inputted value
        # call custom print funtion to print object
        # Continue to next interation of loop
        elif choice == '1':
             change = input("What chage has been identified?: ").lower().strip()
             state.update_status(light=change)
             print_message(state)
             continue
        # if input is 2; prompt for value, call update_status to update the pedestrian var of the object to inputted value
        # call custom print funtion to print object
        # Continue to next interation of loop
        elif choice == '2':
             change = input("What chage has been identified?: ").lower().strip()
             state.update_status(pedestrian=change)
             print_message(state)
             continue
        # if input is 3; prompt for value, call update_status to update the vehicle var of the object to inputted value
        # call custom print funtion to print object 
        # Continue to next interation of loop    
        elif choice == '3':
             change = input("What chage has been identified?: ").lower().strip()
             state.update_status(vehicle=change)
             print_message(state)
             continue   



# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

