from enum import Enum, auto
import time

class States(Enum):
    INTERFACE_NOK = auto()
    INTERFACE_OK = auto()
    PACOTE_OK_RECEBIDO = auto()
    PACOTE_NOK_RECEBIDO = auto()
    SEM_RESPOSTA = auto()

class Events(Enum):
    START = auto()
    CONFIG = auto()
    KEEP_ALIVE = auto()

class Comunication:
    def __init__(self):
        self.__state = States.INTERFACE_NOK

    @classmethod
    def set_state(cls,state):
        cls.__state = state
    
    @classmethod
    def get_state(cls):
        return cls.__state

class Master(Comunication):
    
    def comunicate(self, atual, evento=None):

        if atual == States.INTERFACE_OK and evento==None:
            if self.envia_start():
                self.set_state(States.PACOTE_OK_RECEBIDO)
                return self.get_state(), Events.START
            else:
                self.set_state(States.PACOTE_NOK_RECEBIDO)
                return  self.get_state(), Events.START
        

        elif atual == States.PACOTE_OK_RECEBIDO:
            if evento == Events.START:
                if self.envia_config():
                    self.set_state(States.PACOTE_OK_RECEBIDO)
                    return self.get_state(), Events.CONFIG
                else:
                    self.set_state(States.PACOTE_NOK_RECEBIDO)
                    return self.get_state(), Events.CONFIG


            elif evento == Events.CONFIG:
                if self.manda_keep_alive():
                    self.set_state(States.PACOTE_OK_RECEBIDO)
                    return self.get_state(), Events.KEEP_ALIVE
                else:
                    self.set_state(States.PACOTE_NOK_RECEBIDO)
                    return self.get_state(), Events.KEEP_ALIVE

            elif evento == Events.KEEP_ALIVE:
                if self.manda_keep_alive():
                    self.set_state(States.PACOTE_OK_RECEBIDO)
                    return self.get_state(), Events.KEEP_ALIVE
                else:
                    self.set_state(States.PACOTE_NOK_RECEBIDO)
                    return self.get_state(), Events.KEEP_ALIVE


        elif atual == States.PACOTE_NOK_RECEBIDO:
            if evento == Events.START:
                if self.envia_start():
                    self.set_state(States.PACOTE_OK_RECEBIDO)
                    return self.get_state(), Events.START
                else:
                    self.set_state(States.PACOTE_NOK_RECEBIDO)
                    return self.get_state(), Events.START

            elif evento == Events.CONFIG:
                if self.envia_config():
                    self.set_state(States.PACOTE_OK_RECEBIDO)
                    return self.get_state(), Events.CONFIG
                else:
                    self.set_state(States.PACOTE_NOK_RECEBIDO)
                    return self.get_state(), Events.CONFIG

            elif evento == Events.KEEP_ALIVE:
                if self.envia_start():
                    self.set_state(States.PACOTE_OK_RECEBIDO)
                    return self.get_state(), Events.KEEP_ALIVE
                else:
                    self.set_state(States.PACOTE_NOK_RECEBIDO)
                    return self.get_state(), Events.KEEP_ALIVE
        
        elif atual == States.SEM_RESPOSTA and evento == Events.START:
                if self.envia_start():
                    self.set_state(States.PACOTE_OK_RECEBIDO)
                    return self.get_state(), Events.START
                else:
                    self.set_state(States.PACOTE_NOK_RECEBIDO)
                    return self.get_state(), Events.START


    def envia_start(self):
        print('enviando start...')
        return True

    def envia_config(self):
        print('enviando dados de configurações...')
        return True


    def manda_keep_alive(self):
        print('mandando sinal keep-alive...')
        return True


if __name__ == '__main__':

    switch = Master()

    state,event = switch.comunicate(States.INTERFACE_OK)

    while True:
        state,event = switch.comunicate(state,event)
        time.sleep(3)
