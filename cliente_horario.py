import socket

HOST = "127.0.0.1"
PORT = 8001


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PORT))
        cliente.sendall("HORARIO".encode("utf-8"))
        resposta = cliente.recv(1024).decode("utf-8")
        print(f"Horário do servidor: {resposta}")


if __name__ == "__main__":
    main()