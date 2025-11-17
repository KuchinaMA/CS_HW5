import ssl
import os

def create_ssl_context(role='server', certfile=None, keyfile=None):

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH if role == 'server' else ssl.Purpose.SERVER_AUTH)

    if 'SSLKEYLOGFILE' in os.environ:
        context.keylog_filename = os.environ['SSLKEYLOGFILE']
        print(f"[TLS] Key logging enabled: {os.environ['SSLKEYLOGFILE']}")
    
    if role == 'server':
        if certfile and keyfile:
            context.load_cert_chain(certfile=certfile, keyfile=keyfile)
            print(f"[TLS] Loaded certificate: {certfile}, key: {keyfile}")
        else:
            print("[TLS] Warning: Running server without certificate")

    if role == 'client':
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
    
    return context

def wrap_socket(sock, context, role='server'):

    if role == 'server':
        return context.wrap_socket(sock, server_side=True)
    else:
        return context.wrap_socket(sock, server_side=False)