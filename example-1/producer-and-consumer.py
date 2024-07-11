import threading
import time

class Tela:
    def __init__(self):
        self._buffer = []                       # Buffer
        self._buffer_lock = threading.Lock()    # Lock para o Buffer
        self._buffer_event = threading.Event()  # Event para o buffer

        # Status das threads para uma janela (True = sendo executada, False = Parar)
        self._consumer_status = True
        self._producer_status = True

        # Iniciando as threads para rodarem simultaneamente
        consumer_thread = threading.Thread(target=self.consumer, args=())
        producer_thread = threading.Thread(target=self.producer, args=(10,))

        # Iniciando as Threads
        consumer_thread.start()
        producer_thread.start()

    # Thread para colocar dados no buffer
    # nesse caso ainda é necessário tratar qual é a mensagem que estamos recebendo
    # para chamar o buffer da interface certa (mensagem, status, etc)
    # e essa função possivelmente ficará dentro de APP, pois vai ter apenas ela produzindo
    def producer(self, delay):
        # Enquanto estivermos executando
        while self._producer_status:
            # Simula a demora entre as mensagens recebida
            time.sleep(delay)

            with self._buffer_lock:
                self._buffer.append('Hello World')
                self._buffer_event.set()

    # Thread para retirar os dados de dentro do Buffer
    # terá uma dessa para cada janela, onde a producer
    # irá tratar e subir o event para a janela correta
    def consumer(self):
        # Enquanto estivermos executando
        while self._consumer_status:
            # Aqui a mágica acontece, chamando essa linha, a thread vai ficar
            # dormindo até ter algo pra ela tratar, que é quando a producer
            # subir o event
            self._buffer_event.wait()

            # Se o event for ativado, quer dizer que temos algo
            # no buffer para ser tratado
            with self._buffer_lock:
                # Aqui vamos remover apenas uma mensagem, porem temos que tratar
                # (possivel laço), para poder remover todas de dentro
                msg = self._buffer.pop(0)
                print(f'Mensagem Recebida: {msg}')

                # Agora limpamos o evento para poder reutiliza-lo
                self._buffer_event.clear()

    # Caso queira parar a execução (kkkkkkkkkk)
    def stop_with_rolling_stones(self):
        print('"Deus abençoe a Americaaa !!"')
        self._consumer_status = False
        self._producer_status = False

if __name__ == "__main__":
    tela = Tela()
    time.sleep(60)
    tela.stop_with_rolling_stones()
