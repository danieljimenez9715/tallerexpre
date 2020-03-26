import re
def validarExp(expresion):
    patron = re.compile('[A-Z][0-9][0-9][0-9][a-z][a-z[a-z]*[\W]{3}$')

    if patron.search(expresion):
        resultado = patron.search(expresion).group(0)
        if (resultado == expresion):
            print("La expresion ingresada pertenece a la expresión regular...")
    else:
        print("La expresion ingresada no pertenece a la expresión regular...")

sw = 0
while(sw==0):
    opc = 1
    if(opc == 1):
        expresion = input("INGRESE LA EXPRESION REGULAR: ")
        validarExp(expresion)
        opc = int(input("\nINGRESE 1 PARA SEGUIR VALIDANDO O INGRESE OTRO NUMERO PARA SALIR "))
        print("\n"*50)

    if(opc < 1 or opc > 1):
        print("FIN DEL PROCESO")
        sw = 1
