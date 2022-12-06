import RPi.GPIO as GPIO
import MFRC522

# signal

class RFID:
  """
  Clase utilizada para representar un lector RFID

  Atributos
    reader (MFRC522): Objeto utilizado para realizar la lectura
  """


  def __init__(self):
    """
    Constructor por default
    """
    self.__reader = MFRC522.MFRC522()

  def uidToString(self, uid):

    stringUID = ""

    for i in uid:
      stringUID = format(i, '02X') + stringUID

    return stringUID

  def read(self):

    print("Detectando tarjeta...")

    leyendo = True

    while leyendo:

      # Escanear
      (status, TagType) = self.__reader.MFRC522_Request(self.__reader.PICC_REQIDL)

      # Si se detecta tarjeta
      if status == self.__reader.MI_OK:

        # Obtener UID de la tarjeta
        (status, uid) = self.__reader.MFRC522_SelectTagSN()

        # Si se tiene el UID, continuar
        if status == self.__reader.MI_OK:

          print("UID de la tarjeta: %s" % self.uidToString(uid))

          # Aqui se desbloquearía la puerta y se checa lo de las camaras

          # Salir de lectura
          leyendo = False

        else:
          print("Error de autenticacion")

  # Check - Solo es un objeto para las dos RFID