
import socket
import argparse

def checksum(message):
    
    message_list_header = message.split()[0:10]
   
    decoded_checksum = 0
    for value in message_list_header:
        decoded_checksum += int(value, 16)
    
    string_checksum = hex(decoded_checksum).upper()
    string_checksum = string_checksum.replace("0X","")
    
    if len(string_checksum) > 4:
        first_digit = int(string_checksum[0], 16)
        
        rest = int(string_checksum[1:], 16)
        decoded_checksum = first_digit + rest
        decoded_checksum = hex(decoded_checksum).upper().replace("0X","0x")
        
    
    if decoded_checksum == "0xFFFF":
        
        return True
    else:
        
        return False


def get_payload(message):
    
    message_list =message.split(" ")
   
    payload_list = message.split(" ")[10:]
   
    payload_message = "".join(payload_list)
    
    bytes_message = bytes.fromhex(payload_message)
    decoded_message = bytes_message.decode('utf-8')
   
    return (decoded_message, len(message_list))


def get_ip(message):
    hex_ip = ''.join(message.split()[6:8])
    hex_octets = [hex_ip[i:i+2] for i in range(0, len(hex_ip), 2)]

    decimal_octets = [int(octet, 16) for octet in hex_octets]

    ip_address = ".".join(map(str, decimal_octets))
    return ip_address

    

def main():
    #Code to get the packet from server here 
    # message = what was received
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", type=str, required=True, help="Server IP address")
    args = parser.parse_args()
    PORT = 9879

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((args.ip, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                byte_data = conn.recv(1024)
                if not byte_data:
                    break
                print(byte_data)
                data = byte_data.decode('utf-8')
                header_bytes = byte_data[:50]  # Assuming header is 20 bytes (2 fields * 2 bytes each)
                payload_bytes = byte_data[50:]
                if not checksum(header_bytes):
                    print("The verification of the checksum demonstrates that the packet recived is corrupted. Packet discarded!")
                    
                    continue
                #conn.sendall(data) #currently echoing to notify that the data has been sent but could use other format. 
    
                payload, data_length = get_payload(data)
                ip = get_ip(data)

                print(f"The data recieved from {ip} is {payload} \n ")
                print(f"the data has {data_length*8} bits or {data_length} bytes. Total length of the packet {data_length*2} bytes")
                print(f"The verification of the checksum demonstrates that the packet received is correct")
            
    

if __name__ == "__main__":
    main()






