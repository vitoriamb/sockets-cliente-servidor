# Cliente/Servidor com Sockets
Atividade de Sistemas Distribuídos: modelo cliente/servidor com sockets TCP.

**Aluna:** Vitória Maciel Bernardo

## Questão 1: Servidor de horário (multithread)

O servidor atende um pedido por conexão e devolve a data e hora atuais. Cada cliente é atendido em uma thread própria. O cliente pede o horário, imprime e encerra.

- `servidor_horario.py` (porta 8001)
- `cliente_horario.py`

## Questão 2: Servidor de string invertida

O servidor escuta na porta 8000, recebe uma string, inverte e devolve. O cliente envia "Olá, Mundo Distribuído" e imprime a resposta.

- `servidor_reverso.py` (porta 8000)
- `cliente_reverso.py`

## Como executar

Em um terminal, inicie o servidor. Em outro, rode o cliente:

    python3 servidor_reverso.py
    python3 cliente_reverso.py

    python3 servidor_horario.py
    python3 cliente_horario.py

Requisito: Python 3 (só biblioteca padrão).
