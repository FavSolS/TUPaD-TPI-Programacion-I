# Mostrar estadísticas:
# o Población (top 5, extremos, cercanos a la media y promedio)
# o Superficie (top 5, extremos, cercanos a la media y promedio)
# o Cantidad de países por continente

from countries_helpers import obtener_poblacion, obtener_superficie

CANTIDAD_TOP = 5


def _formatear_numero(numero):
    return f"{numero:,}".replace(",", ".")


def _mostrar_error(mensaje):
    print(f"\nError: {mensaje}\n")


# Funciones auxiliares para la entrada de datos de estadísticas

def _leer_opcion_estadistica():
    while True:
        try:
            print("\n¿Qué estadística desea consultar?")
            print("1. Estadísticas de población")
            print("2. Estadísticas de superficie")
            print("3. Cantidad de países por continente")
            print("0. Volver al menú principal")
            print("(También puede escribir 'salir' o 0 para volver al menú principal)")
            opcion_str = input("Seleccione una opción: ").strip()

            if opcion_str.lower() == "salir" or opcion_str == "0":
                return None

            opcion = int(opcion_str)
            if opcion in (1, 2, 3):
                return opcion

            _mostrar_error("Opción inválida. Ingrese 1, 2, 3 o 0 para volver.")
        except ValueError:
            _mostrar_error("Debe ingresar un número (1, 2, 3 o 0 para volver).")


# Funciones auxiliares para el cálculo de estadísticas

def _calcular_promedio(paises, obtener_valor):
    return sum(obtener_valor(pais) for pais in paises) / len(paises)


def _obtener_top_paises(paises, obtener_valor, cantidad=CANTIDAD_TOP, descendente=True):
    ordenados = sorted(paises, key=obtener_valor, reverse=descendente)
    return ordenados[:min(cantidad, len(paises))]


def _obtener_paises_cercanos_a_media(paises, obtener_valor, cantidad=CANTIDAD_TOP):
    promedio = _calcular_promedio(paises, obtener_valor)
    ordenados = sorted(
        paises,
        key=lambda pais: abs(obtener_valor(pais) - promedio),
    )
    return ordenados[:min(cantidad, len(paises))], promedio


def _paises_con_valor(paises, obtener_valor, valor):
    return [pais for pais in paises if obtener_valor(pais) == valor]


def _mostrar_tabla_paises(paises, titulo, obtener_valor, nombre_columna, unidad):
    cantidad = len(paises)
    etiqueta = "país" if cantidad == 1 else "países"
    print(f"\n{titulo} ({cantidad} {etiqueta}):\n")
    print(f"  {'Nombre':<24} {nombre_columna:>14}")
    print(f"  {'-' * 24} {'-' * 14}")

    for pais in paises:
        print(
            f"  {pais['nombre']:<24} "
            f"{_formatear_numero(obtener_valor(pais)):>14} {unidad}"
        )


def _mostrar_extremos(paises, obtener_valor, nombre_campo, unidad):
    valor_max = max(obtener_valor(pais) for pais in paises)
    valor_min = min(obtener_valor(pais) for pais in paises)

    paises_mayor = _paises_con_valor(paises, obtener_valor, valor_max)
    paises_menor = _paises_con_valor(paises, obtener_valor, valor_min)

    _mostrar_tabla_paises(
        paises_mayor,
        f"País(es) con mayor {nombre_campo}",
        obtener_valor,
        nombre_campo.capitalize(),
        unidad,
    )
    print()
    _mostrar_tabla_paises(
        paises_menor,
        f"País(es) con menor {nombre_campo}",
        obtener_valor,
        nombre_campo.capitalize(),
        unidad,
    )


# Estadísticas completas de un campo numérico (población o superficie).

def _mostrar_estadisticas_campo(paises, obtener_valor, nombre_campo, unidad):
    cantidad = len(paises)
    etiqueta = "país cargado" if cantidad == 1 else "países cargados"
    promedio = _calcular_promedio(paises, obtener_valor)

    top_mayor = _obtener_top_paises(paises, obtener_valor, descendente=True)
    top_menor = _obtener_top_paises(paises, obtener_valor, descendente=False)
    cercanos_a_media, _ = _obtener_paises_cercanos_a_media(paises, obtener_valor)

    print(f"\n{'=' * 60}")
    print(
        f"\nPromedio de {nombre_campo} (sobre {cantidad} {etiqueta}):\n"
        f"  {_formatear_numero(round(promedio))} {unidad}\n"
    )

    _mostrar_extremos(paises, obtener_valor, nombre_campo, unidad)

    print()
    _mostrar_tabla_paises(
        top_mayor,
        f"Top {len(top_mayor)} países con mayor {nombre_campo}",
        obtener_valor,
        nombre_campo.capitalize(),
        unidad,
    )

    print()
    _mostrar_tabla_paises(
        top_menor,
        f"Top {len(top_menor)} países con menor {nombre_campo}",
        obtener_valor,
        nombre_campo.capitalize(),
        unidad,
    )

    print()
    _mostrar_tabla_paises(
        cercanos_a_media,
        f"Top {len(cercanos_a_media)} países con {nombre_campo} más cercana al promedio",
        obtener_valor,
        nombre_campo.capitalize(),
        unidad,
    )
    print()


# Estadísticas de población de todos los países cargados.

def mostrar_estadisticas_poblacion(paises):
    _mostrar_estadisticas_campo(
        paises, obtener_poblacion, "población", "habitantes"
    )


# Estadísticas de superficie de todos los países cargados.

def mostrar_estadisticas_superficie(paises):
    _mostrar_estadisticas_campo(
        paises, obtener_superficie, "superficie", "km²"
    )


# Cantidad de países agrupados por continente.

def mostrar_cantidad_por_continente(paises):
    cantidad_por_continente = {}
    for pais in paises:
        continente = pais["continente"]
        cantidad_por_continente[continente] = (
            cantidad_por_continente.get(continente, 0) + 1
        )

    total = len(paises)
    etiqueta_total = "país" if total == 1 else "países"

    print(f"\n{'=' * 60}")
    print(f"\nDistribución por continente ({total} {etiqueta_total} en total):\n")
    print(f"  {'Continente':<20} {'Cantidad':>10}")
    print(f"  {'-' * 20} {'-' * 10}")

    # Armar lista con cada continente y su cantidad de países
    lista_continentes = []
    for continente in cantidad_por_continente:
        cantidad = cantidad_por_continente[continente]
        lista_continentes.append((continente, cantidad))

    # Ordenar de mayor a menor cantidad (intercambiamos posiciones si hace falta)
    for i in range(len(lista_continentes)):
        for j in range(i + 1, len(lista_continentes)):
            cantidad_actual = lista_continentes[i][1]
            cantidad_siguiente = lista_continentes[j][1]
            if cantidad_siguiente > cantidad_actual:
                temporal = lista_continentes[i]
                lista_continentes[i] = lista_continentes[j]
                lista_continentes[j] = temporal

    for continente, cantidad in lista_continentes:
        etiqueta = "país" if cantidad == 1 else "países"
        print(f"  {continente:<20} {cantidad:>5} {etiqueta}")
    print()


# Punto de entrada: muestra el submenú y ejecuta la estadística elegida.

def obtener_estadisticas(paises):
    opcion = _leer_opcion_estadistica()
    if opcion is None:
        return

    if opcion == 1:
        mostrar_estadisticas_poblacion(paises)
    elif opcion == 2:
        mostrar_estadisticas_superficie(paises)
    elif opcion == 3:
        mostrar_cantidad_por_continente(paises)
