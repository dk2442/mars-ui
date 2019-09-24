import socket

HOST = '172.27.38.111'    # The remote host
PORT = 6666              # The same port as used by the server


def send4int(a, b, c, d):
    """
    the four bytes between the header bytes and the checksum are the data bytes. 
    Try to implement this function, send4int, that can send a, b, c, d, the parameters of this
    function, as the data bytes to the server. Note that you need to compute the checksum
    
    For example, send4int(1, 2, 3, 4) should send [0xff, 0xff, 1, 2, 3, 4, 10]. 
    You should get something like Received b'You send [255, 255, 1, 2, 3, 4, 10]\r\nThe checksum is correct'
    """
    seq = [0xff, 0xff, a, b, c, d, 0]
    checksum = sum(seq[0:6]) % 255
    seq[6] = checksum
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(seq * 2))
        print('Received', repr(s.recv(1024)))


send4int(1, 2, 3, 5)
send4int(127, 5, 19, 2)

