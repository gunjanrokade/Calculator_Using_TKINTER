import tkinter as  tk 
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")


        self.total_expression = ""
        self.current_expression = ""


        # creating objects for functions
        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()
        self.label1, self.label2 = self.create_display_labels()

        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            '.':(4,1), 0:(4,2),
        }

        self.operators = {'/':'\u00F7', '*':'\u00D7', '-':'-', '+':'+'}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_buttons()
        self.create_equal_buttons() 
        self.create_square_button()
        self.create_squareroot_button()

        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight = 1)
            self.button_frame.columnconfigure(x, weight = 1)
    # end of main function


    #other functions 
    def create_display_labels(self):
        label1 = tk.Label(self.display_frame, text = self.total_expression, anchor = tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        label1.pack(expand=True, fill='both')
        label2 = tk.Label(self.display_frame, text = self.current_expression, anchor = tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label2.pack(expand=True, fill='both')
        return label1, label2

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame 

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both") 
        return frame

    # add expressions to add given values to the current_expression
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label2()

    def append_expression(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.update_label1()
        self.update_label2()

    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_label1()
        self.update_label2()
        

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_label1()
        self.current_expression = str(eval(self.total_expression))
        self.update_label2()
        self.total_expression = ''

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text = str(digit), bg=WHITE, fg = LABEL_COLOR, borderwidth='0', 
                        font = DIGITS_FONT_STYLE, command = lambda x=digit: self.add_to_expression(x))
            button.grid(row = grid_value[0], column = grid_value[1], sticky = tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, value in self.operators.items():
            button = tk.Button(self.button_frame, text = value, bg = OFF_WHITE, borderwidth = '0',
             font = DEFAULT_FONT_STYLE,command = lambda x=operator: self.append_expression(x))
            button.grid(row =i, column =4, sticky = tk.NSEW)
            i+=1

    def create_clear_buttons(self):
        button = tk.Button(self.button_frame, text = 'C', bg=WHITE, fg = LABEL_COLOR, borderwidth='0', 
                        font = DIGITS_FONT_STYLE, command = self.clear)
        button.grid(row = 0, column = 1, sticky = tk.NSEW)

    def create_equal_buttons(self):
        button = tk.Button(self.button_frame, text = '=', bg=LIGHT_BLUE, fg = LABEL_COLOR, borderwidth='0', 
                        font = DIGITS_FONT_STYLE, command = self.evaluate )
        button.grid(row = 4, column = 3, columnspan = 2,sticky = tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label2()

    def create_square_button(self):
        button = tk.Button(self.button_frame, text = 'x\u00b2', bg=WHITE, fg = LABEL_COLOR, borderwidth='0', 
                        font = DIGITS_FONT_STYLE, command = self.square)
        button.grid(row = 0, column = 2, sticky = tk.NSEW)

    def squareroot(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label2()

    def create_squareroot_button(self):
        button = tk.Button(self.button_frame, text = '\u221ax', bg=WHITE, fg = LABEL_COLOR, borderwidth='0', 
                        font = DIGITS_FONT_STYLE, command = self.squareroot)
        button.grid(row = 0, column = 3, sticky = tk.NSEW)

    def update_label1(self):
        self.label1.config(text = self.total_expression)

    def update_label2(self):
        self.label2.config(text = self.current_expression)

    def run(self):
        self.window.mainloop()

if __name__=="__main__":
    calc =Calculator()
    calc.run()

    