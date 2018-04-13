from Tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

fenetre.mainloop()
