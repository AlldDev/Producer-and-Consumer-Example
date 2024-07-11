import queue
import threading
import time

class Producer:
    def __init__(self, fila, fila_lock, fila_event):
        self._fila = fila
        self._fila_lock = fila_lock
        self._fila_event = fila_event

    def producer(self):
        while True:
            #self._fila.put('Hello World')
            time.sleep(3)
          
            with self._fila_lock:
                self._fila.append('Hello World')
                print(f'Producer: Produzi algo: {self._fila[-1]}')
                self._fila_event.set()
