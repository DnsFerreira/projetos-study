from tkinter import *
from tkinter import ttk

prati = Tk()

prati.title("Praticando 1 2 3...")
prati.geometry("800x500")
prati.maxsize(width= 800, height=500)
prati.config(bg="black")

frame_tela = Frame(prati, width= 800, height= 230, bg= "lightblue")
frame_tela.grid(row=0 , column= 0)

frame_results = Frame(prati, width=700, height=200)
frame_results.grid(row= 0, column=50)

button_pause = Button(frame_tela,text= "PAUSE", font= ("Poppins 11 bold"))
button_pause.place(x=380, y=5, width= 100)



prati.mainloop()