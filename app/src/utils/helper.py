from datetime import datetime, date


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
            # Si es un objeto datetime, convertirlo a cadena, o también si es un objeto date
            if isinstance(value, datetime) or isinstance(value, date):
                # print(f'Value: {value}, type: {type(value)}, isoformat: {value.isoformat()}')
                converted_row.append(value.isoformat())
            else:
                converted_row.append(value)
        converted_rows.append(converted_row)

    # Convertir las tuplas en una lista de diccionarios
    return [dict(zip(columns, row)) for row in converted_rows]

def clean_dict(data):
    """Covierte los objetos datetime y date a cadenas de texto."""
    for key, value in data.items():
        if isinstance(value, datetime) or isinstance(value, date):
            data[key] = value.isoformat()
    return data