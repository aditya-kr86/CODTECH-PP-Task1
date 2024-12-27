from tkinter import *

class Calculator:
    def __init__(self):
        # This is the window where everything happens
        self.window = Tk()
        self.window.title("Calculator")

        # I Have Disabled direct typing in the display, Because it may cause unwanted issues
        self.calculator_screen = Entry(self.window, width=25, borderwidth=5, state="readonly", readonlybackground="white")
        self.calculator_screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # This will allow keyboard keys to work as button clicks
        self.window.bind("<Key>", self.key_press)

        # These are the calculator buttons
        button_list = [
            "AC", "←", "%", "/",  # First row of buttons
            "7", "8", "9", "*",  # Second row
            "4", "5", "6", "-",  # Third row
            "1", "2", "3", "+",  # Fourth row
            "0", ".", "=",       # Fifth row
        ]

        # Now we place these buttons in a grid layout
        row = 1
        col = 0
        for button_text in button_list:
            # Color logic: Non-digit buttons get red text for visibility
            color = "Red" if not button_text.isdigit() and button_text != "." else "black"
            button = Button(
                self.window,
                text=button_text,
                width=5,
                height=2,
                fg=color,
                command=lambda text=button_text: self.button_click(text),  # Every button knows what it does
            )
            button.grid(row=row, column=col, padx=5, pady=5)  # Button placement
            col += 1
            if col > 3:  # Reset column after 4 buttons
                col = 0
                row += 1

        # This label can be used for additional info like "Calculator by Me"
        created_by = Label()

    def button_click(self, text):
        # What to do when a button is clicked
        current_value = self.calculator_screen.get()
        if text == "=":
            try:
                # `eval` evaluates the math expression (e.g., 2+3 becomes 5)
                result = str(eval(current_value))
                self.set_calculator_display(result)
            except:
                # If there's an error (like dividing by zero), show "Error"
                self.set_calculator_display("Error")
        elif text == "AC":
            # Clear everything on the screen
            self.set_calculator_display("")
        elif text == "←":
            # Remove the last character from the screen
            self.set_calculator_display(current_value[:-1])
        else:
            # Add the button's text to the screen
            self.set_calculator_display(current_value + text)

    def set_calculator_display(self, value):
        # Update the calculator display safely
        self.calculator_screen.config(state="normal")  # Allow writing to the display
        self.calculator_screen.delete(0, END)  # Clear the display
        self.calculator_screen.insert(0, value)  # Insert new value
        self.calculator_screen.config(state="readonly")  # Make it read-only again

    def key_press(self, event):
        # This function handles keys pressed on the keyboard
        key = event.char  # Get the key that was pressed
        if key in "0123456789.+-*/%":  # Allow only valid keys
            self.button_click(key)
        elif key == "\r":  # If "Enter" key is pressed, calculate the result
            self.button_click("=")
        elif key == "\b":  # If "Backspace" is pressed, delete last character
            self.button_click("←")

    def run(self):
        # Start the calculator program
        self.window.mainloop()

# It will Create a Calculator and Start it
Calculator().run()
