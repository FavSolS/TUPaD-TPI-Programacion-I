import unicodedata

# Funciones auxiliares que son reutilizadas en los otros metodos
def validar_lista_cargada(paises):
    if len(paises) == 0:
        print("Error: No hay datos cargados. Seleccione la opción 1 primero.")
        return False
    return True


def validar_entero_no_negativo(valor_str, nombre_campo):
    valor_limpio = valor_str.strip()

    if valor_limpio == "":
        raise ValueError(
            f"La {nombre_campo} no puede estar vacía. Debe ingresar un número entero."
        )

    if "." in valor_limpio or "," in valor_limpio:
        raise ValueError(
            f"La {nombre_campo} debe ser un número entero, no un decimal."
        )

    if not valor_limpio.isdigit():
        raise ValueError(
            f"La {nombre_campo} debe ser un número entero (sin letras ni símbolos)."
        )

    valor = int(valor_limpio)
    if valor < 0:
        raise ValueError(
            f"La {nombre_campo} no puede ser negativa. Ingrese un número igual o mayor a 0."
        )
    return valor


def leer_entero_no_negativo(mensaje, nombre_campo):
    valor_str = input(mensaje)
    return validar_entero_no_negativo(valor_str, nombre_campo)


def normalizar_texto(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def buscar_por_texto(paises, campo, texto, coincidencia_exacta=False):
    texto_normalizado = normalizar_texto(texto)
    resultados = []
    for pais in paises:
        valor_normalizado = normalizar_texto(pais[campo])
        if coincidencia_exacta:
            coincide = valor_normalizado == texto_normalizado
        else:
            coincide = texto_normalizado in valor_normalizado
        if coincide:
            resultados.append(pais)
    return resultados


def nombre_existe(paises, nombre):
    return len(buscar_por_texto(paises, 'nombre', nombre, coincidencia_exacta=True)) > 0

# Funciones auxiliares para el sort
def obtener_nombre(pais):
    return normalizar_texto(pais['nombre'])

def obtener_poblacion(pais):
    return pais['poblacion']

def obtener_superficie(pais):
    return pais['superficie']