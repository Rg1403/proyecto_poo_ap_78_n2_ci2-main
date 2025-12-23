from modelos.aerolinea import Aerolinea


class Avion(Aerolinea):
    def __init__(self, id_avion=None, cod_avion=None, tipo_avion=None, capacidad_avion=None, id_aerolinea=None):
        super().__init__(id_aerolinea)
        self.id_avion = id_avion
        self.cod_avion = cod_avion
        self.tipo_avion = tipo_avion
        self.capacidad_avion = capacidad_avion

    def obtener_info_avion(self):
        return self.cod_avion, self.tipo_avion, self.capacidad_avion

    def obtener_id_avion(self):
        return self.id_avion

    def obtener_cod_avion(self):
        return self.cod_avion

    def obtener_tipo_avion(self):
        return self.tipo_avion

    def obtener_capacidad_avion(self):
        return self.capacidad_avion

    def info_aerolinea(self):
        return super().obtener_info_aerolinea()
