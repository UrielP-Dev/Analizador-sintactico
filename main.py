import parser_yacc

def menu():
    file_path = "codigo_fuente.txt"
    while True:
        try:
            with open(file_path, 'r') as file:
                data = file.read()
                parser_yacc.call_Parse(data)
        except FileNotFoundError:
            print("No se pudo encontrar el archivo 'codigo_fuente.txt'")
        
        input("\nPresione Enter para analizar nuevamente o 'q' para salir: ")
        decision = input().strip().lower()
        if decision == 'q':
            print("Gracias por usar este programa")
            break

if __name__ == '__main__':
    menu()
