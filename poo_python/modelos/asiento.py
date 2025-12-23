# Importación súper clases Vuelo, Pasajero
from modelos.vuelo import Vuelo
from modelos.pasajero import Pasajero

# Definición de clase Asiento, con HERENCIA desde Vuelo


class Asiento(Vuelo):
    # Constructor de la clase Asiento
    def __init__(self, id_asiento=None, id_vuelo=None, categoria=None, num_asiento=None):
        # atributos privados, ENCAPSULACIÓN
        Vuelo().__init__(id_vuelo)
        self.id_asiento = id_asiento
        self.categoria = categoria
        self.num_asiento = num_asiento

    # Métodos públicos de acceso a atributos privados
    def obtener_categoria_asiento(self):
        return self.categoria

    def obtener_numero_asiento(self):
        return self.num_asiento

    # Accediendo a los atributos y méetodos de la súper clase
    def info_vuelo(self):
        return super().obtener_codigo_vuelo()
