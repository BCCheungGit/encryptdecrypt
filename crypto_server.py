from crypto import encrypt, decrypt
from time import sleep
import os,sys,time,datetime,getopt,csv

from flask import Flask, request


app = Flask(__name__)

def get_key(message):
    return encrypt(message)

def timeNow():
    return str(datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S") + "======== ")


@app.route('/encrypt')
def encrypt():
    message = request.args.get('message')
    encrypted_msg, encryption_key = get_key(message)
    return '<div><p>Encrypted Message is : {} and key is  {} </p></div>'.format(encrypted_msg,encryption_key)



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
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)



