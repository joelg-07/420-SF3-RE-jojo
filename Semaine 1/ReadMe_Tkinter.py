from tkinter import Tk, Button, Label
from random import random, randint, choice, choices


class Tkinter(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sagesse")
        citation = self.creer_citation()
        self.label = Label(text=f"{citation}")
        self.label.pack()

        self.bouton = Button(text="Fermer", command=self.fermer_application)
        self.bouton.pack()

    def fermer_application(self):
        self.destroy()

    def creer_citation(self):
        liste_citation = []
        with open("citations.txt", mode= "r", encoding="UTF-8") as file :
            for ligne in file:
                liste_citation.append(f"{ligne}")

        citation_choix = choice(liste_citation)

        return citation_choix


# Creation de la fenêtre
application = Tkinter()
# Boucle principale
application.mainloop()


