#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import hmac
import socket
from hashlib import sha1
from time import sleep,time
from Crypto.Cipher import AES
from base64 import standard_b64decode
from struct import pack, unpack


class SecureClient:

    def __init__(self):
        self.msg_end = '</msg>'
        self.msg_wrong_pin = 'BAD_PIN'
        self.aes_key = 'aes.key'

        self.host = 'crypto-04.v7frkwrfyhsjtbpfcppnu.ctfz.one'
        self.port = 7331
        self.buff_size = 1024

        try:
            self.greeting()
        except KeyboardInterrupt:
            exit(0)
    def totp_gen(self,ttime):
        secret = "0b25610980900cffe65bfa11c41512e28b0c96881a939a2d"
        counter = pack('>Q', ttime // 30)
        totp_hmac = hmac.new(secret.encode('UTF-8'), counter, sha1).digest()
        offset = totp_hmac[19] & 15
        totp_pin = str((unpack('>I', totp_hmac[offset:offset + 4])[0] & 0x7fffffff) % 1000000)
        return totp_pin.zfill(6)

    def greeting(self):
        self.cls()

        #print('\n   ==================================== !!! CONFIDENTIALITY NOTICE !!! ====================================')
        #print('   ||                 You trying to access high confidential Federation workflow system.                 ||')
        #print('   ||                 If you are not authorised to use this system leave it immediately.                 ||')
        #print('   || Otherwise incident will be reported and you will be eliminated as it considered by Federation Law. ||')
        #print('   ========================================================================================================\n')
        print('   Last login time: {0}'.format(self.get_last_login()))
        self.main_menu()
    def extractblock(self,C,N):
        blockb64 = standard_b64decode(C).hex()
        return blockb64[32*(N-1):32*N]
        

    def brute(self):
      candidate="0123456789abcdefghijklmnopqrstuvwxyz"
      totp = "0b" # len : 48
      for i in range(48):
        print("##### {}/48 ####".format(i+1))
        if i < len(totp):
          print("Find "+totp[i])
          continue
        query = ".."+"/"*(64-i)+"totp.secret"
        C = self.send('file '+query)
        original = self.extractblock(C,5)
        print("original ", original)
        for ch in candidate:
          myQuery = query+": "+totp+ch
          CC = self.send('file '+myQuery)
          chkblock = self.extractblock(CC,5)
          if original == chkblock:
            totp +=ch
            print("Find {}".format(ch))
            break
      print("Recover done ",totp)

    def main_menu(self):
       # self.brute()
        while True:
            print(self.totp_gen(int(input('check totp > '))))
            print("\n   You are authorised to:")
            print("      list - view list of available files")
            print("      file - request file from server")
            print("      admin - use administrative functions")
            print("      exit - exit workflow system")

            user_choice = input('\n   What do you want to do? (list/file/admin/exit) > ')

            self.cls()
          
            if user_choice.lower() == 'list':
                self.list_files()
            elif user_choice.lower() == 'file':
                self.view_file()
            elif user_choice.lower() == 'admin':
                self.admin()
            elif user_choice.lower() == 'exit':
                exit(0)
            else:
                print('\n   Unrecognized command, try again')
          
    def list_files(self):
        file_list = self.get_file_list()

        print('\n   You are authorised to view listed files:\n')
        for file in file_list:
            print('   - {0}'.format(file))

    def view_file(self):
        #self.list_files()
        filename = input('Which file you want to view? > ')
        file_content = self.send('file {0}'.format(filename))
        print(file_content)
        fileinhex = standard_b64decode(file_content).hex()
        for i in range(0,len(fileinhex),32):
          print(fileinhex[i:i+32])
        if len(file_content) > 0:
            plain_content = self.decrypt(file_content)
            if len(plain_content) > 0:
                print('========================================================================================================')
                print('Content of {0}'.format(plain_content))
                print('========================================================================================================')
            else:
                print('Seems like you have no decryption key, so you can\'t see any files.')
        else:
            print('Error while requesting file')

    def admin(self):
        print('\n   Access to administrative functions requires additional security check.')
        pin = input('   Enter your administrative PIN > ')
        response = self.send('admin {0}'.format(pin))

        if response == self.msg_wrong_pin:
            print('\n   Wrong administrative PIN. Incident will be reported.')
        else:
            print('\n   High confidential administrative data: {0}'.format(response))

    def decrypt(self, data):
        try:
            key = open(self.aes_key).read()
            cipher = AES.new(key, AES.MODE_ECB)

            plain = cipher.decrypt(standard_b64decode(data)).decode('UTF-8')
            plain = plain[:-ord(plain[-1])]
            return plain

        except Exception as ex:
            return ''

    def get_last_login(self):
        return self.send('login')

    def get_file_list(self):
        files = self.send('list')

        if len(files) > 0:
            return files.split(',')
        else:
            return ['no files available']

    def send(self, data):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, self.port))
            sock.send('{0}{1}'.format(data, self.msg_end).encode('UTF-8'))
            response = self.recv_until(sock, self.msg_end)
            sock.close()
            return response

        except Exception as ex:
            return ''

    def recv_until(self, sock, end):
        try:
            recv = sock.recv(self.buff_size).decode('utf-8')
            while recv.find(end) == -1:
                recv += sock.recv(self.buff_size).decode('utf-8')
            return recv[:recv.find(end)]

        except Exception as ex:
            return ''

    def cls(self):
        pass


if __name__ == '__main__':
    secure_client = SecureClient()
