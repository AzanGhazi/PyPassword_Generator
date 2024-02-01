"""
To satisfy this project 

1) Create a nice GUI that asks for the following conditions
    - Password Length
    - Choice between (only letters, letters and numbers, letters + nums + symbols)
    - Min Symbols (Optional)
    - Min Numbers (Optional)
    - Min Capitals (Optional)

"""
import tkinter as t

#Setup GUI Parameters
master = t.Tk()
master.title('Password Generator')
master.geometry("500x200")

#Add Labels
t.Label(master, text="Length:").grid(row=0)
t.Label(master, text="Type:").grid(row=1)
t.Label(master, text="Symbols:").grid(row=2)
t.Label(master, text="Numbers:").grid(row=3)
t.Label(master, text="Capitals:").grid(row=4)

#Create Text Entries
entry_length = t.Entry(master).grid(row=0, column=1)
entry_symbols = t.Entry(master).grid(row=2, column=1)
entry_numbers = t.Entry(master).grid(row=3, column=1)
entry_captial = t.Entry(master).grid(row=4, column=1)

#Create Mode Selectors
CBNumbers = t.IntVar()
CBSymbols = t.IntVar()

Bletters_numbers = t.Checkbutton(master, text="Numbers", variable=CBNumbers, onvalue=1, offvalue=0).grid(row=1,column=1)
Bletters_numbers_Symbols = t.Checkbutton(master, text="Symbols", variable=CBSymbols, onvalue=1, offvalue=0).grid(row=1,column=2)

#Generate Button
gen_button = t.Button(master, bg='RED', text="Generate!", width=25, command=master.destroy).grid(row=5)
master.mainloop()


