from tkinter import *
import tkinter.font as tkFont
import CalculateAnswer as CA

class App:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack(fill=BOTH,expand=1)
        self.fontStyle = tkFont.Font(family="Helvetica",size=15,weight="bold")  #Creates the font style
        self.fontStyle2 = tkFont.Font(family="Roboto Medium", size=10)  #Creates the font style
        

        self.entryBoxesV = []
        self.infoPosV = 0
        self.infoV = []
        self.finalInfoV = []
        self.columnPosV = 2

   
        self.entryBoxesM = []
        self.infoPosM = 0
        self.infoM = []
        self.finalInfoM = []
        self.columnPosM = 5

        self.answer = StringVar()


        self.addEntryV()
        self.addEntryM()


        Label(self.frame, text='Enter in the Variable Names:', font=self.fontStyle).grid(row =0, column =0,sticky=W+E+N+S, padx=10)    
        Button(self.frame, text='+', height=1, width=3, command=self.addEntryV).grid(row=0, column=1, sticky=W+E+N+S)    
        Button(self.frame, text='-', height=1, width=3, command=self.removeEntryV).grid(row=1, column=1, sticky=W+E+N+S)


        Label(self.frame, text = 'Enter in the Minterms:', font = self.fontStyle).grid(row = 0, column = 3, sticky = W+E+N+S, padx=10)    
        Button(self.frame, text = '+', height = 1, width = 3, command = self.addEntryM).grid(row = 0, column = 4, sticky = W+E+N+S)    
        Button(self.frame, text = '-', height = 1, width = 3, command = self.removeEntryM).grid(row = 1, column = 4, sticky = W+E+N+S)


        Button(self.frame, text = 'Simplify', font = self.fontStyle2, command = self.submitData, width = 10).grid(row = 1, column = 0, sticky = N)


        Label(self.frame, text='Answer:', font = self.fontStyle).grid(row = 0, column = 6, sticky=W+E+N+S, padx=10)
        Entry(self.frame, textvariable = self.answer, font = self.fontStyle, width = 35).grid(row = 0, column = 7, sticky = W+E+N+S)

        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(2,weight=1)
        self.frame.columnconfigure(3,weight=1)
        self.frame.columnconfigure(5,weight=1)
        self.frame.columnconfigure(6,weight=1)
        
    def addEntryV(self):
        self.entryBoxesV, self.infoPosV, self.infoV = self.addEntry(self.entryBoxesV, self.infoPosV, self.infoV, self.columnPosV)

    def removeEntryV(self):
        self.entryBoxesV, self.infoPosV, self.infoV = self.removeEntry(self.entryBoxesV, self.infoPosV, self.infoV)

    def addEntryM(self):
        self.entryBoxesM, self.infoPosM, self.infoM = self.addEntry(self.entryBoxesM, self.infoPosM, self.infoM, self.columnPosM)

    def removeEntryM(self):
        self.entryBoxesM, self.infoPosM, self.infoM = self.removeEntry(self.entryBoxesM, self.infoPosM, self.infoM)

    def addEntry(self,entryBoxes,infoPos,info, columnPos):
        a = StringVar()
        entry = Entry(self.frame, textvariable = a, font = self.fontStyle, width = 5)
        entry.grid(row = infoPos, column = columnPos, sticky = W+E+N+S)
        entryBoxes.append(entry)
        info.append(a)
        infoPos = infoPos + 1
        return entryBoxes, infoPos, info

    def removeEntry(self,entryBoxes,infoPos,info):
        if(len(entryBoxes) > 1):
            entryBoxes[infoPos-1].destroy()
            entryBoxes.pop(infoPos-1)
            info.pop(infoPos-1)
            infoPos = infoPos - 1
        return entryBoxes, infoPos, info

    def submitData(self):
        self.finalInfoV = []
        self.finalInfoM = []
        checkMinterms = True
        
        for i in range(0,len(self.infoV)):
            self.finalInfoV.append(self.infoV[i].get())
        
        for i in range(0,len(self.infoM)):
            minterm = self.infoM[i].get()
            self.finalInfoM.append(minterm)

                
        if(self.finalInfoV[0] != '' and self.finalInfoM[0] != '' and checkMinterms == True):
            self.answer.set(CA.runModel(self.finalInfoV, self.finalInfoM))  
