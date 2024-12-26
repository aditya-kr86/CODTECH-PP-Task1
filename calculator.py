from tkinter import *

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")

        # Disable direct typing in the display
        self.calculator_screen = Entry(self.window, width=25, borderwidth=5, state="readonly", readonlybackground="white")
        self.calculator_screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Bind keypress events
        self.window.bind("<Key>", self.key_press)

        # Create buttons
        button_list = [
            "AC", "←", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "=",
        ]
        row = 1
        col = 0
        for button_text in button_list:
            color = "Red" if not button_text.isdigit() and button_text != "." else "black"
            button = Button(
                self.window,
                text=button_text,
                width=5,
                height=2,
                fg=color,
                command=lambda text=button_text: self.button_click(text),
            )
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
        created_by = Label()

    def button_click(self, text):
        # Handle button clicks
        current_value = self.calculator_screen.get()
        if text == "=":
            try:
                result = str(eval(current_value))
                self.set_calculator_display(result)
            except:
                self.set_calculator_display("Error")
        elif text == "AC":
            self.set_calculator_display("")
        elif text == "←":
            self.set_calculator_display(current_value[:-1])
        else:
            self.set_calculator_display(current_value + text)

    def set_calculator_display(self, value):
        # Set value in the display
        self.calculator_screen.config(state="normal")
        self.calculator_screen.delete(0, END)
        self.calculator_screen.insert(0, value)
        self.calculator_screen.config(state="readonly")

    def key_press(self, event):
        # Handle keypress events
        key = event.char
        if key in "0123456789.+-*/%":
            self.button_click(key)
        elif key == "\r":  # Enter key
            self.button_click("=")
        elif key == "\b":  # Backspace
            self.button_click("←")

    def run(self):
        # Start the main loop
        self.window.mainloop()


# It will Create a Calculator and Start it
Calculator().run()
