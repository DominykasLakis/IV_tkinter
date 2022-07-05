from datetime import datetime
from tkcalendar import DateEntry
from tkinter import *
from duomenys2 import *


langas = Tk()
langas.title("IV Skaičiuoklė")
var = IntVar()
sizex = 600
sizey = 400
posx = 40
posy = 20


def ideti():
     with open(failas_duomenys, 'wb') as irasymas:
        ivesti = float(ivedimo_langas.get()), datos_ivedimas.get()
        sarasas.append(ivesti)
        pickle.dump(sarasas, irasymas)
        langeliai()


def visi():
    for viskas in sarasas:
        visi_irasai.insert(0, viskas)


def istrinti():
    pasirinkti = visi_irasai.curselection()
    for pasirinkti in pasirinkti:
        visi_irasai.delete(pasirinkti)
        for pasirinkti in pasirinkti(sarasas):
            sarasas.remove([pasirinkti])


def langeliai():
    ivedimo_langas.delete(0, END)
    saraso_sumos_langelis.delete(0, END)
    saraso_sumos_langelis.insert(END, saraso_suma())
    saugus_balanso_langelis.delete(0, END)
    saugus_balanso_langelis.insert(0, saugus_balansas())
    atideta_mokesciams_langelis.delete(0, END)
    atideta_mokesciams_langelis.insert(0, atideta_mokesciams())
    visi_irasai.delete(0, END)
    visi_irasai.insert(0, visi())


pajamu_ivedimas = Label(langas, text="Įvesti datą ir pajamas ")
datos_ivedimas = DateEntry(langas,bg="darkblue",fg="white", date=datetime.now)
ivedimo_langas = Entry(langas)
mygtukas = Button(langas, text="Įvesti", command=ideti)
istrinimas = Button(langas, text="Ištrinti", command=istrinti)
Listbox(langas)
visi_irasai = Listbox(width=20,height=10,font=('times',12))
visi_irasai.insert(0, visi())


saraso_sumos_tekstas = Label(langas, text="Visų pajamų suma €")
saraso_sumos_langelis = Entry(langas)
saraso_sumos_langelis.insert(0, saraso_suma())


balansas = Label(langas, text="Saugus balansas €")
saugus_balanso_langelis = Entry(langas)
saugus_balanso_langelis.insert(0, saugus_balansas())


atideta = Label(langas, text="Atidėta mokesčiams €")
atideta_mokesciams_langelis = Entry(langas)
atideta_mokesciams_langelis.insert(0, atideta_mokesciams())


soc_dr = Label(langas, text="PSD")
soc_dr_langas = Listbox(langas)
soc_dr_langas.insert(0, draudimas())
soc_dr_langas.place(x=250, y=110, width=180, height=20)
soc_l = Label(langas, bg='white', width=20, text='51.5€')
soc = Button(langas, text="Sumokejau", command=sumoketa)


pajamu_ivedimas.grid(row=2, column=0)
datos_ivedimas.grid(row=2, column=1)
ivedimo_langas.grid(row=2, column=2)
mygtukas.grid(row=2, column=3)
saraso_sumos_tekstas.grid(row=3, column=0)
saraso_sumos_langelis.grid(row=3, column=1)
balansas.grid(row=4, column=0)
saugus_balanso_langelis.grid(row=4, column=1)
atideta.grid(row=5, column=0)
atideta_mokesciams_langelis.grid(row=5, column=1)
visi_irasai.grid(row=6, column=0)
istrinimas.grid(row=7, column=0)
soc_dr.grid(row=6, column=1)
soc_l.grid(row=6, column=2)
soc.grid(row=6, column=3)
langas.mainloop()

