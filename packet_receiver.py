def integerToHex(lst):
    string = ''
    spacing =''
    for item in lst:
        if len(str(item))<4:
            
            item = hex(item)
            item = item.replace("0x","")
            for index in range(0,4-len(str(item)),1):
                spacing="0"+spacing
                
            string=string+" "+spacing+item
            spacing = ''
        else:
            item = hex(item)
            item = item.replace("0x","")
            string=string+" "+item
    return string




def main():
    #Code to get the packet from server here 
    # message = what was received 
    if not checksum(message):
        print("The verification of the checksum demonstrates that the packet recived is corrupted. Packet discared!")
        return
    
    payload, data_length = get_payload(message)
    ip = get_ip(message)

    print(f"The data recieved from {ip} is {payload} /n ")
    print(f"the data has {data_length} bits or {data_length/8} bytes. Total length of the packet is {(message.strip()length())/2} bytes")
    print(f"The verification of the checksum demonstartes that the packet received is correct")

