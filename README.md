Max Molnar 100746162
TPRG2 - Project 1
This repository contains three files; The vending_machine.py file is the base state machine progam for the vending machine that works on windows using a graphic
user inteface by PySimpleGUI. The test_vending_machine.py file tests the state machine and checks the value of all of the coins (Nickel, Dime, Quarter, Loonie, Toonie)
and that the program cycles to the correct state to deposit and return the coins. The second branch contains the vending_machine_Pi4.py file that works with the Raspberry
Pi 4 and interfaces with external circuits; one being the RETURN pushbutton and the other being a physical Servo motor that emulates the vending machine dispensing product. 
The difference between the Rpi4 file and the Windows file is simply that the servo motor code is commented out to avoid windows trying to interface with it. The test file works
with both the windows or the Rpi4 file. 
