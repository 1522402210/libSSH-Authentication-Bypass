# libSSH-Authentication-Bypass
Spawn to shell without any credentials by using CVE-2018-10933

Information about CVE-2018-10933 by libSSH : https://www.libssh.org/security/advisories/CVE-2018-10933.txt

Bugfix Release by libSSH : https://www.libssh.org/2018/10/16/libssh-0-8-4-and-0-7-6-security-and-bugfix-release/

## Create a vulnerable ssh server:

Download, uncompress and build the vulnerable libSSH Version : https://www.libssh.org/files/0.7/libssh-0.7.4.tar.xz

And then run libSSH on your own server.

## libSSH authentication bypass with tool that i wrote
# If you have got any fake ssh keys use the second bypasswithfakekey.py

#libsshauthbypass.py
```
pip install paramiko==2.0.8
If 2.0.8 doesn't works try : pip install paramiko==2.4.2

pip install socket

python libsshauthbypass.py
```
#libsshauthbypass.py
```
pip install paramiko==2.0.8
If 2.0.8 doesn't works try : pip install paramiko==2.4.2

pip install socket

python bypasswithkey.py
```



## Shodan.io libSSH

![](https://i.imgur.com/SWEfcGR.png)
