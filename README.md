# TUPaD — TPI Programación I

## Gestión de Datos de Países

Aplicación de consola en Python para administrar un listado de países. Los datos se cargan desde un archivo CSV, se manipulan en memoria durante la ejecución y los cambios de alta o modificación se persisten en el mismo archivo.

## Requisitos

- Python 3.x
- No requiere librerías externas

## Cómo ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

Al iniciar, seleccionar la opción **1** para cargar los datos desde `countries.csv`. El resto de las operaciones requiere que la lista esté cargada.

## Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `main.py` | Punto de entrada y menú principal |
| `countries.csv` | Base de datos de países (nombre, población, superficie, continente) |
| `countries_csv.py` | Lectura, alta y actualización del CSV |
| `countries_helpers.py` | Funciones auxiliares compartidas (validaciones, búsqueda, normalización) |
| `countries_management.py` | Alta y modificación de países |
| `countries_search.py` | Búsqueda por nombre |
| `countries_sort.py` | Ordenamiento de países |
| `countries_filter.py` | Filtrado por continente, población o superficie |
| `countries_stats.py` | Estadísticas sobre los datos cargados |

Cada país se representa como un diccionario con las claves: `nombre`, `poblacion`, `superficie` y `continente`.

## Menú principal

| Opción | Descripción |
|---|---|
| 1 | Cargar países desde `countries.csv` |
| 2 | Mostrar países *(pendiente de implementación)* |
| 3 | Buscar país por nombre |
| 4 | Agregar un nuevo país |
| 5 | Actualizar población y superficie de un país |
| 6 | Ordenar países |
| 7 | Filtrar países |
| 8 | Obtener estadísticas |
| 9 | Salir |

## Funcionalidades

### Carga de datos

- Lee el archivo `countries.csv` con codificación UTF-8.
- La carga solo puede realizarse una vez por ejecución.

### Búsqueda

- Buscar un país por nombre a través del módulo `countries_search.py`.
- Utiliza `buscar_por_texto` con **coincidencia parcial**: si el texto ingresado aparece dentro del nombre del país, se incluye en los resultados (por ejemplo, `"arg"` devuelve *Argelia* y *Argentina*).
- Si se ingresa el nombre completo, también funciona como coincidencia exacta.
- Antes de comparar, el texto se normaliza: se ignoran mayúsculas/minúsculas, espacios al inicio y al final, y acentos (por ejemplo, `"mexico"` encuentra *México*).
- Muestra todos los países que coincidan o un mensaje si no hay resultados.

### Alta y modificación

- Agregar un país con todos los campos obligatorios (no se permiten campos vacíos).
- Validación de nombres duplicados al dar de alta.
- Actualizar población y superficie de un país existente.
- Los cambios se guardan en `countries.csv`.

### Filtrado

Submenú con las siguientes opciones:

- Por continente (coincidencia parcial).
- Por rango de población (mínimo y máximo).
- Por rango de superficie (mínimo y máximo).

### Ordenamiento

- Por nombre, población o superficie.
- Orden ascendente o descendente.

### Estadísticas

Submenú con las siguientes opciones:

- **Estadísticas de población:** promedio, país(es) con mayor y menor población, top 5 con mayor y menor población, y top 5 más cercanos al promedio.
- **Estadísticas de superficie:** promedio, país(es) con mayor y menor superficie, top 5 con mayor y menor superficie, y top 5 más cercanos al promedio.
- **Cantidad de países por continente:** distribución ordenada de mayor a menor.

## Convención de commits

Formato basado en [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/):

```
<tipo>[alcance opcional]: <descripción>
```

### Tipos habituales

| Tipo | Uso |
|---|---|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de errores |
| `refactor` | Refactorización sin cambio de comportamiento |
| `docs` | Cambios en documentación |
| `chore` | Tareas de mantenimiento |

### Alcance

Usar el nombre del módulo o la funcionalidad afectada:

- Por archivo: `fix(countries-csv): corregir encoding del archivo`
- Por feature: `feat(countries-stats): agregar top 5 por población`

### Ejemplos

```
feat(countries-filter): agregar filtro por rango de superficie
fix(countries-csv): corregir lectura con caracteres especiales
feat(countries-stats): implementar estadísticas de población
docs(readme): actualizar menú y estructura del proyecto
refactor(countries-helpers): extraer validación de enteros
```

### Nombres de ramas

Seguir el mismo criterio, separando tipo y descripción con `/`:

```
feat/countries-stats
fix/csv-encoding
docs/update
```
