import argparse
from tcp_server import tcp_server
from tcp_client import tcp_client

def main():
    parser = argparse.ArgumentParser(description="TCP client-server demo with TLS")
    parser.add_argument("--role", required=True, choices=["server", "client"], help="Role (client or server)")
    parser.add_argument("--host", default="localhost", help="Address to connect (client) or bind (server)")
    parser.add_argument("--port", type=int, default=8888, help="Port number (default 8888)")

    parser.add_argument("--certfile", help="Path to certificate file (server only)")
    parser.add_argument("--keyfile", help="Path to private key file (server only)")
    parser.add_argument("--cafile", help="CA certificate file (client only)")

    args = parser.parse_args()

    if args.role == "server":
        tcp_server(args.host, args.port, args.certfile, args.keyfile)
    elif args.role == "client":
        tcp_client(args.host, args.port, args.cafile)

if __name__ == "__main__":
    main()