import parser_yacc
import os

def menu():
    opcion = 0
    while (opcion != 3):
        print('''MENU ANALIZADOR SINTÁCTICO
         \t1: Línea de código
         \t2: Leer archivo.c++
         \t3: Salir''')
        opcion = int(input("opcion: "))
        if opcion == 1:
            linea = input("Ingrese una línea de código c++: \n")
            if (linea): 
                parser_yacc.call_Parse(linea)
            else:
                print("\nIngrese código c++ válido")
            print("\npresione enter para continuar...")    
            input()
        elif opcion == 2:
            path = input("Ingrese la dirección del archivo a analizarse: \n")
            if ( os.path.exists (path)):
                f = open(path)
                data = f.read()
                f.close()
                parser_yacc.call_Parse(data)
            else:
                print ("El archivo no existe")
            print("\npresione enter para continuar...")
            input()
        elif opcion == 3:
            print("gracias por usar este programa")
        else:
            print("ok")
    pass


if __name__ == '__main__':
    menu()  