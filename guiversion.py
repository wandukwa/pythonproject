import tkinter as tk

#define mortage function to run upon submit
def submit():
    loan = int(entry_a.get())
    term = int(entry_b.get())
    rate = float(entry_c.get())
    down = int(entry_d.get())

    months = term * 12
    rate_monthly = rate / 100/12
    payment = (rate_monthly / (1-(1 + rate_monthly)))
    result = tk.label(text = "$" + str(round(payment,2)))
    result.pack()


#create tkinter window (GUI)
window = tk.Tk()

#CREATE text and entry boxes

label_a = tk.Label(text = "please enter loan amount: ")
label_a.pack()
entry_a = tk.Entry()
entry_a.pack()
label_b = tk.Label(text = "please enter loan term: ")
label_b.pack()
entry_b = tk.Entry()

entry_b.pack()
label_c = tk.Label(text = "please enter loan rate: ")
label_c.pack()
entry_c = tk.Entry()
entry_c.pack()
label_d = tk.Label(text = "please enter the down payment: ")
label_d.pack()
entry_d = tk.Entry()
entry_d.pack()

#create submit button
mybutton = tk.Button(window, text="Submit", width=10, command=submit)
mybutton.pack()

#run the loop
window.mainloop()

