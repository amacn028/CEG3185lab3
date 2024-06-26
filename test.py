import socket

def create_packet():
    hex_string = '123456789ABCDEF0123456789ABCDEF0123448656C6C6F2C20576F726C6421'
    hex_int = int(hex_string, 16)
    return bytes.fromhex(hex_string)

def main():
    PORT = 9879
    HOST = '127.0.0.1'  # Localhost

    packet = create_packet()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(packet)

if __name__ == "__main__":
    main()
