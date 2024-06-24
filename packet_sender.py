import socket
import sys
import string
import argparse
import binascii
from decimal import Decimal

def printTest(server,payload):
    print("\nserver is: ")
    print("\n")
    print(server)
    print("\npayload is: ")
    print("\n")
    print(payload)
#rename this string to integer honestly 
def stringToHex(string):
    hex_list =[]
    temp = []
    hex_value=[]
    testlist=[]

    if(string.isalnum() == True):
        
        string=list(string)
        stringlength=len(string)
        for index in range(0,stringlength,1):
            string[index] = int(string[index],base = 16)
            value = string[index]*(16**(stringlength-index-1))
            hex_value.append(value)
        word = sum(hex_value)
        #print("\nhex_value is: ",hex_value)      
        hex_list.append(word)
        hex_value.clear()
        return hex_list
        #print("\ntest is: ",testlist)
    print("\nstring is: ",string)
    if(type(string)==list):
        print("\nflag list")
        stringlength=len(string)
        for index in range(0,stringlength,1):
            string[index] = int(str(string[index]),base = 16)
            value = string[index]*(16**(stringlength-index-1))
            hex_value.append(value)
        word = sum(hex_value)
        #print("\nhex_value is: ",hex_value)      
        hex_list.append(word)
        hex_value.clear()
        return hex_list
        
    stringHex2=string.replace(".","")
    
    if(stringHex2.isdigit()):
        print("test flag")
        stringHex=string.split(".")
        print(stringHex)
        stringlength=len(stringHex)
        
        for index in range(0,stringlength,1):
            stringHex[index] = int(stringHex[index],base = 16)
            value = stringHex[index]*(16**(stringlength-index-1))
            hex_value.append(stringHex[index])
        word = sum(hex_value)
        #word = int(word)
        print("\nword is: ",word)
        print(type(word))
        hex_list.append(word)
        hex_value.clear()
        print("\ntest is: ",hex_list) 
        return hex_list
               
    else:
        
            
            
        stringHex = ''.join(hex(ord(char))for char in string)
        stringHex = stringHex.replace("0x"," ")
        stringHex = stringHex.split(" ")
        print("\nstringHex is: ",stringHex) 
        length = len(stringHex)
        for index in range(1,length-1,2):
            portion = [stringHex[index],stringHex[index+1]]
            word = ''.join(portion)
            temp.append(word)
        print("\ntemp is: ",temp)    
        stringHex= ' '.join(temp)
    
        tempLength = len(temp)
        for index in range(0,tempLength,1):
            word = list(temp[index])
            testlist.append(word)
            wordLength= len(word)
            for index in range(0,wordLength,1):
                word[index] = int(word[index],base =16)
                value = word[index]*(16**(wordLength-index-1))
                hex_value.append(value)
            word = sum(hex_value)
            print("\nhex_value is: ",hex_value)      
            hex_list.append(word)
            hex_value.clear()
          
    
    return hex_list

def checkSumCalculator(payloadheaderIP,headerLength,TOS,IPheaderLength,Identification,IPFlagsAndFragmentOffset,IPTTLandProtocol,sourceIP,destinationIP):
    temp =[]
    word1 = payloadheaderIP+headerLength+TOS
    word1=stringToHex(word1)
    print("\ntest is: ",word1)
    temp.append(word1)
    headerChecksum = stringToHex("0000")
    temp.append(headerChecksum)
    IPheaderLengthHex= stringToHex(IPheaderLength)
    temp.append(IPheaderLengthHex)
    print("\ntemp is: ",temp)
    IdentificationHex = stringToHex(Identification)
    temp.append(IdentificationHex)
    IPFlagsAndFragmentOffsetHex=stringToHex(IPFlagsAndFragmentOffset)
    temp.append(IPFlagsAndFragmentOffsetHex)
    IPTTLandProtocolHex=stringToHex(IPTTLandProtocol)
    temp.append(IPTTLandProtocolHex)
    
    
    sourceIPHex = stringToHex(sourceIP)
    temp.append(sourceIPHex)
    destinationIPHex = stringToHex(destinationIP)
    temp.append(destinationIPHex)
    
    
    
    print("\ntemp is: ",temp)
    temp = [item for sublist in temp for item in sublist]
    print("\ntemp is: ",temp)
    checksum = sum(temp)
    print("\nchecksum is: ",checksum)
    return checksum
    
 #needs testing still, need to fix checkSumCalculator first
def encapsulatePacket(IPheaderLength,Identification,checkSum,sourceIP,destinationIP,
                      payloadheaderIP ="4",headerLength ="5",TOS ="00",
                      IPFlagsAndFragmentOffset = "4000",
                      IPTTLandProtocol ="4006"):
   
    packet = headerIP+headerLength+TOS+" "+IPheaderLength+" "+Identification+" "+IPFlagsAndFragmentOffset+" "+IPTTLandProtocol+" "+checksum+" "+sourceIPHex+" "+destinationIPHex+" "+payload

    return packet


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-server",type = str,required = True,action ="store")
    parser.add_argument("-payload",type = str,required = True,action = "store")
    args = parser.parse_args()

    server = args.server
    payload = args.payload

    payloadHex = stringToHex(payload)
    serverHex = stringToHex(server)
    
    #print(payloadHex)

     #may want to make these variables as user inputs, not sure yet
    testSource = "192.168.0.3"
    testDestination = "192.168.0.1"


    
    print("\n")
    print("conversion test begin: ")
    print("\n",testSource)
    print("\n",testDestination)
    IdentificationHex = stringToHex(testSource)
    IPheaderLengthHex =stringToHex(testDestination)
    
    
    print("\nconversion test conclude: ")

    print("\n",IdentificationHex)
    print("\n",IPheaderLengthHex)


    
    sourceIP= str(input("Please input the sourceIP in the following format xxx.xxx.x.x: "))
    sourceIPHex = stringToHex(sourceIP)
    print("\n")
    destinationIP= str(input("Please input the sourceIP in the following format xxx.xxx.x.x: "))
    destinationIPHex = stringToHex(destinationIP)
    payloadheaderIP ="4"
    headerLength ="5"
    TOS ="00"
    IPFlagsAndFragmentOffset = "4000"
    IPTTLandProtocol ="4006"
    IPheaderLength ="0028"
    Identification ="1c46"

    #checksum = "9D35" #need to implement  code to calculate checksum here, using hardcoded checksum here for now
    checksum = checkSumCalculator(payloadheaderIP,headerLength,TOS,IPheaderLength,Identification,IPFlagsAndFragmentOffset,IPTTLandProtocol,sourceIP,destinationIP)
    print("\n checksum is: ", checksum)                   
    packet = encapsulatePacket(IPheaderLength,Identification,checksum,sourceIP,destinationIP,payloadheaderIP ,headerLength ,TOS,IPFlagsAndFragmentOffset,IPTTLandProtocol)
    print(packet)
                       
    return 0

if __name__ == "__main__":
    main()


#############################################################################
'''

# Create a TCP/IP socket
Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10800)
print ('connecting to ', server_address)
Client_socket.connect(server_address)

##After the connection is established, data can be sent through the socket with sendall() and received with recv(), just as in the server.

try:
    
    # Send data
    # message = b'This is a massage from hamzah.  It will be repeated.'
    # you can enter the massage from keyboard this way. instead of the fixed massage above
    value = input("Please enter  the massage you want to be echoed:\n")
    message = value.encode('utf-8')
    print( 'sending : ' ,  message)
    Client_socket.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    
    
    # here we choose the size of the buffer e.g. 100 
    while amount_received < amount_expected:
        data = Client_socket.recv(100)
        amount_received += len(data)
        print ('received :' , data) 

finally:
    print('closing socket')
    Client_socket.close()
    
'''

    
