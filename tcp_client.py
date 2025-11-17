import socket
from protocol import send_msg, recv_msg
from tls_utils import create_ssl_context, wrap_socket

def tcp_client(host, port):

    ssl_context = create_ssl_context('client')
    
    with socket.create_connection((host, port)) as s:
        ssl_sock = wrap_socket(s, ssl_context, 'client')
        
        print(f"[TCP CLIENT] Connected to {host}:{port}")
        print(f"[TCP CLIENT] TLS enabled: YES")
        print("Type 'exit' to quit")
        
        with ssl_sock:
            print(f"[TCP CLIENT] TLS handshake completed")
            while True:
                message = input("You: ")
                if message.lower() == "exit":
                    print("[TCP CLIENT] Exiting...")
                    break
                send_msg(ssl_sock, message.encode())
                reply = recv_msg(ssl_sock)
                if reply is None:
                    print("[TCP CLIENT] Server closed connection")
                    break
                print(f"Server says: {reply.decode()}")