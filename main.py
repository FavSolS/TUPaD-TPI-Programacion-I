# Importo funciones que necesito en este file
from countries_csv import leer_csv
from countries_helpers import validar_lista_cargada 
from countries_management import alta_nuevo_pais, modificar_pais
from countries_search import buscar_pais
from countries_sort import ordenar_paises


# Menu

##Función básica para mostrarle el menu al usuario.
def mostrar_menu():
    print("\n===== Gestión de Datos de Países =====")
    print("1. Primera carga de paises desde la base de datos (csv)") #done
    print("2. Mostrar paises") ##usar paginado --- este podria ser un nice to have porque no lo pide la consigna
    print("3. Buscar país por nombre") #done
    print("4. Agregar un nuevo país") #done
    print("5. Actualizar datos de un país") #done
    print("6. Ordenar países") 
    print("7. Filtrar países")
    print("8. Obtener estadísticas")
    print("9. Salir")
    print("==============================================")

    
# Inicialización del listado de paises que nos traeremos del csv
paises = []
# Inicialización de opcion del menu
opcion = 0

while opcion != 9:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                if len(paises) > 0:
                    print("\nLa lista de paises ya fue cargada, por favor selecciona otra opción.")
                else:
                    paises = leer_csv()
                # print para debug/check
                # print(paises)
            elif opcion == 2:
               if validar_lista_cargada(paises):
                pass
            elif opcion == 3:
                if validar_lista_cargada(paises):
                    buscar_pais(paises)
            elif opcion == 4:
                if validar_lista_cargada(paises):
                    alta_nuevo_pais(paises)
            elif opcion == 5:
                if validar_lista_cargada(paises):
                    modificar_pais(paises)
            elif opcion == 6:
                if validar_lista_cargada(paises):
                    ordenar_paises(paises)
            elif opcion == 7:
                if validar_lista_cargada(paises):
                    pass
            elif opcion == 8:
                if validar_lista_cargada(paises):
                    pass
            elif opcion == 9:
                print("Saliendo del sistema. ¡Adiós!")
                break
            else:
                print("Error: Opción inválida. Ingrese un número entre 1 y 8.")
        except ValueError as e:
            print(f"Error: {e}")
