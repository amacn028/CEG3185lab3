import socket

def checksum(message):
    message_list_header = message.split()[0:9]
    decoded_checksum = int(0,16)
    for value in message_list_header():
        decoded_checksum =+ int(value, 16)

    string_checksum = hex(decoded_checksum).upper()
    if len(string_checksum) == 5:
        first_digit = int(string_checksum[0], 16)
        rest = int(string_checksum[1:], 16)
        decoded_checksum = first_digit + rest
    
    if decoded_checksum == 0xFFFF:
        return True
    else:
        return False


def get_payload(message):
    payload_list = message.split()[9:]
    payload_message = "".join(payload_list)
    bytes_message = bytes.fromhex(payload_message)
    decoded_message = bytes_message.decode('utf-8')
    return (decoded_message, len(payload_message)/2)


def get_ip(message):
    hex_ip = ''.join(message.split()[6:8])
    hex_octets = [hex_ip[i:i+2] for i in range(0, len(hex_ip), 2)]

    decimal_octets = [int(octet, 16) for octet in hex_octets]

    ip_address = ".".join(map(str, decimal_octets))
    return ip_address

    

def main():
    #Code to get the packet from server here 
    # message = what was received
    PORT = 9879

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data) #currently echoing to notify that the data has been sent but could use other format. 
    
    if not checksum(data):
        print("The verification of the checksum demonstrates that the packet recived is corrupted. Packet discared!")
        return
    
    payload, data_length = get_payload(data)
    ip = get_ip(data)

    print(f"The data recieved from {ip} is {payload} /n ")
    print(f"the data has {data_length*8} bits or {data_length} bytes. Total length of the packet is {data.strip().length()/2} bytes")
    print(f"The verification of the checksum demonstartes that the packet received is correct")

