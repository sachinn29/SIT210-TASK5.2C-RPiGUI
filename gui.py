# Import the necessary libraries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Set up the LED pins
red_led = LED(14)
white_led = LED(10)
green_led = LED(6)

# Define LED toggle functions

# For RED LED
def toggle_red_led():
    if red_led.is_lit:
        red_led.off()
        red_button["text"] = "Turn Red LED On"
    else:
        red_led.on()
        red_button["text"] = "Turn Red LED Off"

# For WHITE LED
def toggle_white_led():
    if white_led.is_lit:
        white_led.off()
        white_button["text"] = "Turn White LED On"
    else:
        white_led.on()
        white_button["text"] = "Turn White LED Off"

# For GREEN LED
def toggle_green_led():
    if green_led.is_lit:
        green_led.off()
        green_button["text"] = "Turn Green LED On"
    else:
        green_led.on()
        green_button["text"] = "Turn Green LED Off"

# Define exit function
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Create buttons for LEDs and exit

# Red LED button
red_button = Button(win, text="Turn Red LED On", font=myFont, command=toggle_red_led)
red_button.grid(row=0, column=1)

# White LED button
white_button = Button(win, text="Turn White LED On", font=myFont, command=toggle_white_led)
white_button.grid(row=0, column=3)

# Green LED button
green_button = Button(win, text="Turn Green LED On", font=myFont, command=toggle_green_led)
green_button.grid(row=0, column=6)

# Exit button
exit_button = Button(win, text="Exit", font=myFont, command=close, bg='red')
exit_button.grid(row=2, column=3)

# Assign exit function to window close button
win.protocol("WM_DELETE_WINDOW", close)

# Enter main loop
win.mainloop()  # Loop forever