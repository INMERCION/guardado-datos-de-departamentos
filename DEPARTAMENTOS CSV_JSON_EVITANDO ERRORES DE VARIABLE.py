import json
import csv
departamentos = []

def menu():
    while True:
        print("\nInmobiliaria DUOC")
        print("1. Agregar Departamento")
        print("2. Listar Departamentos")
        print("3. Buscar Departamento")
        print("4. Modificar Departamento")
        print("5. Eliminar Departamento")
        print("6. Guardar Datos en JSON")
        print("7. Guardar Datos en CSV")
        print("8. Cargar Datos desde JSON")
        print("9. Cargar Datos desde CSV")
        print("10. Salir")
        opc = input(": ")
        if opc == "1":
            agregar()
        elif opc == "2":
            listar()
        elif opc == "3":
            buscar()
        elif opc == "4":
            modificar()
        elif opc == "5":
            eliminar()
        elif opc == "6":
            guardar_datos_json()
        elif opc == "7":
            guardar_datos_csv()
        elif opc == "8":
            cargar_datos_json()
        elif opc == "9":
            cargar_datos_csv()
        elif opc == "10":
            salir()
            break
        else:
            print("Escoja una opción correcta")

def agregar():
    id = input("\nAgregue ID: ") 
    dirección = input("Agregue Dirección: ") 
    while True:
        try:
            precio = int(input("Precio UF: ")) 
            superficie = float(input("Superficie en m²: ")) 
            habitaciones = int(input("Número de habitaciones: "))
            break
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos para \nprecio, superficie y habitaciones.")

    departamento = {
        "id": id,
        "dirección": dirección,
        "precio": precio,
        "superficie": superficie,
        "habitaciones": habitaciones
    }
    departamentos.append(departamento)

def listar():

    lista_ordenada = sorted(departamentos, key=lambda x: x["id"])

    for idx, departamento in enumerate(lista_ordenada, start=1):
        print(f"\nDEPARTAMENTO: {idx}")
        print(f"ID              : {departamento['id']}")
        print(f"Dirección       : {departamento['dirección']}")
        print(f"Precio          : {departamento['precio']} UF")
        print(f"Superficie      : {departamento['superficie']} m²")
        print(f"N° Habitaciones : {departamento['habitaciones']}")

    if not departamentos:
        print("\nNo hay departamentos que mostrar")

def buscar():
    buscar = input("\nIngrese el ID del Departamento: ")
    departamento_encontrado = False
    for departamento in departamentos:
        if departamento["id"].lower() == buscar.lower():
            print(f"ID              : {departamento['id']}")
            print(f"Dirección       : {departamento['dirección']}")
            print(f"Precio          : {departamento['precio']} UF")
            print(f"Superficie      : {departamento['superficie']} m²")
            print(f"N° Habitaciones : {departamento['habitaciones']}")
            departamento_encontrado = True
            break
    
    if not departamento_encontrado:
        print(f"\nDepartamento con ID {buscar} no encontrado.")

def modificar():
    modificar = input("\nINGRESE ID: ")
    encontrado = False
    for departamento in departamentos:
        if departamento["id"] == modificar:
            departamento["id"] = input("Ingrese nuevo ID: ")
            departamento["dirección"] = input("Ingrese nueva Dirección: ")
            departamento["precio"] = float(input("Ingrese nuevo precio en UF: "))
            departamento["superficie"] = int(input("Ingrese nueva superficie en m²: "))
            departamento["habitaciones"] = int(input("N° de Habitaciones: "))
            print("\nDepartamento modificado con ÉXITO!!!")
            encontrado = True
            break
    if not encontrado:
        print("\nDepartamento no encontrado...")

def eliminar():
    eliminar = input("\nINGRESE ID: ")
    encontrado = False
    for departamento in departamentos:
        if departamento["id"] == eliminar:
            departamentos.remove(departamento)
            print("\nDepartamento Eliminado con Exito!!!")
            encontrado = True
            break
    if not encontrado:
        print("\nDepartamento no encontrado...")

def guardar_datos_json():
    with open("Departamentos.json", 'w') as file:
        json.dump(departamentos, file, indent=4)
    print("\nDatos guardados en Departamentos.json.")

def guardar_datos_csv():
    with open("Departamentos.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "dirección", "precio", "superficie", "habitaciones"])
        for departamento in departamentos:
            writer.writerow([departamento["id"], departamento["dirección"], departamento["precio"], departamento["superficie"], departamento["habitaciones"]])
    print("\nDatos guardados en Departamentos.csv.")

def cargar_datos_json():
    try:
        with open("Departamentos.json", 'r') as file:
            global departamentos
            departamentos = json.load(file)
        print("\nDatos cargados desde Departamentos.json")
    except FileNotFoundError:
        print("\nEl archivo Departamentos.json no existe.")
    except ValueError:
        print("\nEl archivo Departamentos.json esta Vacio.")

def cargar_datos_csv():
    try:
        with open("Departamentos.csv", 'r') as file:
            reader = csv.DictReader(file)
            global departamentos
            departamentos = [row for row in reader]
        print("\nDatos cargados desde Departamentos.csv")
    except FileNotFoundError:
        print("\nEl archivo Departamentos.csv no existe.")

def salir():
    print("\nSaliendo del programa...")

if __name__ == "__main__":
    menu()
