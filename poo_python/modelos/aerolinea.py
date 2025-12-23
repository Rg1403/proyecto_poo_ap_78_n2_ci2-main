# Definición de clase Aerolínea
class Aerolinea:
    # Constructor de la clase
    def __init__(self, id_aerolinea=None, nombre_aerolinea=None, web_aerolinea=None):
        # atributos privados, ENCAPSULACIÓN
        self.id_aerolinea = id_aerolinea
        self.nombre_aerolinea = nombre_aerolinea
        self.web_aerolinea = web_aerolinea

    # Métodos públicos de acceso a atributos privados
    def obtener_info_aerolinea(self):
        return self.id_aerolinea,self.nombre_aerolinea,self.web_aerolinea
    
    def obtener_id_aerolinea(self):
        return self.id_aerolinea
    
    def obtener_nombre_aerolinea(self):
        return self.nombre_aerolinea

    def obtener_web_aerolinea(self):
        return self.web_aerolinea
