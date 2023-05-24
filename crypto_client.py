from crypto import encrypt, decrypt
from time import sleep
import os,sys,time,datetime,getopt,csv

def get_key(message):
    return encrypt(message)

def timeNow():
    return str(datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S") + "======== ")

#print('Encrypted message is {}'.format(get_key('hello')[0]))
#print('\nKey is {}'.format(get_key('hello')[1]))

def main():
   print('============================================================')
   print('===== Crypto Client ========================================')
   print('===== Usage: ./crypto_client e:raw message here ============')
   print('=====        ./crypto_client d:encrypted message ===========')
   
   if len(sys.argv) == 1:
        print(timeNow() + 'Started')
        _Mesgin=input('\nEnter message for encryption:')
        encrypted_msg, encrypted_key = get_key(_Mesgin)
        print('Encrypted message for {} is {}'.format(_Mesgin, encrypted_msg))
        print('\nKey for {} is {}'.format(_Mesgin, encrypted_key))



#=============================================================================
if __name__ == "__main__":
    main()



