import math
def cuadrado():
	lado = int(input("INGRESE LADO: "))
	perimetro = lado*4
	area = lado * lado
	print("EL PERIMETRO ES: "+ str(perimetro))
	print("EL AREA ES: "+str(area))

def triangulo():
	base = int(input("INGRESE LA BASE: "))
	altura = int(input("INGRESE LA ALTURA: "))
	l1 = int(input("INGRESE LADO 1: "))
	l2 = int(input("INGRESE LADO 2: "))
	area = (base*altura)/2
	perimetro = l1 + l2 + base
	print("EL PERIMETRO ES: "+ str(perimetro))
	print ("EL AREA DEL TRIANGULO ES: "+str(area))

def pentagono():
	lado= int(input("INGRESE EL LADO: "))
	radio= int(input("INGRESE EL RADIO: "))
	apotema=math.sqrt((radio*radio)-(1/2*1/2))
	perimetro=lado*radio
	area=(perimetro*apotema)/2
	print("EL PERIMETRO ES: "+ str(perimetro))
	print ("EL AREA ES: "+str(area))
	
	
a = int (input("INGRESE NUMERO DE LADOS DE SU FIGURA: "))
if (a == 1 or a == 2):
	print ("NO EXISTE FIGURA")
if (a == 3):
	print ("SU FIGURA ES UN TRIANGULO")
	triangulo()
if (a == 4):
    print ("SU FIGURA ES UN CUADRADO: ") 
    cuadrado()
if (a == 5):
    print ("SU FIGURA ES UN PENTAGONO: ") 
    pentagono()

