# Libssh-Authentication-Bypass
Spawn to shell without any credentials by using CVE-2018-10933

Information write-up about CVE-2018-10933 by libSSH : https://www.libssh.org/security/advisories/CVE-2018-10933.txt

## Create a vulnerable ssh server:

Download, uncompress and build the vulnerable LibSSH Version : https://www.libssh.org/files/0.7/libssh-0.7.4.tar.xz

And then run libssh on your own server.

## LibSSH authentication bypass with tool that i wrote

```
pip install paramiko==2.0.8
pip install socket

python libsshauthbypass.py
```
