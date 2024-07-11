import queue
import threading

class Consumer:
    def __init__(self, fila, fila_lock, fila_event):
        self._fila = fila
        self._fila_lock = fila_lock
        self._fila_event = fila_event

    def consumer(self):
        while True:
            self._fila_event.wait()
            #data = self._fila.get()

            with self._fila_lock:
                data = self._fila.pop(0)
                print(f'Consumer: Consumi algo: {data}\n')

                self._fila_event.clear()
