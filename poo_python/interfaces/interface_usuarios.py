import getpass

def solicitar_data_usuario(proceso=''):
    while True:
        mensaje_nombre = 'Ingrese Nombre Usuario (o ENTER para conservar): '
        mensaje_contrasena = 'Ingrese Contraseña Usuario (o ENTER para conservar): '
        if proceso != None:
            mensaje_nombre = 'Ingrese Nombre Usuario: '
            mensaje_contrasena = 'Ingrese Contraseña Usuario: '
        nombre = input(mensaje_nombre)
        contrasena = getpass.getpass(mensaje_contrasena)
        if nombre != '' and contrasena != '':
            return nombre, contrasena