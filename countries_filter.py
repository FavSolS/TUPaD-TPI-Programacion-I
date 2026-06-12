# Filtrar países por:
# o Continente
# o Rango de población
# o Rango de superficie

from countries_helpers import buscar_por_texto, validar_entero_no_negativo


def _formatear_numero(numero):
    return f"{numero:,}".replace(",", ".")


def _mostrar_error(mensaje):
    print(f"\nError: {mensaje}\n")


def mostrar_resultados(resultados, descripcion_filtro):
    print(f"\n{'=' * 60}")

    if len(resultados) == 0:
        print(f"\nNo se encontraron países para el criterio indicado.")
        return

    cantidad = len(resultados)
    etiqueta = "país encontrado" if cantidad == 1 else "países encontrados"
    print(f"\n{cantidad} {etiqueta}:\n")
    print(f"  {'Nombre':<24} {'Población':>14} {'Superficie':>14}  Continente")
    print(f"  {'-' * 24} {'-' * 14} {'-' * 14}  {'-' * 12}")

    for pais in resultados:
        print(
            f"  {pais['nombre']:<24} "
            f"{_formatear_numero(pais['poblacion']):>14} "
            f"{_formatear_numero(pais['superficie']):>14}  "
            f"{pais['continente']}"
        )
    print()


# Llamo funcion auxiliar para coincidencia parcial por continente
def filtrar_por_continente(paises, continente):
    return buscar_por_texto(paises, 'continente', continente)


def filtrar_por_poblacion(paises, poblacion_min, poblacion_max):
    resultados = []
    for pais in paises:
        if poblacion_min <= pais['poblacion'] <= poblacion_max:
            resultados.append(pais)
    return resultados


def filtrar_por_superficie(paises, superficie_min, superficie_max):
    resultados = []
    for pais in paises:
        if superficie_min <= pais['superficie'] <= superficie_max:
            resultados.append(pais)
    return resultados


# Funciones auxiliares para la entrada de datos del filtro

def _leer_criterio_filtro():
    while True:
        try:
            print("\n¿Por qué criterio desea filtrar?")
            print("1. Continente")
            print("2. Rango de población")
            print("3. Rango de superficie")
            print("0. Volver al menú principal")
            criterio_str = input("Seleccione una opción: ").strip()

            if criterio_str.lower() == "salir" or criterio_str == "0":
                return None

            criterio = int(criterio_str)
            if criterio in (1, 2, 3):
                return criterio

            _mostrar_error("Opción inválida. Ingrese 1, 2, 3 o 0 para volver.")
        except ValueError:
            _mostrar_error("Debe ingresar un número (1, 2, 3 o 0 para volver).")


def _leer_continente():
    print("\nIngrese el continente a filtrar (escriba 'salir' o 0 para volver al menú principal).")
    while True:
        continente = input("Continente: ")
        if continente.strip().lower() in ("salir", "0"):
            return None
        if continente.strip() == "":
            _mostrar_error(
                "El continente no puede estar vacío. Ingrese un nombre válido o escriba 'salir'."
            )
            continue
        return continente


def _leer_rango_numerico(nombre_rango, nombre_min, nombre_max):
    print(
        f"\nIngrese el rango de {nombre_rango} "
        f"(escriba 'salir' o 0 para volver al menú principal)."
    )
    while True:
        try:
            min_str = input(f"Ingrese la {nombre_min}: ")
            if min_str.strip().lower() in ("salir", "0"):
                return None

            # Llamo funcion auxiliar para validar el entero ingresado
            valor_min = validar_entero_no_negativo(min_str, nombre_min)

            max_str = input(f"Ingrese la {nombre_max}: ")
            if max_str.strip().lower() in ("salir", "0"):
                return None

            valor_max = validar_entero_no_negativo(max_str, nombre_max)

            if valor_min > valor_max:
                raise ValueError(
                    f"La {nombre_min} ({valor_min}) no puede ser mayor que la "
                    f"{nombre_max} ({valor_max}). Verifique el orden del rango."
                )

            return valor_min, valor_max

        except ValueError as e:
            _mostrar_error(f"{e} Intente nuevamente.")


def filtrar_paises(paises):
    criterio = _leer_criterio_filtro()
    if criterio is None:
        return

    if criterio == 1:
        continente = _leer_continente()
        if continente is None:
            return
        resultados = filtrar_por_continente(paises, continente)
        mostrar_resultados(resultados, f"continente «{continente.strip()}»")

    elif criterio == 2:
        rango = _leer_rango_numerico(
            "población", "población mínima", "población máxima"
        )
        if rango is None:
            return
        poblacion_min, poblacion_max = rango
        resultados = filtrar_por_poblacion(paises, poblacion_min, poblacion_max)
        mostrar_resultados(
            resultados,
            f"población entre {_formatear_numero(poblacion_min)} y "
            f"{_formatear_numero(poblacion_max)} habitantes",
        )

    elif criterio == 3:
        rango = _leer_rango_numerico(
            "superficie en km²", "superficie mínima", "superficie máxima"
        )
        if rango is None:
            return
        superficie_min, superficie_max = rango
        resultados = filtrar_por_superficie(paises, superficie_min, superficie_max)
        mostrar_resultados(
            resultados,
            f"superficie entre {_formatear_numero(superficie_min)} y "
            f"{_formatear_numero(superficie_max)} km²",
        )
