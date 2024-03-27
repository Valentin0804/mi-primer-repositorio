from typing import Any, List, Tuple

nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]

def combinar_basico(nombres: List[str], precios: List[float]) -> Tuple[Any]:

    if len(nombres) != len(precios):
        raise ValueError("Las listas deben tener la misma longitud")
    combinacion = []
    for i in range(len(nombres)):
        combinacion.append((nombres[i], precios[i]))

    return tuple(combinacion)

respuesta = (
    ("ventana", 100.48),
    ("lámpara", 16.42),
    ("shampoo", 5.2),
)

assert combinar_basico(nombre_articulos, precio_articulos) == respuesta


###############################################################################

id_articulos = [6852, 1459, 3578]


def combinar_enumerate(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:

    if len(nombres) != len(precios) != len(ids):
        raise ValueError("Las listas deben tener la misma longitud")
    combinacion2 = []
    for i in range(len(nombres)):
        combinacion2.append((nombres[i], precios[i], ids[i]))

    return tuple(combinacion2)


respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)
assert combinar_enumerate(nombre_articulos, precio_articulos, id_articulos) == respuesta

###############################################################################

id_articulos = [6852, 1459, 3578]
categoria_articulos = ["hogar", "libreria", "perfumeria"]
importado_articulos = [True, False, True]


def combinar_zip_args(*args) -> Tuple[Any]:

    if len(set(len(arg) for arg in args)) != 1:
        raise ValueError("Todas las listas deben tener la misma longitud")
    return tuple(zip(*args))

respuesta = (
    ("ventana", 100.48, 6852, "hogar", True),
    ("lámpara", 16.42, 1459, "libreria", False),
    ("shampoo", 5.2, 3578, "perfumeria", True),
)

componentes = [
    nombre_articulos,
    precio_articulos,
    id_articulos,
    categoria_articulos,
    importado_articulos,
]

assert combinar_zip_args(*componentes) == respuesta
