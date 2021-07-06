#password generator by Andre de Biasi

import random
import PySimpleGUI as sg

class Generator:
    def __init__(self,length,include,lc,uc,n,s):
        self.length = length #length of password
        self.include = include #characters wanted to be included
        self.lc = lc #num of lowercase characters
        self.uc = uc #num of uppercase characters
        self.n = n #num of number characters
        self.s = s #num of special characters

    def create(self):

        s_count = 0 #num of special characters in include
        uc_count = 0 #num of capital characters in include
        lc_count = 0 #num of lowercase characters in include
        n_count = 0 #num of numbers in include
        for char in self.include: #counts types of characters in include
            test = ord(char)
            if 48 <= test <= 57: #ASCII numbers
                n_count += 1
            elif 65 <= test <= 90: #ASCII uppercase letters
                uc_count += 1
            elif 97 <= test <= 122: #ASCII lowercase letters
                lc_count += 1
            else: #ASCII special characters are all other numbers not already mentioned
                s_count += 1

        while len(self.include) < self.length:
            #will complete lc, up, n, then s constraints
            if lc_count < self.lc: #completing lowercase constrain
                lc_count += 1
                rdm = random.randint(97,122)
            elif uc_count < self.uc: #completing uppercase constraint
                uc_count += 1
                rdm = random.randint(65,90)
            elif n_count < self.n: #completing number constraint
                n_count += 1
                rdm = random.randint(48,57)
            elif s_count < self.s: #completing special characters constraint
                s_count += 1
                while True: #generates random numbers until it is a special character
                    rdm = random.randint(32,126)
                    if 97 <= rdm <= 122 or 65 <= rdm <= 90 or 48 <= rdm <= 57:
                        continue #discards all random numbers that do not result in special characters
                    else:
                        break #if special character number is generated, add to output
            else: #if all other constraints are met, print completely random character
                rdm = random.randint(32,126)
            rdm = chr(rdm) #turn back to character
            self.include += rdm #add to output
        #ends while loop
        l = list(self.include) #turn string into list for easy operations
        random.shuffle(l) #shuffle the list (randomize)
        result = ''.join(l) #shuffled list back to string to print (join list of elements in single quotes)
        window["-PW-"].update(result)
        #return result #this is the password
            #add spaces to the include until is equal to length,
            #shuffle the list, add random values in spots of the spaces in create()

    def check(self):
        s_count = 0 #num of special characters in include
        uc_count = 0 #num of capital characters in include
        lc_count = 0 #num of lowercase characters in include
        n_count = 0 #num of numbers in include
        for char in self.include: #counts types of characters you want to include
            test = ord(char)
            if 48 <= test <= 57:
                n_count += 1
            elif 65 <= test <= 90:
                uc_count += 1
            elif 97 <= test <= 122:
                lc_count += 1
            else:
                s_count += 1

        if uc_count < self.uc: #if the count in include is larger, use that for reference, if not use constraint
            uc_use = self.uc
        else:
            uc_use = uc_count
        if lc_count < self.lc:
            lc_use = self.lc
        else:
            lc_use = lc_count
        if n_count < self.n:
            n_use = self.n
        else:
            n_use = n_count
        if s_count < self.s:
            s_use = self.s
        else:
            s_use = s_count

        if self.length < (uc_use+lc_use+s_use+n_use): #if the constraints cannot be completed due to the number of included characters or the length of password being too short, exit
            print("Your password must be longer to fulfill the constraints, or you must require less constraints")
        else:
            p1.create() #if all constraints can be filled, create the password

#GUI
layout = [[sg.Text("My Password Generator",size=(45,1),justification="center")],
                [sg.Text("Enter password length"), sg.Input(key="-LENGTH-")],
                [sg.Text("Enter characters you want to include"), sg.Input(key="-INCLUDE-")],
                [sg.Text("How many lowercase letters?"), sg.Input(key="-LC-")],
                [sg.Text("How many uppercase letters?"), sg.Input(key="-UC-")],
                [sg.Text("How many numbers?"), sg.Input(key="-NC-")],
                [sg.Text("How many special characters?"), sg.Input(key="-SC-")],
                [sg.Button("GENERATE"),
                #sg.Button("COPY"),
                sg.Button("EXIT")],
                [sg.Text("Generated password: "), sg.Text(size=(30,1), key="-PW-")]]

window = sg.Window("Generator GUI",layout) #create window with layout

while True: #GUI event loop
    event, values = window.read()
    print(event,values)
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    if event == "GENERATE":
        a = int(values["-LENGTH-"])
        b = values["-INCLUDE-"]
        c = int(values["-LC-"])
        d = int(values["-UC-"])
        e = int(values["-NC-"])
        f = int(values["-SC-"])
        p1 = Generator(a, b, c, d, e, f)
        p1.check()
    #if event == "COPY":
    #    sg.clipboard_clear()
    #    sg.clipboard_append(values["-PW-"])
    #    sg.update()
window.close()
