
import socket
import threading
from datetime import datetime

HOST = "0.0.0.0"
PORT = 8001


def atender_cliente(conn: socket.socket, addr: tuple) -> None:
    with conn:
        pedido = conn.recv(1024).decode("utf-8").strip()
        print(f"[{threading.current_thread().name}] {addr} pediu: {pedido!r}")
        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        conn.sendall(horario.encode("utf-8"))


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))
        servidor.listen()
        print(f"Servidor de horário escutando em {HOST}:{PORT}")
        while True:
            conn, addr = servidor.accept()
            threading.Thread(
                target=atender_cliente, args=(conn, addr), daemon=True
            ).start()


if __name__ == "__main__":
    main()