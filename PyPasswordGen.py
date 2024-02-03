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
import string
import secrets
import re
import random

#Setup GUI Parameters
master = t.Tk()
master.title('Password Generator')
master.geometry("500x200")

generated_pass = ""

#Add Labels
t.Label(master, text="Length:").grid(row=0)
t.Label(master, text="Type:").grid(row=1)
t.Label(master, text="Symbols:").grid(row=2)
t.Label(master, text="Numbers:").grid(row=3)
t.Label(master, text="Capitals:").grid(row=4)

#Create Text Entries
entry_length = t.Entry(master)
entry_symbols = t.Entry(master)
entry_numbers = t.Entry(master)
entry_captial = t.Entry(master)
#Line them up on grid
entry_length.grid(row=0, column=1)
entry_symbols.grid(row=2, column=1)
entry_numbers.grid(row=3, column=1)
entry_captial.grid(row=4, column=1)


#Create Mode Selectors
CBNumbers = t.BooleanVar()
CBSymbols = t.BooleanVar()

Bletters_numbers = t.Checkbutton(master, text="Numbers", variable=CBNumbers, onvalue=True, offvalue=False).grid(row=1,column=1)
Bletters_numbers_Symbols = t.Checkbutton(master, text="Symbols", variable=CBSymbols, onvalue=True, offvalue=False).grid(row=1,column=2
                                                                                                                   )
def setPass():
    global generated_pass
    print(generated_pass)
    pass

#Generate Password Gen Function and logic

def genPass():
    #Grab User Inputs and Desired State
    Length = int(entry_length.get() or 0)
    BNums = CBNumbers.get()
    BSyms = CBSymbols.get()
    Numbers = int(entry_numbers.get() or 0)
    Symbols = int(entry_symbols.get() or 0)
    Capitals = int(entry_captial.get() or 0)


    global generated_pass

    print("Calling the Password Generator", Length, BNums, BSyms, Symbols, Numbers, Capitals)
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    if Length == 0:
        generated_pass = ""
        setPass()
        return
    if not BSyms:
        Symbols = 0
    if not BNums:
        Numbers = 0

    Lower = Length - BNums - BSyms - Numbers - Capitals
    char_selection = letters
    if BNums:
        char_selection += digits
    if BSyms:
        char_selection += symbols
    print(char_selection)
    
    while True:
        temp_pass = ""
        temp_select = ""
        for _ in range(Numbers):
            temp_select += secrets.choice(digits)
        for _ in range(Symbols):
                temp_select += secrets.choice(symbols)
        for _ in range(Capitals):
                temp_select += secrets.choice(letters.upper())
        for _ in range(Lower):
                temp_select += secrets.choice(letters.lower())
        #for _ in range(Length):
        #temp_pass = "".join(random.sample(temp_select, Length))
        temp_List = list(temp_select)
        random.shuffle(temp_List)
        temp_pass = "".join(temp_List)

        constraints = [
            (Numbers, r'\d'),
            (Symbols, fr'[{symbols}]'),
            (Capitals, r'[A-Z]'),
            (Lower, r'[a-z]')
        ]

        if all(
            constraint <= len(re.findall(pattern, temp_pass))
            for constraint, pattern in constraints
        ):
            generated_pass = temp_pass
            break
        print(temp_pass)
    
    setPass()
    return



#Generate Button
gen_button = t.Button(master, bg='RED', text="Generate!", width=25, 
                      command=genPass).grid(row=5)
master.mainloop()


