Raspberry Pi GPIO Calculator

A hardware-based calculator built using a Raspberry Pi, 4×4 matrix keypad, and 16×2 LCD display.

The project demonstrates practical Raspberry Pi GPIO programming, matrix keypad scanning, LCD interfacing, and Python-based arithmetic expression handling.

Features
4×4 matrix keypad input
16×2 LCD display
Addition, subtraction, multiplication, and division
Square operation
Multi-digit number input
Basic arithmetic expression evaluation
Keypad debouncing
GPIO-based hardware interfacing
Error handling for invalid calculations
Real-time display of input and results
Hardware Used
Raspberry Pi
4×4 Matrix Keypad
16×2 LCD
Breadboard
Jumper wires
Power supply
GPIO Pin Configuration
16×2 LCD
LCD Pin	Raspberry Pi GPIO
RS	GPIO 21
E	GPIO 20
D4	GPIO 16
D5	GPIO 12
D6	GPIO 26
D7	GPIO 13

The LCD is interfaced with the Raspberry Pi using a 4-bit communication interface.

4×4 Keypad
Keypad Connection	Raspberry Pi GPIO
Row 1	GPIO 2
Row 2	GPIO 3
Row 3	GPIO 4
Row 4	GPIO 17
Column 1	GPIO 18
Column 2	GPIO 23
Column 3	GPIO 24
Column 4	GPIO 25
Key Mapping
Key	Function
0–9	Number input
A	Addition (+)
B	Subtraction (-)
C	Multiplication (*)
D	Division (/)
*	Square
=	Calculate
How It Works

The Raspberry Pi continuously scans the rows and columns of the 4×4 matrix keypad to detect key presses.

When a key is pressed:

The keypad scanning routine identifies the corresponding key.
Numerical keys are added to the current expression.
Operator keys are converted into their respective mathematical operators.
The entered expression is displayed on the LCD.
Pressing = evaluates the expression and displays the result.
Pressing * calculates the square of the entered number.
After displaying the result, the calculator is ready for a new calculation.

The LCD is controlled directly through Raspberry Pi GPIO pins using a 4-bit interface.

A small delay is used during keypad scanning to reduce unwanted multiple detections from a single key press.

Example Operations

12 + 5 → 17

8 × 7 → 56

25 ÷ 5 → 5

6² → 36

Software Used
Python 3
Thonny Python IDE
RPi.GPIO
Python Decimal module
Raspberry Pi OS / Linux environment
Expression Evaluation

The calculator uses Python's eval() function to evaluate arithmetic expressions entered through the keypad.

For the square operation, Python's Decimal class is used to perform the calculation.

The program also includes basic exception handling so that invalid calculations display an error instead of terminating the program.

Note: eval() is used as a simple approach for this hardware prototype. A dedicated expression parser would be more appropriate for a production implementation.

Project Structure
Raspberry-Pi-GPIO-Calculator/
│
├── calculator.py
└── README.md
Running the Project

The program was developed and tested using the Thonny Python IDE on the Raspberry Pi.

After connecting the LCD and keypad according to the GPIO configuration:

Open calculator.py in Thonny.
Connect the Raspberry Pi hardware.
Run the program using Thonny.
The LCD initializes and displays the calculator interface.
Use the keypad to enter numbers and perform calculations.
Learning Outcomes

This project provided practical experience in:

Raspberry Pi GPIO programming
Python programming for hardware control
Interfacing a 4×4 matrix keypad with a Raspberry Pi
Scanning keypad rows and columns
Interfacing a 16×2 LCD in 4-bit mode
Digital input and output control
Hardware-software integration
Handling user input from physical hardware
Implementing arithmetic operations in Python
Basic exception handling
Implementing keypad debouncing
Debugging hardware and software interaction
Understanding GPIO-based embedded system design
Future Improvements

The project can be further developed by adding:

Decimal number input
Negative number support
Parentheses and advanced mathematical operations
A dedicated clear/reset function
Calculation history
Memory functions such as M+, M-, and MR
A safer mathematical expression parser instead of eval()
Improved handling of long expressions on the 16×2 LCD
More robust keypad debouncing
Additional mathematical functions such as square root and percentage
A custom PCB for a compact implementation
A 3D-printed enclosure
Battery-powered operation
Project Status

Completed Prototype

The calculator successfully demonstrates keypad-based numerical input, arithmetic operations, LCD output, and Raspberry Pi GPIO control.

Conclusion

This project demonstrates how a Raspberry Pi can be used to develop a complete hardware-software system by combining GPIO programming, matrix keypad interfacing, LCD communication, and Python-based computation.

It provided hands-on experience in connecting physical hardware with software and implementing an interactive embedded application.


https://github.com/user-attachments/assets/6ce862e2-1ef8-4d33-a4b2-9c217a93e5fd



<img width="1600" height="1200" alt="calc" src="https://github.com/user-attachments/assets/47699bec-58d8-4a66-a98f-640065d97a76" />




