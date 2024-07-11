import queue
import threading
import consumer
import producer

if __name__ == '__main__':
    #fila = queue.Queue()
    fila = []
    fila_lock = threading.Lock()
    fila_event = threading.Event()

    cl = producer.Producer(fila, fila_lock, fila_event)
    sv = consumer.Consumer(fila, fila_lock, fila_event)

    tt_client = threading.Thread(target=cl.producer)
    tt_server = threading.Thread(target=sv.consumer)

    tt_client.start()
    tt_server.start()
