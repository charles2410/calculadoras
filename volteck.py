import sys
import time

#funciones
def calibre8(a):
    factor=9.98/100
    x=a/factor
    return x
def calibre10(a):
    factor=5.97/100
    x=a/factor
    return x
def calibre12(a):
    factor=4.02/100
    x=a/factor
    return x
def calibre14(a):
    factor=2.77/100
    x=a/factor
    return x
def quit():
    print("Salir....")
    time.sleep(2)
    sys.exit()
def getnum():
    a= float(input("Introduce el peso del cable:  "))
    return a

#esta es la funcion principal del menu
def menu():
    #
    #print("***Main menu")
    time.sleep(1)

choice=input(""" 
    Menu Principal
    
    A: Calibre 8
    B: Calibre 10
    C: Calibre 12
    D: Calibre 14
    E: Salir
    Escoge la opcion 
        """)

if choice== "A" or choice=="a":
    num1=getnum()
    total= calibre8(num1)
    print("Tienes", total,  "Metros")
elif choice =="B" or choice =="b":
    num1 =getnum()
    total=calibre10(num1)
    print("Tienes", total,  "Metros")
elif choice =="C" or choice =="c":
    num1=getnum()
    total=calibre12(num1)
    print("Tienes", total,  "Metros")
elif choice=="D" or choice =="d":
    num1=getnum()
    total=calibre14(num1)
    print("Tienes ", total, "Metros" )
elif choice =="E" or choice =="e":
     quit()
else:
    print("Escoge una opcion correcta")
    



        





