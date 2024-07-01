#Text in here describes how to run our code 
1) open an instance of idle
2) open packet_receiver.py with idle, run packet_receiver.py
3) open a command prompt window, change directory  to the directory of packet_receiver.py
4) in the command line prompt window type "python packet_receiver.py -ip xxx.xxx.x.x" ( fill in the server/source ip address as the x's)
5)  open another instance of idle
6) open packet_sender.py with idle, run packet_sender.py
7) open another command prompt window, change directory  to the directory of packet_sender.py
8) in the command line prompt window type "python packet_sender.py -server xxx.xxx.x.x -payload 'xxxxxxxxxxx' " ( fill in the server/source ip address, and the payload string  as the x's)
9) when prompted to fill in the source ip, ensure it matches that ip following "-server" in the command line prompt window , as shown above.
10) when prompted to fill in the destination ip, fillout whatever the destination ip address is needed


Test command line arguments: 

python packet_receiver.py -ip 127.0.0.1

python packet_sender.py -server 127.0.0.1 -payload "COLOMBIA 2 - MESSI  0"
