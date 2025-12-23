from modelos.localidad import Localidad
from modelos.avion import Avion


class Vuelo(Localidad, Avion):
    def __init__(self, id_vuelo=None, fecha_hora_salida=None, destino=None, origen=None, cod_vuelo=None, id_avion=None, tipo_vuelo=None, id_localidad=None):
        Localidad().__init__(id_localidad)
        Avion().__init__(id_avion)
        self.id_vuelo = id_vuelo
        self.fecha_hora_salida = fecha_hora_salida
        self.destino = destino
        self.origen = origen
        self.cod_vuelo = cod_vuelo
        self.tipo_vuelo = tipo_vuelo
        
    def obtener_id_vuelo(self):
        return self.id_vuelo
    
    def obtener_fecha_hora_salida(self):
        return self.fecha_hora_salida

    def obtener_codigo_vuelo(self):
        return self.cod_vuelo

    def obtener_tipo_vuelo(self):
        return self.tipo_vuelo

    def info_localidad(self):
        return super().obtener_info_localidad()
    
    def info_avion(self):
        return super().obtener_info_avion()