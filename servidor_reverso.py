
import socket
import threading

HOST = "0.0.0.0"
PORT = 8000

def atender_cliente(conn: socket.socket, addr: tuple) -> None:
    with conn:
        dados = conn.recv(1024)
        if not dados:
            return
        texto = dados.decode("utf-8")
        print(f"{addr} enviou: {texto!r}")
        conn.sendall(texto[::-1].encode("utf-8"))


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))
        servidor.listen()
        print(f"Servidor de string invertida escutando em {HOST}:{PORT}")
        while True:
            conn, addr = servidor.accept()
            threading.Thread(
                target=atender_cliente, args=(conn, addr), daemon=True
            ).start()


if __name__ == "__main__":
    main()