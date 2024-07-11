import queue
import threading
import time

class Client_producer:
    def __init__(self, fila, fila_lock, fila_event):
        self._fila = fila
        self._fila_lock = fila_lock
        self._fila_event = fila_event

    def producer(self):
        while True:
            time.sleep(3)
            #self._fila.put('Hello World')
          
            with self._fila_lock:
                print('Client: Produzi algo')
                self._fila.append('Hello World')
                self._fila_event.set()
