import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.config(bg="#2c3e50")


# Global variable to store the current expression
expression = ""

def updateExpression(value):
    global expression
    if value == "*":
        expression += "*" 
        entry_box.insert(tk.END, 'x')
    elif value == "/":
       expression += "/" 
       entry_box.insert(tk.END, '÷')
    else:
       expression += str(value)
       entry_box.insert(tk.END, value)
    

def evaluteExpression():
    global expression
    try:
        result = str(eval(expression))
        entry_box.delete(0,tk.END)
        entry_box.insert(tk.END,result)
        expression = result
    except ZeroDivisionError:
        entry_box.delete(0, tk.END)
        entry_box.insert(tk.END, "NOT DEFINED")
        expression = ""
    except Exception :
        entry_box.delete(0,tk.END)
        entry_box.insert(tk.END,"Error")
        expression = ""

def clearDisplay():
    global expression
    expression = ""
    entry_box.delete(0,tk.END)

def erase():
    global expression
    expression = expression[:-1]
    entry_box.delete(0,tk.END)
    entry_box.insert(tk.END,expression)

def percentage():
    global expression
    # Check if there's a number to calculate percentage on
    if expression:
        try:
            # Find the last operand in the expression
            last_number = ""
            for i in range(len(expression) - 1, -1, -1):
                if expression[i] in "+-*/":
                    last_number = expression[i + 1:]
                    base_expression = expression[:i + 1]
                    break
            else:
                # If no operator is found, treat the entire expression as the last number
                last_number = expression
                base_expression = ""

            # Convert the last operand to a percentage of the preceding expression
            if base_expression:
                percentage_value = str(float(base_expression.rstrip("+-*/")) * float(last_number) / 100)
                expression = base_expression + percentage_value
            else:
                percentage_value = str(float(last_number) / 100)
                expression = percentage_value
            
            entry_box.delete(0, tk.END)
            entry_box.insert(tk.END, expression)
        except ValueError:
            entry_box.delete(0, tk.END)
            entry_box.insert(tk.END, "Error")
            expression = ""


entry_box = tk.Entry(root,bg="lightblue",font=("Arial",40),justify="right")
entry_box.place(x=0,y=0,width=400,height=100)

button_cancel = tk.Button(root,text="C",bg="#e74c3c",fg="white",font=("Arial",40),command= clearDisplay)
button_cancel.place(x=0,y=100,width=100,height=100)

button_divide = tk.Button(root,text="➗",bg="#3498db",fg="white",font=("Arial",30),command=lambda: updateExpression('/'))
button_divide.place(x=100,y=100,width=100,height=100)

button_multiply = tk.Button(root,text="X",bg="#3498db",fg="white",font=("Arialbold",40),command= lambda:updateExpression('*'))
button_multiply.place(x=200,y=100,width=100,height=100)

button_clear = tk.Button(root,text="Clear",bg="#3498db",fg="white",font=("Arialbold",25),command= erase)
button_clear.place(x=300,y=100,width=100,height=100)



button_7 = tk.Button(root,text="7",bg="lightyellow",font=("Arial",40),command=lambda: updateExpression(7))
button_7.place(x=0,y=200,width=100,height=100)

button_8 = tk.Button(root,text="8",bg="lightyellow",font=("Arial",40),command=lambda: updateExpression(8))
button_8.place(x=100,y=200,width=100,height=100)

button_9 = tk.Button(root,text="9",bg="lightyellow",font=("Arial",40),command=lambda: updateExpression(9))
button_9.place(x=200,y=200,width=100,height=100)

button_minus = tk.Button(root,text="-",bg="#3498db",fg="white",font=("Arialbold",60),command=lambda: updateExpression('-'))
button_minus.place(x=300,y=200,width=100,height=100)



button_4 = tk.Button(root,text="4",bg="lightyellow",font=("Arial",40),command=lambda: updateExpression(4))
button_4.place(x=0,y=300,width=100,height=100)

button_5 = tk.Button(root,text="5",bg="lightyellow",font=("Arial",40),command=lambda: updateExpression(5))
button_5.place(x=100,y=300,width=100,height=100)

button_6 = tk.Button(root,text="6",bg="lightyellow",font=("Arial",40),command=lambda: updateExpression(6))
button_6.place(x=200,y=300,width=100,height=100)

button_plus = tk.Button(root,text="+",bg="#3498db",fg="white",font=("Arialbold",50),command=lambda: updateExpression('+'))
button_plus.place(x=300,y=300,width=100,height=100)


button_1 = tk.Button(root,text="1",bg="lightyellow",font=("Arial",40),command=lambda: updateExpression(1))
button_1.place(x=0,y=400,width=100,height=100)

button_2 = tk.Button(root,text="2",bg="lightyellow",font=("Arial",40),command=lambda: updateExpression(2))
button_2.place(x=100,y=400,width=100,height=100)

button_3 = tk.Button(root,text="3",bg="lightyellow",font=("Arial",40),command=lambda: updateExpression(3))
button_3.place(x=200,y=400,width=100,height=100)

button_equal = tk.Button(root,text="=",bg="#2ecc71",fg="white",font=("Arialbold",40),command= evaluteExpression)
button_equal.place(x=300,y=400,width=100,height=200)

button_percent = tk.Button(root,text="%",bg="lightyellow",font=("Arial",40),command=percentage)
button_percent.place(x=0,y=500,width=100,height=100)

button_0 = tk.Button(root,text="0",bg="lightyellow",font=("Arial",40),command=lambda: updateExpression(0))
button_0.place(x=100,y=500,width=100,height=100)

button_point = tk.Button(root,text=".",bg="lightyellow",font=("Arialbold",40),command=lambda: updateExpression('.'))
button_point.place(x=200,y=500,width=100,height=100)




root.mainloop()