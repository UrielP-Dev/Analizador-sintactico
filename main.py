import parser_yacc

def menu():
    opcion = 0
    while (opcion != 2):
        print('''MENU ANALIZADOR SINTÁCTICO
         \t1: Analizar código desde archivo
         \t2: Salir''')
        opcion = int(input("Opción: "))
        if opcion == 1:
            file_path = "codigo_fuente.txt"
            try:
                with open(file_path, 'r') as file:
                    data = file.read()
                    parser_yacc.call_Parse(data)
            except FileNotFoundError:
                print("No se pudo encontrar el archivo 'codigo_fuente.txt'")
            print("\nPresione Enter para continuar...")
            input()
        elif opcion == 2:
            print("Gracias por usar este programa")
        else:
            print("Opción no válida. Intente de nuevo.")
    pass

if __name__ == '__main__':
    menu()
