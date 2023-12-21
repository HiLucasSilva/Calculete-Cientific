from tkinter import *
from tkinter import ttk
import math

class Calculadora():

    def __init__(self):
        self.root = Tk()
        self.configureRoot()
        self.setFrame()
        self.setLabels()
        self.setButtons()
        self.setComboBox()
        self.root.mainloop()

    def configureRoot(self):
        self.root.title("Calculadora")
        self.root.geometry("300x390")
        self.root.resizable(FALSE, FALSE)   

    def setFrame(self):
        self.tela = Frame(self.root, width=300, height=100, bg="black")
        self.tela.grid(row=0, column=0)

        self.operacao = Frame(self.root, width=300, height=268)
        self.operacao.grid(row=1, column=0)

        self.corpo = Frame(self.root, width=300, height=268)
        self.corpo.grid(row=2, column=0)

        self.expoente_entry = Entry(self.operacao, width=9)
        self.expoente_entry.grid(row=4, column=2)
 
    def setLabels(self):
        self.lblTela = Label(self.tela, text="", width=32, height=3, padx=6, anchor='e', bd=0, justify=RIGHT, bg="black", fg="#feffff", font=24)
        self.lblTela.place(relx=0, rely=0.2)


    def setButtons(self):
        self.btSen = Button(self.operacao, text="sen", width=10, height=2, relief=RAISED, bg="gray", fg="#feffff", command=lambda: self.calculate_trigonometric("sen"))
        self.btSen.grid(row=0, column=0)

        self.btCos = Button(self.operacao, text="cos", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff", command=lambda: self.calculate_trigonometric("cos"))
        self.btCos.grid(row=0, column=1)

        self.btTan = Button(self.operacao, text="tan", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff", command=lambda: self.calculate_trigonometric("tan"))
        self.btTan.grid(row=0, column=2)

        self.btApagarUmNumero = Button(self.operacao, text="<<", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff", command=self.delete_last_digit)
        self.btApagarUmNumero.grid(row=0, column=3)

        
        self.btlog10 = Button(self.operacao, text="log10", width=10, height=2, relief=RAISED, bg="gray", fg="#feffff", command=self.calculate_log10)
        self.btlog10.grid(row=1, column=0)

        self.btlog = Button(self.operacao, text="log", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff", command=self.calculate_ln)
        self.btlog.grid(row=1, column=1)

        self.btCE = Button(self.operacao, text="CE", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff", command=self.clear_entry)
        self.btCE.grid(row=1, column=2)

        self.btC = Button(self.operacao, text="C", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff", command=self.clear_entry)
        self.btC.grid(row=1, column=3)


        self.btNumAoQuadrado = Button(self.operacao, text="x²", width=10, height=2, relief=RAISED, bg="gray", fg="#feffff", command=self.calculate_square)
        self.btNumAoQuadrado.grid(row=2, column=0)

        self.btNumeroElevadoAOutro = Button(self.operacao, text="^", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff",command=lambda: self.add_to_display("**"))
        self.btNumeroElevadoAOutro.grid(row=2, column=1)

        self.btRaizQuadrada = Button(self.operacao, text="sqrc", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff", command=self.calculate_square_root)
        self.btRaizQuadrada.grid(row=2, column=2)

        self.btDivisao = Button(self.operacao, text="/", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff", command=lambda: self.add_to_display("/"))
        self.btDivisao.grid(row=2, column=3)


        self.bt7 = Button(self.operacao, text="7", width=10, height=2, relief=RAISED , bg="#424345", fg="#feffff", command=lambda: self.add_to_display("7"))
        self.bt7.place(relx=0, rely=0.48)
        self.bt7.grid(row=3, column=0)

        self.bt8 = Button(self.operacao, text="8", width=9, height=2, relief=RAISED , bg="#424345", fg="#feffff", command=lambda: self.add_to_display("8"))
        self.bt8.place(relx=0.2, rely=0.48)
        self.bt8.grid(row=3, column=1)

        self.bt9 = Button(self.operacao, text="9", width=9, height=2, relief=RAISED , bg="#424345", fg="#feffff", command=lambda: self.add_to_display("9"))
        self.bt9.place(relx=0.4, rely=0.48)
        self.bt9.grid(row=3, column=2)

        self.btX = Button(self.operacao, text="X", width=9, height=2, relief=RAISED , bg="gray", fg="#feffff", command=lambda: self.add_to_display("*"))
        self.btX.place(relx=0.6, rely=0.48)
        self.btX.grid(row=3, column=3)


        self.bt4 = Button(self.operacao, text="4", width=10, height=2, relief=RAISED , bg="#424345", fg="#feffff", command=lambda: self.add_to_display("4"))
        self.bt4.place(relx=0., rely=0.64)
        self.bt4.grid(row=4, column=0)

        self.bt5 = Button(self.operacao, text="5", width=9, height=2, relief=RAISED , bg="#424345", fg="#feffff", command=lambda: self.add_to_display("5"))
        self.bt5.place(relx=0.2, rely=0.64)
        self.bt5.grid(row=4, column=1)

        self.bt6 = Button(self.operacao, text="6", width=9, height=2, relief=RAISED , bg="#424345", fg="#feffff",command=lambda: self.add_to_display("6"))
        self.bt6.place(relx=0.4, rely=0.64)
        self.bt6.grid(row=4, column=2)

        self.btSub = Button(self.operacao, text="-", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff", command=lambda: self.add_to_display("-"))
        self.btSub.grid(row=4, column=3)


        self.bt1 = Button(self.operacao, text="1", width=10, height=2, relief=RAISED , bg="#424345", fg="#feffff", command=lambda: self.add_to_display("1"))
        self.bt1.place(relx=0., rely=0.8)
        self.bt1.grid(row=5, column=0)

        self.bt2 = Button(self.operacao, text="2", width=9, height=2, relief=RAISED , bg="#424345", fg="#feffff", command=lambda: self.add_to_display("2"))
        self.bt2.place(relx=0.2, rely=0.8)
        self.bt2.grid(row=5, column=1)

        self.bt3 = Button(self.operacao, text="3", width=9, height=2, relief=RAISED , bg="#424345", fg="#feffff", command=lambda: self.add_to_display("3"))
        self.bt3.place(relx=0.4, rely=0.8)
        self.bt3.grid(row=5, column=2)

        self.btPlus = Button(self.operacao, text="+", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff", command=lambda: self.add_to_display("+"))
        self.btPlus.grid(row=5, column=3)


        self.btPorcentagem = Button(self.operacao, text="%", width=10, height=2, relief=RAISED, bg="gray", fg="#feffff", command=self.calculate_percent)
        self.btPorcentagem.grid(row=6, column=0)

        self.bt0= Button(self.operacao, text="0", width=9, height=2, relief=RAISED , bg="#424345", fg="#feffff", command=lambda: self.add_to_display("0"))
        self.bt0.place(relx=0.2, rely=0.96)
        self.bt0.grid(row=6, column=1)

        self.btVirgula = Button(self.operacao, text=",", width=9, height=2, relief=RAISED, bg="gray", fg="#feffff", command=lambda: self.add_to_display("."))
        self.btVirgula.grid(row=6, column=2)

        self.btIgual = Button(self.operacao, text="=", width=9, height=2, relief=RAISED, bg="cyan", fg="#feffff", command=self.calculate_result)
        self.btIgual.grid(row=6, column=3)

    def setComboBox(self):
        self.unit_var = StringVar()
        self.unit_combobox = ttk.Combobox(self.root, textvariable=self.unit_var, values=["Graus", "Radianos"])
        self.unit_combobox.place(relx=0, rely=0.20)
        self.unit_combobox.current(0)

    def add_to_display(self, value):
        current_text = self.lblTela.cget("text")
        self.lblTela.config(text=current_text + value)

    def calculate_result(self):
        try:
            expression = self.lblTela.cget("text")
            result = eval(expression)
            self.lblTela.config(text=str(result))
        except Exception as e:
            self.lblTela.config(text="Erro")

    def calculate_trigonometric(self, func):
        try:
            value = float(self.lblTela.cget("text"))
            result = None
            if func == "sen":
                result = math.sin(math.radians(value))
            elif func == "cos":
                result = math.cos(math.radians(value))
            elif func == "tan":
                result = math.tan(math.radians(value))
            self.lblTela.config(text=str(result))
        except Exception as e:
            self.lblTela.config(text="Erro")

    def calculate_exponent(self):
        try:
            value = float(self.lblTela.cget("text"))
            exponent = float(self.expoente_entry.get())
            result = value ** exponent
            self.lblTela.config(text=str(result))
        except Exception as e:
            self.lblTela.config(text="Erro")

    def clear_entry(self):
        self.lblTela.config(text="")

    def delete_last_digit(self):
        current_text = self.lblTela.cget("text")
        updated_text = current_text[:-1]  
        self.lblTela.config(text=updated_text)

    def calculate_square_root(self):
        try:
            value = float(self.lblTela.cget("text"))
            result = math.sqrt(value)
            self.lblTela.config(text=str(result))
        except Exception as e:
            self.lblTela.config(text="Erro")

    def calculate_log10(self):
        try:
            value = float(self.lblTela.cget("text"))
            result = math.log10(value)
            self.lblTela.config(text=str(result))
        except Exception as e:
            self.lblTela.config(text="Erro")

    def calculate_ln(self):
        try:
            value = float(self.lblTela.cget("text"))
            result = math.log(value)
            self.lblTela.config(text=str(result))
        except ValueError:
            self.lblTela.config(text="Erro: valor negativo para ln")
        except Exception as e:
            self.lblTela.config(text="Erro")

    def calculate_square(self):
        try:
            value = float(self.lblTela.cget("text"))
            result = value ** 2
            self.lblTela.config(text=str(result))
        except Exception as e:
            self.lblTela.config(text="Erro")        

    def calculate_percent(self):
        try:
            value = float(self.lblTela.cget("text"))
            result = value / 100
            self.lblTela.config(text=str(result))
        except Exception as e:
            self.lblTela.config(text="Erro")
 
Calculadora()       