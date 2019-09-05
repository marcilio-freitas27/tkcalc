from tkinter import *

class Calc:
    def __init__(self, master=None):
        # frame top level conteiner
        self.widget = Frame(master)
        self.widget.pack()
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.widget2 = Frame(master)
        self.widget2.pack()
        self.widget3 = Frame(master)
        self.widget3.pack()
        self.widget4 = Frame(master)
        self.widget4.pack()

        # tela
        self.tela = Label(self.widget, text="TK CALC")
        self.tela["font"] = ("verdana","7","bold")
        self.tela["width"] = 30
        self.tela["height"] = 2
        self.tela.pack()

        # tela 1
        self.tela1 = Label(self.widget, text="")
        self.tela1["font"] = ("verdana","7","bold")
        self.tela1["width"] = 10
        self.tela1["height"] = 2
        self.tela1.pack()

        # botões top, linha um
        self.button = Button(self.widget1, text="7")
        self.button.pack(side=LEFT)
        self.button["command"] = self.insert7
        self.button = Button(self.widget1, text='<')
        self.button["command"] = self.backspace
        self.button.pack(side=RIGHT)
        self.button = Button(self.widget1, text='+')
        self.button.pack(side=RIGHT)
        self.button["command"] = self.mais
        self.button = Button(self.widget1, text='9')
        self.button["command"] = self.insert9
        self.button.pack(side=RIGHT)
        self.button = Button(self.widget1, text='8')
        self.button["command"] = self.insert8
        self.button.pack(side=RIGHT)
        

        #botões center, linha 2
        self.button = Button(self.widget2, text='4')
        self.button["command"] = self.insert4
        self.button.pack(side=LEFT)
        self.button = Button(self.widget2, text='%')
        self.button["command"] = self.porcem
        self.button.pack(side=RIGHT)
        self.button = Button(self.widget2, text='-')
        self.button["command"] = self.menos
        self.button.pack(side=RIGHT)
        self.button = Button(self.widget2, text='6')
        self.button["command"] = self.insert6
        self.button.pack(side=RIGHT)
        self.button = Button(self.widget2, text='5')
        self.button["command"] = self.insert5
        self.button.pack(side=RIGHT)

        #botões bottom, linha 3
        self.button = Button(self.widget3, text='1')
        self.button["command"] = self.insert1
        self.button.pack(side=LEFT)
        self.button = Button(self.widget3, text='√')
        self.button["command"] = self.raiz
        self.button.pack(side=RIGHT)
        self.button = Button(self.widget3, text='*')
        self.button["command"] = self.multi
        self.button.pack(side=RIGHT)
        self.button = Button(self.widget3, text='3')
        self.button["command"] = self.insert3
        self.button.pack(side=RIGHT)
        self.button = Button(self.widget3, text='2')
        self.button["command"] = self.insert2
        self.button.pack(side=RIGHT)
        
        #botões bottom2, linha 4
        self.button = Button(self.widget4, text='c')
        self.button["command"] = self.clear
        self.button.pack(side=LEFT)
        self.button = Button(self.widget4, text='=')
        self.button["command"] = self.igual
        self.button.pack(side=RIGHT)
        self.button = Button(self.widget4, text='/')
        self.button["command"] = self.divi
        self.button.pack(side=RIGHT)
        self.button = Button(self.widget4, text='.')
        self.button["command"] = self.insertponto
        self.button.pack(side=RIGHT)
        self.button = Button(self.widget4, text='0')
        self.button["command"] = self.insert0
        self.button.pack(side=RIGHT)
        
       
    # eventos dos botões
    def insert0(self):
        self.tela1["text"] += "0"
    
    def insert7(self):
        self.tela1["text"] += "7"
    
    def insert1(self):
        self.tela1["text"] += "1"
    
    def insert2(self):
        self.tela1["text"] += "2"

    def insert3(self):
        self.tela1["text"] += "3"
    
    def insert4(self):
        self.tela1["text"] += "4"
    
    def insert5(self):
        self.tela1["text"] += "5"

    def insert6(self):
        self.tela1["text"] += "6"
    
    def insert8(self):
        self.tela1["text"] += "8"

    def insert9(self):
        self.tela1["text"] += "9"

    def insertponto(self):
        self.tela1["text"] += "."

    def mais(self):
        self.tela1["text"] += "+"

    def menos(self):
        self.tela1["text"] += "-"

    def multi(self):
        self.tela1["text"] += "*"

    def divi(self):
        self.tela1["text"] += "/"

    def raiz(self):
        self.tela1["text"] = str(int(self.tela1["text"])**0.5)
    
    def porcem(self):
        self.tela1["text"] = str(int(self.tela1["text"])/100)

    def igual(self):
        try:
            self.tela1["text"] = str(eval(self.tela1["text"]))

        except:
            self.tela1["text"] = "ERROR"

    def clear(self):
        self.tela1["text"] = ""

    def backspace(self):
        texto = list(self.tela1["text"])
        texto.remove(texto[len(texto) - 1])
        novo = "".join(texto)
        self.tela1["text"] = novo
        
root = Tk()
Calc(root)
if __name__ == '__main__':
    root.mainloop()
