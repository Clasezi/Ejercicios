from Pila import Pila


print("\n{:3}{:<5}  ".format("  ", "-"*50))
print("{:15}{:<0}  ".format("  ", "TORRES DE HANOI"))
print("{:3}{:<5}  ".format("  ", "-"*50))
print("\n{:3}{:<5}  ".format("  ", "La cantidad de discos debe ser entre 3 y 7 " ))


while True:
    cantidad = int(input("\n{:3}{:<0}  ".format("  ", "Ingrese el numero de discos: ")))
    if cantidad>=3 and cantidad<8:
        break
    else:
        print("\n{:3}{:<5}  ".format("  ", "ingrese un numero entre desde 3 hasta 7"))

TorreInicial = Pila()
TorreMedio = Pila()
TorreFinal = Pila()


def Llenar_torreInicial():
    for i in range(cantidad):
        disco = int(input("\n{:3}{:<0}  ".format("  ","Numero del disco {}:".format(i + 1))))

        TorreInicial.items.append(disco)


def Llenar_torreFinalconInicial():
    disco_retirar = TorreInicial.pop()
    TorreFinal.items.append(disco_retirar)


def Llenar_torreFinal_Medio():
    disco_retirar = TorreMedio.pop()
    TorreFinal.items.append(disco_retirar)


def Llenar_TorreMedioconInicial():
    disco_retirar = TorreInicial.pop()
    TorreMedio.items.append(disco_retirar)


def Llenar_TorreMedioconFinal():
    disco_retirar = TorreFinal.pop()
    TorreMedio.items.append(disco_retirar)


def Llenar_TorreInicialconFinal():
    disco_retirar = TorreFinal.pop()
    TorreInicial.items.append(disco_retirar)


def Llenar_TorreInicialconMedio():
    disco_retirar = TorreMedio.pop()
    TorreInicial.items.append(disco_retirar)


if cantidad == 3:
    Llenar_torreInicial()
    print("")
    print("\n{:3}{:<25} {:<25}{:<25} ".format("  ", "TORRE INICIAL", "TORRE DEL MEDIO", "TORRE FINAL"))
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconMedio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinal_Medio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

elif cantidad == 4 :
    Llenar_torreInicial()
    print("")
    print("\n{:3}{:<25} {:<25}{:<25} ".format("  ", "TORRE INICIAL", "TORRE DEL MEDIO", "TORRE FINAL"))
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))
    
    Llenar_TorreMedioconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinal_Medio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinal_Medio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconMedio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinal_Medio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinal_Medio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

elif cantidad == 5 :
    Llenar_torreInicial()
    print("")
    print("\n{:3}{:<25} {:<25}{:<25} ".format("  ", "TORRE INICIAL", "TORRE DEL MEDIO", "TORRE FINAL"))
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconMedio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinal_Medio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconMedio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconMedio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinal_Medio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconMedio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconMedio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinal_Medio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreMedioconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))
    
    Llenar_TorreMedioconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_TorreInicialconMedio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinal_Medio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))