from negocio.negocio_aerolineas import obtener_datos_aerolineas


def solicitar_data_avion(proceso=''):
    aerolinea_avion = 0
    tipo_avion = 0
    capacidad_avion = 0

    while True:
        mensaje_aerolinea_avion = 'Ingrese Id Aerolínea (o ENTER para conservar): '
        mensaje_codigo_avion = 'Ingrese Código Avión (o ENTER para conservar): '
        mensaje_tipo_avion = 'Ingrese Tipo Avión (1=Carga | 2=Pasajeros) (o ENTER para conservar): '
        mensaje_capacidad_avion = 'Ingrese Capacidad Avión (o ENTER para conservar): '

        if proceso != None:
            mensaje_aerolinea_avion = 'Ingrese Id Aerolínea: '
            mensaje_codigo_avion = 'Ingrese Código Avión: '
            mensaje_tipo_avion = 'Ingrese Tipo Avión (1=Carga | 2=Pasajeros): '
            mensaje_capacidad_avion = 'Ingrese Capacidad Avión: '

        obtener_datos_aerolineas()
        while True:
            aerolinea_avion_str = input(mensaje_aerolinea_avion)
            try:
                aerolinea_avion = int(aerolinea_avion_str)
                break
            except:
                print('Ingrese un número entero válido para el Id.')
        codigo_avion = input(mensaje_codigo_avion)
        while True:
            tipo_avion_str = input(mensaje_tipo_avion)
            try:
                tipo_avion = int(tipo_avion_str)
                break
            except:
                print('Ingrese un número entero válido para el Id.')
        while True:
            capacidad_avion_str = input(mensaje_capacidad_avion)
            try:
                capacidad_avion = int(capacidad_avion_str)
                break
            except:
                print('Ingrese un número entero válido para el Id.')

        if aerolinea_avion > 0 and codigo_avion != '' and tipo_avion > 0 and capacidad_avion > 0:
            return aerolinea_avion, codigo_avion, tipo_avion, capacidad_avion


def solicitar_data_eliminar_avion():
    while True:
        nombre = input('Ingrese Nombre Aerolínea a Eliminar: ')
        if nombre != '':
            return nombre
