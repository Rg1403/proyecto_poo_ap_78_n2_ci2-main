from prettytable import PrettyTable
from datos.consultas import consulta_select,consulta_insert
from datos.conexion import leer_datos,insertar_datos
from modelos.avion import Avion
from interfaces.interface_aviones import solicitar_data_avion,solicitar_data_eliminar_avion


def obtener_datos_aviones():
    lista_aviones = []
    tabla_aviones = PrettyTable()
    tabla_aviones.field_names = ['N°', 'Código', 'Tipo', 'Capacidad']

    campos = 'id_avion,cod_avion,tipo_avion,capacidad_avion'
    tabla = 'aviones'
    consulta = consulta_select(campos, tabla)

    if consulta:
        resultado = leer_datos(consulta)
        if resultado:
            for data in resultado:
                avion = Avion(
                    data[0], data[1], data[2], data[3])  # type: ignore
                lista_aviones.append(avion)

        if len(lista_aviones) > 0:
            for objeto in lista_aviones:
                tipo = ''
                capacidad = ''
                if objeto._tipo_avion == 1:
                    tipo = 'Carga'
                    capacidad = f'{objeto._capacidad_avion} Ton'
                else:
                    tipo = 'Pasajeros'
                    capacidad = f'{objeto._capacidad_avion} Pasajeros'
                tabla_aviones.add_row(
                    [objeto._id_avion, objeto._cod_avion, tipo, capacidad])
        print(tabla_aviones)


def crear_avion():
    campos = 'cod_avion,tipo_avion,capacidad_avion'
    tabla = 'aviones'
    aerolinea_avion, codigo_avion, tipo_avion, capacidad_avion = solicitar_data_avion('crear')  # type: ignore        
    datos = (aerolinea_avion, codigo_avion,tipo_avion,capacidad_avion)
    consulta = consulta_insert(campos, tabla)
    insertar_datos(consulta, datos, 'crear')


# def modificar_aerolinea():
#     obtener_datos_aerolineas()

#     nombre = input('Ingrese Nombre Aerolínea a Editar: ')
#     if nombre != '':
#         campos = 'id_aerolinea,nombre_aerolinea,web_aerolinea'
#         tabla = 'aerolineas'
#         consulta = consulta_nombre_aerolinea(campos, tabla)
#         if consulta:
#             aerolinea = leer_dato_individual(consulta, nombre)
#             if aerolinea:
#                 nuevo_nombre, nueva_web = solicitar_data_aerolinea()  # type: ignore

#                 if nuevo_nombre == '':
#                     nuevo_nombre = str(aerolinea[1])  # type: ignore
#                 if nueva_web == '':
#                     nueva_web = aerolinea[2]  # type: ignore

#                 datos = (nuevo_nombre.title(), nueva_web,
#                          aerolinea[0])  # type: ignore
#                 consulta_update = aerolinea_update()
#                 insertar_datos(consulta_update, datos)
#                 # type: ignore
#                 print(
#                     f'¡Aerolínea "{str(aerolinea[1])}" modificada existosamente!')


# def eliminar_aerolinea():
#     obtener_datos_aerolineas()

#     nombre = input('Ingrese Nombre Aerolínea a Eliminar: ')
#     if nombre != '':
#         campos = 'id_aerolinea,nombre_aerolinea,web_aerolinea'
#         tabla = 'aerolineas'
#         consulta = consulta_nombre_aerolinea(campos, tabla)
#         if consulta:
#             aerolinea = leer_dato_individual(consulta, nombre)
#             if aerolinea:
#                 datos = (aerolinea[0],)  # type: ignore
#                 consulta_delete = aerolinea_delete()
#                 insertar_datos(consulta_delete, datos)
#                 # type: ignore
#                 print(
#                     f'¡Aerolínea "{str(aerolinea[1])}" eliminada existosamente!')
