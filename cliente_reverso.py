
import socket

HOST = "127.0.0.1"
PORT = 8000
MENSAGEM = "Olá, Mundo Distribuído"


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PORT))
        cliente.sendall(MENSAGEM.encode("utf-8"))
        resposta = cliente.recv(1024).decode("utf-8")
        print(f"Enviado:  {MENSAGEM}")
        print(f"Recebido: {resposta}")


if __name__ == "__main__":
    main()