import socket
import argparse
from protocol import send_msg, recv_msg
from tls_utils import create_ssl_context, wrap_socket

def tcp_server(host, port, certfile=None, keyfile=None):
    ssl_context = create_ssl_context('server', certfile, keyfile)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        print(f"[TCP SERVER] Listening on {host}:{port}...")
        print(f"[TCP SERVER] TLS enabled: YES")
        if certfile:
            print(f"[TCP SERVER] Using certificate: {certfile}")
        
        while True:
            conn, addr = s.accept()
            ssl_conn = wrap_socket(conn, ssl_context, 'server')
            
            with ssl_conn:
                print(f"[TCP SERVER] TLS connection established with {addr}")
                try:
                    while True:
                        data = recv_msg(ssl_conn)
                        if data is None:
                            print("[TCP SERVER] Client disconnected")
                            break
                        text = data.decode()
                        print(f"[CLIENT]: {text}")
                        response = f"Got it! I also {text}".encode()
                        send_msg(ssl_conn, response)
                except ssl.SSLError as e:
                    print(f"[TCP SERVER] SSL error: {e}")
                except Exception as e:
                    print(f"[TCP SERVER] Error: {e}")