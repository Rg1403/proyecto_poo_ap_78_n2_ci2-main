# Definición de clase Usuario
class Usuario:
    # Constructor de la clase
    def __init__(self, id_usuario=None, nombre_usuario=None, contrasena=None, habilitado=None):
        # atributos privados, ENCAPSULACIÓN
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.habilitado = habilitado

    # Métodos públicos de acceso a atributos privados
    def obtener_info_usuario(self):
        return self.id_usuario,self.nombre_usuario
    
    def obtener_id_usuario(self):
        return self.id_usuario
    
    def obtener_nombre_usuario(self):
        return self.nombre_usuario

    def obtener_usuario_habilitado(self):
        return self.habilitado