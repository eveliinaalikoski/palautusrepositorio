# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")
logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}") # muutos confliktissa
print(f"{x} - {y} = {erotus(x, y)}") # muutos confliktissa

logger("lopetetaan ohjelma")
print("goodbye!")