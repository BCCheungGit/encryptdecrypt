from flask import Blueprint, render_template, flash, request, redirect, url_for, Flask
from cryptography.fernet import Fernet
from time import sleep
import os,sys,time,datetime,getopt,csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfasdfasdf'

def encrypt1(plain_text):
    key = Fernet.generate_key() #this is your "password"
    cipher_suite = Fernet(key)
    encrypted = cipher_suite.encrypt(str.encode(plain_text))
    return encrypted, key

def decrypt1(encoded_text, key):
    cipher_suite = Fernet(key)
    decrypted = cipher_suite.decrypt(encoded_text)
    return decrypted


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        input = request.form.get('message')
        print(request.form.get('message'))
        print("Message to be encrypted:", input)
        encrypted_msg, encryption_key = encrypt1(input)

        return render_template('index.html', outmessage=encrypted_msg.decode('utf-8'), outkey=encryption_key.decode('utf-8'))
    return render_template('index.html')



@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        encoded = request.form.get('encoded')
        key = request.form.get('key')
        decrypted_message = decrypt1(encoded, key).decode('utf-8')
        return render_template('index.html', original=decrypted_message) 
    
    return render_template('index.html', original=decrypted_message)






if __name__ == '__main__':
    app.run(debug=True)