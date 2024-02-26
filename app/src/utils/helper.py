from datetime import datetime


"""Funciones de ayuda para la manipulación de datos."""

def rows_to_dicts(rows, columns):
    """
    Convierte una lista de tuplas en una lista de diccionarios.
    Cada diccionario representa una fila, con las claves siendo los nombres de las columnas.
    """
    # Convertir los objetos datetime a cadenas de texto
    converted_rows = []
    for row in rows:
        converted_row = []
        for value in row:
            if isinstance(value, datetime):
                converted_row.append(value.isoformat())
            else:
                converted_row.append(value)
        converted_rows.append(converted_row)

    # Convertir las tuplas en una lista de diccionarios
    return [dict(zip(columns, row)) for row in converted_rows]