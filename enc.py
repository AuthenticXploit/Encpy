#!/usr/bin/env python2
# encoding: utf-8
"""
enc.py

Created by AuthenticXploit on 23/06/2021.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""

import base64
import zlib
import marshal
from sys import exit
from os import system
from time import sleep

def quit():
    print("\033[36;1m[\033[33;1m!\033[36;1m] \033[31;1mExit\x1b[0m")
    exit()

system('clear')
print """\033[91m
      _____ _   _  ____ ______   __
     | ____| \ | |/ ___|  _ \ \ / /\033[33;1m
     |  _| |  \| | |   | |_) \ V /\033[32;1m
     | |___| |\  | |___|  __/ | |\033[36;1m
     |_____|_| \_|\____|_|    |_|\033[1;97m
     
     \x1b[1;97m Author   \033[31;1m:  \033[32mAuthenticXploit
     \x1b[1;97m Type     \033[31;1m:  \033[32mEncrypt python
     \x1b[1;97m Version  \033[31;1m:  \033[32m0.1
     \x1b[1;97m Contact  \033[31;1m:  \033[32mhttps://t.me/AuthenticXploit_bot
     \x1b[1;97m
 \033[31;1m[\033[37;1m01\033[31;1m]\033[1;93m Encrypt Base16
 \033[31;1m[\033[37;1m02\033[31;1m]\033[1;93m Encrypt Base32
 \033[31;1m[\033[37;1m03\033[31;1m]\033[1;93m Encrypt Base64
 \033[31;1m[\033[37;1m04\033[31;1m]\033[1;93m Encrypt Marshal
 \033[31;1m[\033[37;1m05\033[31;1m]\033[1;93m Encrypt Zlib,Base16
 \033[31;1m[\033[37;1m06\033[31;1m]\033[1;93m Encrypt Zlib,Base32
 \033[31;1m[\033[37;1m07\033[31;1m]\033[1;93m Encrypt Zlib,Base64
 \033[31;1m[\033[37;1m08\033[31;1m]\033[1;93m Encrypt Marshal,Zlib,Base16
 \033[31;1m[\033[37;1m09\033[31;1m]\033[1;93m Encrypt Marshal,Zlib,Base32
 \033[31;1m[\033[37;1m10\033[31;1m]\033[1;93m Encrypt Marshal,Zlib,Base64
 \033[31;1m[\033[37;1m00\033[31;1m]\033[1;93m Exit
 """

def main():   
    choice = raw_input('\x1b[1;37m\x1b[31m\n[\x1b[33m+\x1b[1;37m\x1b[31m]\x1b[34m Choose \x1b[31m: \x1b[0m')
    if choice == '1' or choice == '01':
        try:
            file = raw_input('\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mFile\x1b[31m: \x1b[0m')
            fileopen = open(file).read()
            a = base64.b16encode(fileopen)
            b = "#Encrypt by AuthenticXploit\n#Github : https://github.com/AuthenticXploit\nimport base64\nexec(base64.b16decode('" + a + "'))"
            c = file.replace('.py', '_crypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print '\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mOUTPUT\x1b[31m:\x1b[0m', c
            main()
        except:
            print '\x1b[1;37m\x1b[31m[\x1b[33m!\x1b[1;37m\x1b[31m] \x1b[31mFile not found!'
            quit()

    elif choice == '2' or choice == '02':
        try:
            file = raw_input('\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mFile\x1b[31m: \x1b[0m')
            fileopen = open(file).read()
            a = base64.b32encode(fileopen)
            b = "#Encrypt by AuthenticXploit\n#Github : https://github.com/AuthenticXploit\nimport base64\nexec(base64.b32decode('" + a + "'))"
            c = file.replace('.py', '_crypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print '\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mOUTPUT\x1b[31m:\x1b[0m', c
            main()
        except:
            print '\x1b[1;37m\x1b[31m[\x1b[33m!\x1b[1;37m\x1b[31m] \x1b[31mFile not found!'
            quit()

    elif choice == '3' or choice == '03':
        try:
            file = raw_input('\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mFile\x1b[31m: \x1b[0m')
            fileopen = open(file).read()
            a = base64.b64encode(fileopen)
            b = "#Encrypt by AuthenticXploit\n#Github : https://github.com/AuthenticXploit\nimport base64\nexec(base64.b64decode('" + a + "'))"
            c = file.replace('.py', '_crypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print '\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mOUTPUT\x1b[31m:\x1b[0m', c
            main()
        except:
            print '\x1b[1;37m\x1b[31m[\x1b[33m!\x1b[1;37m\x1b[31m] \x1b[31mFile not found!'
            quit()

    elif choice == '4' or choice == '04':
        try:
            file = raw_input('\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mFile\x1b[31m: \x1b[0m')
            fileopen = open(file).read()
            a = compile(fileopen, 'dg', 'exec')
            m = marshal.dumps(a)
            s = repr(m)
            b = '#Encrypt by AuthenticXploit\n#Github : https://github.com/AuthenticXploit\nimport marshal\nexec(marshal.loads(' + s + '))'
            c = file.replace('.py', '_crypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print '\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mOUTPUT\x1b[31m:\x1b[0m', c
            main()
        except:
            print '\x1b[1;37m\x1b[31m[\x1b[33m!\x1b[1;37m\x1b[31m] \x1b[31mFile not found!'
            quit()

    elif choice == '5' or choice == '05':
        try:
            file = raw_input('\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mFile\x1b[31m: \x1b[0m')
            fileopen = open(file).read()
            c = zlib.compress(fileopen)
            d = base64.b16encode(c)
            e = '#Encrypt by AuthenticXploit\n#Github : https://github.com/AuthenticXploit\nimport marshal,zlib,base64\nexec(zlib.decompress(base64.b16decode("' + d + '")))'
            f = file.replace('.py', '_crypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print '\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mOUTPUT\x1b[31m:\x1b[0m', f
            main()
        except:
            print '\x1b[1;37m\x1b[31m[\x1b[33m!\x1b[1;37m\x1b[31m] \x1b[31mFile not found!'
            quit()

    elif choice == '6' or choice == '06':
        try:
            file = raw_input('\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mFile\x1b[31m: \x1b[0m')
            fileopen = open(file).read()
            c = zlib.compress(fileopen)
            d = base64.b32encode(c)
            e = '#Encrypt by AuthenticXploit\n#Github : https://github.com/AuthenticXploit\nimport marshal,zlib,base64\nexec(zlib.decompress(base64.b32decode("' + d + '")))'
            f = file.replace('.py', '_crypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print '\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mOUTPUT\x1b[31m:\x1b[0m', f
            main()
        except:
            print '\x1b[1;37m\x1b[31m[\x1b[33m!\x1b[1;37m\x1b[31m] \x1b[31mFile not found!'
            quit()

    elif choice == '7' or choice == '07':
        try:
            file = raw_input('\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mFile\x1b[31m: \x1b[0m')
            fileopen = open(file).read()
            c = zlib.compress(fileopen)
            d = base64.b64encode(c)
            e = '#Encrypt by AuthenticXploit\n#Github : https://github.com/AuthenticXploit\nimport marshal,zlib,base64\nexec(zlib.decompress(base64.b64decode("' + d + '")))'
            f = file.replace('.py', '_crypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print '\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mOUTPUT\x1b[31m:\x1b[0m', f
            main()
        except:
            print '\x1b[1;37m\x1b[31m[\x1b[33m!\x1b[1;37m\x1b[31m] \x1b[31mFile not found!'
            quit()

    elif choice == '8' or choice == '08':
        try:
            file = raw_input('\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mFile\x1b[31m: \x1b[0m')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b16encode(c)
            e = '#Encrypt by AuthenticXploit\n#Github : https://github.com/AuthenticXploit\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("' + str(d) + '"))))'
            f = file.replace('.py', '_crypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print '\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mOUTPUT\x1b[31m:\x1b[0m', f
            main()
        except:
            print '\x1b[1;37m\x1b[31m[\x1b[33m!\x1b[1;37m\x1b[31m] \x1b[31mFile not found!'
            quit()

    elif choice == '9' or choice == '09':
        try:
            file = raw_input('\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mFile\x1b[31m: \x1b[0m')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b32encode(c)
            e = '#Encrypt by AuthenticXploit\n#Github : https://github.com/AuthenticXploit\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("' + str(d) + '"))))'
            f = file.replace('.py', '_crypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print '\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mOUTPUT\x1b[31m:\x1b[0m', f
            main()
        except:
            print '\x1b[1;37m\x1b[31m[\x1b[33m!\x1b[1;37m\x1b[31m] \x1b[31mFile not found!'
            quit()

    elif choice == '10' or choice == '10':
        try:
            file = raw_input('\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mFile\x1b[31m: \x1b[0m')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b64encode(c)
            e = '#Encrypt by AuthenticXploit\n#Github : https://github.com/AuthenticXploit\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + str(d) + '"))))'
            f = file.replace('.py', '_crypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print '\x1b[1;37m\x1b[31m[\x1b[33m*\x1b[1;37m\x1b[31m] \x1b[0mOUTPUT\x1b[31m:\x1b[0m', f
            main()
        except:
            print '\x1b[1;37m\x1b[31m[\x1b[33m!\x1b[1;37m\x1b[31m] \x1b[31mFile not found!'
            quit()

    elif choice == '0' or choice == '00':
        system('clear')
        print('\x1b[34m[\x1b[33m*\x1b[34m] \x1b[1;37m\x1b[31mExit')
        sleep(2)
        exit('\x1b[33mSee you again ;)\x1b[33m')
        
    else:
        print '\x1b[31m\n[\x1b[33m-\x1b[31m] \x1b[33mWrong input..!!'
        sleep(1)
        main()


if __name__ == '__main__':
    try:
        main()
    except(KeyboardInterrupt, EOFError):
        print("\033[36;1m\n[\033[31;1m!\033[36;1m]\033[33;1mDetects a forced stop program \x1b[0m")
        exit(0)
