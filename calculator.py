import RPi.GPIO as GPIO
from time import sleep
import time
from decimal import Decimal

# Use BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for LCD
LCD_RS = 21
LCD_E = 20
LCD_D4 = 16
LCD_D5 = 12
LCD_D6 = 26
LCD_D7 = 13

# Set GPIO pins as outputs for LCD
GPIO.setup(LCD_RS, GPIO.OUT)
GPIO.setup(LCD_E, GPIO.OUT)
GPIO.setup(LCD_D4, GPIO.OUT)
GPIO.setup(LCD_D5, GPIO.OUT)
GPIO.setup(LCD_D6, GPIO.OUT)
GPIO.setup(LCD_D7, GPIO.OUT)

# LCD Constants
LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

# LCD utility functions
def lcd_toggle_enable():
    sleep(0.0005)
    GPIO.output(LCD_E, True)
    sleep(0.0005)
    GPIO.output(LCD_E, False)
    sleep(0.0005)

def lcd_byte(bits, mode):
    GPIO.output(LCD_RS, mode)
    GPIO.output(LCD_D4, bool(bits & 0x10))
    GPIO.output(LCD_D5, bool(bits & 0x20))
    GPIO.output(LCD_D6, bool(bits & 0x40))
    GPIO.output(LCD_D7, bool(bits & 0x80))
    lcd_toggle_enable()
    GPIO.output(LCD_D4, bool(bits & 0x01))
    GPIO.output(LCD_D5, bool(bits & 0x02))
    GPIO.output(LCD_D6, bool(bits & 0x04))
    GPIO.output(LCD_D7, bool(bits & 0x08))
    lcd_toggle_enable()

def lcd_init():
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)

def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for char in message:
        lcd_byte(ord(char), LCD_CHR)

# Keypad setup
ROW_PINS = [2, 3, 4, 17]
COL_PINS = [18, 23, 24, 25]

KEYPAD = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '=', 'D']
]

GPIO.setup(ROW_PINS, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(COL_PINS, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Keypad scanning function
def read_keypad():
    for row in range(4):
        # Set all rows HIGH
        for r in ROW_PINS:
            GPIO.output(r, GPIO.HIGH)

        # Set one row LOW at a time
        GPIO.output(ROW_PINS[row], GPIO.LOW)
        sleep(0.01)

        for col in range(4):
            if GPIO.input(COL_PINS[col]) == GPIO.HIGH:
                # Wait for key release
                while GPIO.input(COL_PINS[col]) == GPIO.HIGH:
                    sleep(0.01)
                return KEYPAD[row][col]

    return None

def calculate_expression(expr):
    try:
        return str(eval(expr))
    except Exception:
        return "Error"

def main():
    lcd_init()
    lcd_string("Calculator", LCD_LINE_1)
    sleep(2)

    current_input = ""
    lcd_string("Input: ", LCD_LINE_1)

    while True:
        key = read_keypad()

        if key:
            print("Pressed:", key)

            if key in "0123456789":
                current_input += key
                lcd_string(current_input, LCD_LINE_2)

            elif key == 'A':
                current_input += "+"
                lcd_string(current_input, LCD_LINE_2)

            elif key == 'B':
                current_input += "-"
                lcd_string(current_input, LCD_LINE_2)

            elif key == 'C':
                current_input += "*"
                lcd_string(current_input, LCD_LINE_2)

            elif key == 'D':
                current_input += "/"
                lcd_string(current_input, LCD_LINE_2)

            elif key == '*':
                try:
                    num = Decimal(current_input)
                    current_input = str(num ** 2)
                    lcd_string("Result:", LCD_LINE_1)
                    lcd_string(current_input, LCD_LINE_2)
                    print("Squared Result:", current_input)
                    time.sleep(2)
                    current_input = ""
                    lcd_string("Input: ", LCD_LINE_1)

                except Exception:
                    lcd_string("Error", LCD_LINE_2)
                    print("Error Squaring")
                    time.sleep(2)
                    current_input = ""
                    lcd_string("Input: ", LCD_LINE_1)

            elif key == '=':
                result = calculate_expression(current_input)
                lcd_string(current_input, LCD_LINE_1)
                lcd_string(result, LCD_LINE_2)
                print(f"{current_input} = {result}")
                time.sleep(3)
                current_input = ""
                lcd_string("Input: ", LCD_LINE_1)

        time.sleep(0.1)

try:
    main()
finally:
    GPIO.cleanup()
