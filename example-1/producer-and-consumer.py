import threading
import time

class ProducerAndConsumer:
    def __init__(self):
        self._buffer = []                       # Buffer
        self._buffer_lock = threading.Lock()    # Lock para o Buffer
        self._buffer_event = threading.Event()  # Event para o buffer

        self._producer_status = True
        self._consumer_status = True
        
        # Iniciando as threads para rodarem simultaneamente
        self._producer_thread = threading.Thread(target=self.producer, args=(10,))
        self._consumer_thread = threading.Thread(target=self.consumer, args=())
        
    def producer(self, delay):
        while self._producer_status:
            time.sleep(delay)

            with self._buffer_lock:
                self._buffer.append('Hello World')
                print(f'Coloquei no Buffer: {self._buffer[-1]}')
                # Subindo o evento para a consumer saber
                self._buffer_event.set()

    def consumer(self):
        while self._consumer_status:
            # Aguarda até a producer subir o evento
            self._buffer_event.wait()

            with self._buffer_lock:
                msg = self._buffer.pop(0)
                print(f'Removi do Buffer: {msg}')

                # Limpamos o evento para poder reutiliza-lo
                self._buffer_event.clear()

    # Iniciando as Threads
    def run(self):
        print('Threads iniciadas!\nEm 60 segundos encerrarei a execução!')
        self._consumer_thread.start()
        self._producer_thread.start()

    # Caso queira parar a execução (kkkkkkkkkk)
    def stop_with_rolling_stones(self):
        print('"Deus abençoe a Americaaa !!"')
        self._consumer_status = False
        self._producer_status = False

        self._consumer_thread.join()
        self._producer_thread.join()

if __name__ == "__main__":
    conceito = ProducerAndConsumer()
    conceito.run()

    time.sleep(60)
    conceito.stop_with_rolling_stones()
