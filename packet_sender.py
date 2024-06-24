import socket
import sys
import string
import argparse

ip_address_list =[]
sliced_ip_address_list=[]
def printTest(server,payload):
    print("\nserver is: ")
    print("\n")
    print(server)
    print("\npayload is: ")
    print("\n")
    print(payload)
 
def stringToHexEquivalentIntegerValue(string):
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
            
        hex_list.append(word)
        hex_value.clear()
        return hex_list
        
    
    if(type(string)==list):
        
        stringlength=len(string)
        for index in range(0,stringlength,1):
            string[index] = int(str(string[index]),base = 16)
            value = string[index]*(16**(stringlength-index-1))
            hex_value.append(value)
        word = sum(hex_value)
              
        hex_list.append(word)
        hex_value.clear()
        return hex_list
        
    stringHex2=string.replace(".","")
    
    if(stringHex2.isdigit()):
        
        stringHex=string.split(".")  
        
        for item in stringHex:
            value = int(item)
            value = hex(value)
            value = value.replace("0x","")
            testlist.append(value)
            
        stringlength= len(testlist)
        for index in range(0,stringlength,2):
            portion = [testlist[index],testlist[index+1]]
            
            word = ''.join(portion)
            temp.append(word)
            
            wordLength= len(word)
        
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
            word = int(word)
            ip_address_list.append(word)   
            hex_list.append(word)
            
            
            
            summation = sum(hex_list)
            hex_list.clear()
            
            hex_value.clear()
            hex_list.append(summation)
        
       
         
        return hex_list
               
    else:
        
            
            
        stringHex = ''.join(hex(ord(char))for char in string)
        stringHex = stringHex.replace("0x"," ")
        stringHex = stringHex.split(" ")
         
        length = len(stringHex)
        for index in range(1,length-1,2):
            portion = [stringHex[index],stringHex[index+1]]
            word = ''.join(portion)
            temp.append(word)
            
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
                 
            hex_list.append(word)
            hex_value.clear()
          
    
    return hex_list

def checkSumCalculator(payloadheaderIP,headerLength,TOS,IPheaderLength,Identification,IPFlagsAndFragmentOffset,IPTTLandProtocol,sourceIP,destinationIP):
    temp =[]
    hex_list =[]
    hex_value=[]
    word1 = payloadheaderIP+headerLength+TOS
    word1=stringToHexEquivalentIntegerValue(word1)
    
    temp.append(word1)
    headerChecksum = stringToHexEquivalentIntegerValue("0000")
    temp.append(headerChecksum)
    IPheaderLengthHex= stringToHexEquivalentIntegerValue(IPheaderLength)
    temp.append(IPheaderLengthHex)
    
    IdentificationHex = stringToHexEquivalentIntegerValue(Identification)
    temp.append(IdentificationHex)
    IPFlagsAndFragmentOffsetHex=stringToHexEquivalentIntegerValue(IPFlagsAndFragmentOffset)
    temp.append(IPFlagsAndFragmentOffsetHex)
    IPTTLandProtocolHex=stringToHexEquivalentIntegerValue(IPTTLandProtocol)
    temp.append(IPTTLandProtocolHex)
    
    
    sourceIPHex = stringToHexEquivalentIntegerValue(sourceIP)
    temp.append(sourceIPHex)
    destinationIPHex = stringToHexEquivalentIntegerValue(destinationIP)
    temp.append(destinationIPHex)
    
    
    
    
    temp = [item for sublist in temp for item in sublist]
    
    checksum = sum(temp)
    test = hex(checksum)
    
    stringHex = test.replace("0x","")
    checksumlength = len(test)
    if checksumlength>4:
        
        
        word2 = stringHex[1:]
        word3 =stringHex[:1]
        
        word1 = list(word2)
        wordLength=len(word2)
        for index in range(0,wordLength,1):
                word1[index] = int(word1[index],base =16)
                value = word1[index]*(16**(wordLength-index-1))
                hex_value.append(value)
        word = sum(hex_value)
                 
        hex_list.append(word)
        hex_list.append(int(word3))
        hex_value.clear()
        
        value=sum(hex_list)
        ones_comp = 65535-value
        checksum=hex(ones_comp)
        checksum=checksum.replace("0x","")
    
    return checksum
    
def integerToHex(lst):
    string = ''
    for item in lst:
        if item>16:
            item = hex(item)
            item = item.replace("0x","")
            string=string+" "+item
        else:
            item = hex(item)
            item = item.replace("0x","")
            string=string+" "+"000"+item
            
    return string


def encapsulatePacket(IPheaderLength,Identification,checksum,sourceIPandDestinationIPWord,payload,
                      payloadheaderIP ="4",headerLength ="5",TOS ="00",
                      IPFlagsAndFragmentOffset = "4000",
                      IPTTLandProtocol ="4006"):
   
    packet = payloadheaderIP+headerLength+TOS+" "+IPheaderLength+" "+Identification+" "+IPFlagsAndFragmentOffset+" "+IPTTLandProtocol+" "+checksum+sourceIPandDestinationIPWord+payload

    return packet


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-server",type = str,required = True,action ="store")
    parser.add_argument("-payload",type = str,required = True,action = "store")
    args = parser.parse_args()

    server = args.server
    payload = args.payload

    payloadHex = stringToHexEquivalentIntegerValue(payload)
    serverHex = stringToHexEquivalentIntegerValue(server)
    
   
    


    
    sourceIP= str(input("Please input the sourceIP in the following format xxx.xxx.x.x: "))
    sourceIPHex = stringToHexEquivalentIntegerValue(sourceIP)
    print("\n")
    destinationIP= str(input("Please input the sourceIP in the following format xxx.xxx.x.x: "))
    destinationIPHex = stringToHexEquivalentIntegerValue(destinationIP)
    
    payloadheaderIP ="4"
    headerLength ="5"
    TOS ="00"
    IPFlagsAndFragmentOffset = "4000"
    IPTTLandProtocol ="4006"
    IPheaderLength ="0028"
    Identification ="1c46"
    
    
    checksum = checkSumCalculator(payloadheaderIP,headerLength,TOS,IPheaderLength,Identification,IPFlagsAndFragmentOffset,IPTTLandProtocol,sourceIP,destinationIP)
    
    sliced_ip_address_list= ip_address_list[:4:1]
    
    word1 = integerToHex(sliced_ip_address_list)
    
    #payloadHex = integerToHex(payloadHex)
    packet = encapsulatePacket(IPheaderLength,Identification,checksum,word1,str(payloadHex),payloadheaderIP ,headerLength ,TOS,IPFlagsAndFragmentOffset,IPTTLandProtocol)
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

    
