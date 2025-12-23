from datos.consultas import consulta_insert,consulta_nombre_usuario
from datos.conexion import insertar_datos,leer_dato_individual
from interfaces.interface_usuarios import solicitar_data_usuario
from modelos.usuario import Usuario
import bcrypt

def crear_usuario():
    campos = 'nombre_usuario,contrasena,habilitado'
    tabla = 'usuarios'
    nombre, contrasena = solicitar_data_usuario('crear')  # type: ignore
    if nombre != '' and contrasena != '':
        contrasena_encriptada = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
        datos = (nombre.title(), contrasena_encriptada, True)
        consulta = consulta_insert(campos, tabla)
        insertar_datos(consulta, datos, 'crear')
        
def login():
    nombre, contrasena = solicitar_data_usuario('crear')
    if nombre != '' and contrasena != '':
        campos = 'id_usuario,nombre_usuario,contrasena,habilitado'
        tabla = 'usuarios'
        dato = (nombre.title())
        consulta = consulta_nombre_usuario(campos, tabla)
        usuario_db = leer_dato_individual(consulta, dato)
        if usuario_db:
            usuario = Usuario(
                usuario_db[0],usuario_db[1],usuario_db[2],usuario_db[3]) # type: ignore
            contrasena_db = str(usuario.contrasena)
            if bcrypt.checkpw(contrasena.encode('utf-8'), contrasena_db.encode('utf-8')):
                return True
            else:
                print('Contraseña NO corresponde.')
        else:
            print('Usuario NO registrado.')