from tkinter import *
from tkinter import ttk

cor1= "#3b3b3b"
cor2= "#feffff"
cor3= "#38576b"
cor4= "#ECEFF1"
cor5= "#FFAB40"


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg= cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width= 235, height= 268)
frame_corpo.grid(row=1, column=0)

#------------ variavel todos valores -----------------------#
 
todos_valores = ""

#----------------- create fuction ---------------------------#

def entrar_valores(event):

    global todos_valores 

    todos_valores = todos_valores + str(event)

#------------------ passar valor para tela ------------------#
    valor_text.set(todos_valores)

#---------------- fuction calcular --------------------------#
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_text.set(str(resultado))

#-------------------limpar tela -----------------------------#
def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_text.set("")
#----------------------- create label -----------------------#
valor_text = StringVar()
app_label = Label(frame_tela, textvariable= valor_text, width= 16, height= 2, padx=7, relief= FLAT, anchor= "e", justify=RIGHT, font= ("Ivy 18"), bg= cor3, fg= "white")
app_label.place(x=0, y=0)


#-------------create_button----------------------#
clean_button = Button(frame_corpo, command= limpar_tela, text="C", width=11, height=2, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
clean_button.place(x=0, y=0)

porce_button = Button(frame_corpo, command= lambda:entrar_valores("%"), text="%", width=5, height=2, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
porce_button.place(x=118, y=0)

divi_button = Button(frame_corpo, command= lambda:entrar_valores("/"), text="/", width=5, height=2, bg= cor5, fg= cor2, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
divi_button.place(x=177, y=0)



sete_button = Button(frame_corpo, command= lambda:entrar_valores("7"), text="7", width=5, height=2, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
sete_button.place(x=0, y=52)

oito_button = Button(frame_corpo, command= lambda:entrar_valores("8"), text="8", width=5, height=2, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
oito_button.place(x=59, y=52)

nove_button = Button(frame_corpo, command= lambda:entrar_valores("9"), text="9", width=5, height=2, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
nove_button.place(x=118, y=52)

aste_button = Button(frame_corpo, command= lambda:entrar_valores("*"), text="*", width=5, height=2, bg= cor5, fg= cor2, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aste_button.place(x=177, y=52)



quatro_button = Button(frame_corpo, command= lambda:entrar_valores("4"), text="4", width=5, height=2, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
quatro_button.place(x=0, y=104)

cinco_button = Button(frame_corpo, command= lambda:entrar_valores("5"), text="5", width=5, height=2, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
cinco_button.place(x=59, y=104)

seis_button = Button(frame_corpo, command= lambda:entrar_valores("6"), text="6", width=5, height=2, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
seis_button.place(x=118, y=104)

menos_button = Button(frame_corpo, command= lambda:entrar_valores("-"), text="-", width=5, height=2, bg= cor5, fg= cor2, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
menos_button.place(x=177, y=104)


um_button = Button(frame_corpo, command= lambda:entrar_valores("1"), text="1", width=5, height=2, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
um_button.place(x=0, y=156)

dois_button = Button(frame_corpo, command= lambda:entrar_valores("2"), text="2", width=5, height=2, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
dois_button.place(x=59, y=156)

tres_button = Button(frame_corpo, command= lambda:entrar_valores("3"), text="3", width=5, height=2, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
tres_button.place(x=118, y=156)

mais_button = Button(frame_corpo, command= lambda:entrar_valores("+"), text="+", width=5, height=2, bg= cor5, fg= cor2, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
mais_button.place(x=177, y=156)


um_button = Button(frame_corpo, command= lambda:entrar_valores("0"), text="0", width=11, height=3, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
um_button.place(x=0, y=208)

um_button = Button(frame_corpo, command= lambda:entrar_valores("."), text=".", width=5, height=3, bg= cor4, font= ("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
um_button.place(x=118, y=208)

um_button = Button(frame_corpo, command= calcular, text="=", width=5, height=3, bg= cor4, font= ("Ivy 13  bold"), relief=RAISED, overrelief=RIDGE)
um_button.place(x=177, y=208)





janela.mainloop()