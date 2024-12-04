def verificar_metros_cuadrados(largo, ancho, consumos):
    total_metros_cuadrados = largo * ancho
    representacion_visual = [["|" for _ in range(ancho)] for _ in range(largo)]
    metros_consumidos = 0

    # Visualizar área original
    print(f"Total de Metros Cuadrados: {total_metros_cuadrados}")
    print(f"Representación Visual ({largo} x {ancho}):")
    for fila in representacion_visual:
        print("".join(fila))
    print()

    # Procesar cada consumo
    for consumo in consumos:
        clargo, cancho = consumo
        metros_consumidos += clargo * cancho
        for i in range(clargo):
            for j in range(cancho):
                if i < largo and j < ancho:
                    representacion_visual[i][j] = " "

    metros_restantes = total_metros_cuadrados - metros_consumidos

    # Visualizar área después de los consumos
    print("Después de aplicar consumos:")
    for fila in representacion_visual:
        print("".join(fila))
    print()

    # Mostrar metros cuadrados consumidos y restantes
    print(f"Metros Cuadrados Consumidos: {metros_consumidos}")
    print(f"Metros Cuadrados Restantes: {metros_restantes}")

def main():
    try:
        largo = int(input("Ingrese el largo en metros: "))
        ancho = int(input("Ingrese el ancho en metros: "))
        
        if largo <= 0 or ancho <= 0:
            print("Los valores deben ser mayores que 0.")
            return

        consumos = []
        while True:
            clargo = input("Ingrese el largo del consumo (o presione Enter para terminar): ")
            if clargo == "":
                break
            cancho = input("Ingrese el ancho del consumo: ")
            
            try:
                clargo = int(clargo)
                cancho = int(cancho)
                if clargo > 0 and cancho > 0:
                    consumos.append((clargo, cancho))
                else:
                    print("Los valores de consumo deben ser mayores que 0.")
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")

        verificar_metros_cuadrados(largo, ancho, consumos)

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
