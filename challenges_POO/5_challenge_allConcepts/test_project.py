from os import system


system('clear')
from Monitor import Monitor
from Keyboard import Keyboard
from Mouse import Mouse
from Computer import Computer
from Order import Order


monitor1 = Monitor('Asus','24 pulgadas')
keyboard1 = Keyboard('USB','Redragon')
mouse1 = Mouse('Blutooth','Logitech')
Computer1 = Computer('Lenovo', monitor1, keyboard1, mouse1)


monitor2 = Monitor('HP','12 pulgadas')
keyboard2 = Keyboard('Blutooth','weibo')
mouse2 = Mouse('USB','iconic')
Computer2 = Computer('McBook',monitor2, keyboard2, mouse2)

Computers1 = (Computer1, Computer2)
Order1 = Order(Computers1)
print(Order1)