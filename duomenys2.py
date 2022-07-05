import pickle, os
from datetime import date


sarasas = []
failas_duomenys = 'duomenys.dat'


if os.path.exists(failas_duomenys):
    with open(failas_duomenys, 'rb') as skaitymas:
        sarasas = pickle.load(skaitymas)

def saraso_suma():
    sumos = [x[0] if isinstance(x, tuple)else x for x in sarasas]
    suma = sum(sumos)
    return float(suma)

def saugus_balansas():
    if saraso_suma() < 3500:
        return round(saraso_suma() - psd() - vsd())
    else:
        return round(saraso_suma() - psd() - vsd() - gpm())

def vsd():
    return saraso_suma() // 100 * 12.52

def psd():
    return saraso_suma() // 100 * 6.98

def gpm():
    return saraso_suma() // 100 * 5

def atideta_mokesciams():
    return round(saraso_suma() - saugus_balansas())

def draudimas():
    siandien = date.today()
    if siandien.day == 1:
        return "Mėnesio pradžia, sumokėti PSD"

def sumoketa():
    if draudimas():
        return saraso_suma() - 51.5