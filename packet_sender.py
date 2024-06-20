import socket
import sys
import string
import argparse


def printTest(server,payload):
    print("\nserver is: ")
    print("\n")
    print(server)
    print("\npayload is: ")
    print("\n")
    print(payload)

def stringToHex(string):
    temp = []
    
    stringHex = ''.join(hex(ord(char))for char in string)
    stringHex = stringHex.replace("0x"," ")
    stringHex = stringHex.split(" ")
    length = len(stringHex)
    for index in range(1,length-1,2):
        portion = [stringHex[index],stringHex[index+1]]
        word = ''.join(portion)
        temp.append(word)
        
    stringHex= ' '.join(temp)
    return stringHex
#needs work, not completely debugged yet
def checkSumCalculator(payloadheaderIP,headerLength,TOS,IPheaderLength,Identification,IPFlagsAndFragmentOffset,IPTTLandProtocol,sourceIP,destinationIP):
    temp =[]
    word1 = payloadheaderIP+headerLength+TOS
    word1 = stringToHex(word1)
    temp.append(word1)
    headerChecksum = stringToHex("0000")
    temp.append(headerChecksum)
    payloadheaderIPHex = stringToHex(payloadheaderIP)
    temp.append(payloadheaderIPHex)
    headerLengthHex=stringToHex(headerLength)
    temp.append(headerLengthHex)
    TOSHex=stringToHex(TOS)
    temp.append(TOSHex)
    IPheaderLengthHex= stringToHex(IPheaderLength)
    temp.append(IPheaderLengthHex)
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
    checksum = sum(temp)
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
    print(payloadHex)

     #may want to make these variables as user inputs, not sure yet
    IPheaderLength = "0028"
    Identification = "1c46"
    print("\n")
    sourceIP= str(input("Please input the sourceIP in the following format: xxx.xxx.x.x"))
    sourceIPHex = stringToHex(sourceIP)
    print("\n")
    destinationIP= str(input("Please input the sourceIP in the following format: xxx.xxx.x.x"))
    destinationIPHex = stringToHex(destinationIP)
    payloadheaderIP ="4"
    headerLength ="5"
    TOS ="00"
    IPFlagsAndFragmentOffset = "4000",
    IPTTLandProtocol ="4006"

    #checksum = "9D35" #need to implement  code to calculate checksum here, using hardcoded checksum here for now
    checksum = checkSumCalculator(payloadheaderIP,headerLength,TOS,IPheaderLength,Identification,IPFlagsAndFragmentOffset,IPTTLandProtocol,sourceIP,destinationIP)
    print(checksum)                   
    packet = encapsulatePacket(IPheaderLength,Identification,checkSum,sourceIP,destinationIP,payloadheaderIP ,headerLength ,TOS,IPFlagsAndFragmentOffset,IPTTLandProtocol)
    print(packet)
                       
    return 0

if __name__ == "__main__":
    main()


    
    

    
