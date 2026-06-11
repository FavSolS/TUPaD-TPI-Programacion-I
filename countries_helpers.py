# Funciones auxiliares que son reutilizadas en los otros metodos

def validar_lista_cargada(paises):
    if len(paises) == 0:
        print("Error: No hay datos cargados. Seleccione la opción 1 primero.")
        return False
    return True


def nombre_existe(paises, nombre):
    # Strip elimina espacios, lower convierte a minusculas. Nos sirve para comparar nombres siempre en las mismas condiciones sin importar como haya sido escrito
    nombre_normalizado = nombre.strip().lower()
    for item in paises:
        if item['nombre'].strip().lower() == nombre_normalizado:
            return True
    return False