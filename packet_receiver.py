import socket
import argparse

def checksum(message):
    message_list_header = message.split()[0:9]
    for item in message_list_header:
        print('message_list_header: '+ item.decode('utf-8') + '\n')
    decoded_checksum = 0
    for value in message_list_header:
        decoded_checksum += int(value, 16)

    print('decoded_checksum: ' + decoded_checksum + '\n')
    string_checksum = hex(decoded_checksum).upper().replace("0x","")
    print("string_checksum" +str(string_checksum)+ "\n")
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
    return (decoded_message, len(payload_list)*2)


def get_ip(message):
    hex_ip = ''.join(message.split()[6:8])
    hex_octets = [hex_ip[i:i+2] for i in range(0, len(hex_ip), 2)]

    decimal_octets = [int(octet, 16) for octet in hex_octets]

    ip_address = ".".join(map(str, decimal_octets))
    return ip_address

    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", type=str, required=True, help="Server IP address")
    args = parser.parse_args()
    PORT = 9879

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((args.ip, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                byte_data = conn.recv(1024)
                if not byte_data:
                    break
                data = byte_data.decode('utf-8')
                print('data recieved: '+ data)
                header_bytes = byte_data[:20]  # Assuming header is 20 bytes (2 fields * 2 bytes each)
                payload_bytes = byte_data[20:]
                if not checksum(header_bytes):
                    print("The verification of the checksum demonstrates that the packet recived is corrupted. Packet discared!")
                    continue
                
                conn.send(byte_data) #currently echoing to notify that the data has been sent but could use other format. 
    
                payload, data_length = get_payload(data)
                ip = get_ip(data)

                print(f"The data recieved from {ip} is {payload} /n ")
                print(f"the data has {data_length*8} bits or {data_length} bytes. Total length of the packet is {len(data.strip())/2} bytes")
                print(f"The verification of the checksum demonstartes that the packet received is correct")



if __name__ == "__main__":
    main()