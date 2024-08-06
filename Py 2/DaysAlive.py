from datetime import datetime

def dias_vivo(fecha_nacimiento):
    hoy = datetime.now()
    # Convierte la cadena de fecha de nacimiento en un objeto datetime
    nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
    # Calcula la diferencia en días entre hoy y la fecha de nacimiento
    dias_vivo = (hoy - nacimiento).days
    return dias_vivo

# Solicita al usuario su fecha de nacimiento
tu_fecha = input("Introduce tu fecha de nacimiento (DIA-MES-AÑO): ")
# Calcula los días que ha vivido el usuario
dias = dias_vivo(tu_fecha)
# Imprime el resultado
print(f"Naciste el {tu_fecha} así que llevas {dias} días vivo")
