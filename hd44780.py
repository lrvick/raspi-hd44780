#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       gpio_play6.py
# Texy 2012

import RPi.GPIO as GPIO
import time

def main():

    GPIO.setmode(GPIO.BCM) # use BCM I/O names
    GPIO.setup(24, GPIO.OUT) # E
    GPIO.setup(4, GPIO.OUT) # RS
    GPIO.setup(18, GPIO.OUT) # DB4
    GPIO.setup(21, GPIO.OUT) # DB5
    GPIO.setup(22, GPIO.OUT) # DB6
    GPIO.setup(23, GPIO.OUT) # DB7
    GPIO.setup(17, GPIO.OUT) # LED
    lcd_cmd(0x33) # $33 8-bit mode   
    lcd_cmd(0x32) # $32 8-bit mode   
    lcd_cmd(0x28) # $28 8-bit mode   
    lcd_cmd(0x0C) # $0C 8-bit mode   
    lcd_cmd(0x06) # $06 8-bit mode   
    lcd_cmd(0x01) # $01 8-bit mode   
    lcd_string("Hello Pi")
    lcd_cmd(0xC0) # next line
    lcd_string("Forum peeps!")


def lcd_cmd(bits):
   bits=bin(bits)
   bits=bits[2:]
   zeros=(8-len(bits))*"0"
   bits=zeros+bits
   GPIO.output(4, False) # RS low
   GPIO.output(18, False)
   GPIO.output(21, False)
   GPIO.output(22, False)
   GPIO.output(23, False)
   if bits[0]=="1" :
      GPIO.output(23, True)
   if bits[1]=="1" :
      GPIO.output(22, True)
   if bits[2]=="1" :
      GPIO.output(21, True)
   if bits[3]=="1" :
      GPIO.output(18, True)
   time.sleep(0.01)
   GPIO.output(24, True) # E high
   time.sleep(0.01)
   GPIO.output(24, False) # E low
   time.sleep(0.01)
   GPIO.output(18, False)
   GPIO.output(21, False)
   GPIO.output(22, False)
   GPIO.output(23, False)
   if bits[4]=="1" :
      GPIO.output(23, True)
   if bits[5]=="1" :
      GPIO.output(22, True)
   if bits[6]=="1" :
      GPIO.output(21, True)
   if bits[7]=="1" :
      GPIO.output(18, True)
   time.sleep(0.01)
   GPIO.output(24, True) # E high
   time.sleep(0.01)
   GPIO.output(24, False) # E low
   time.sleep(0.01)

def lcd_string(message):
   msg_len = len(message)
   for i in range(msg_len):
      lcd_char(message[i])
      
      
      


def lcd_char(bits):
   bits=bin(ord(bits))
   bits=bits[2:]
   zeros=(8-len(bits))*"0"
   bits=zeros+bits
   GPIO.output(4, True) # RS high
   GPIO.output(18, False)
   GPIO.output(21, False)
   GPIO.output(22, False)
   GPIO.output(23, False)
   if bits[0]=="1" :
      GPIO.output(23, True)
   if bits[1]=="1" :
      GPIO.output(22, True)
   if bits[2]=="1" :
      GPIO.output(21, True)
   if bits[3]=="1" :
      GPIO.output(18, True)
   time.sleep(0.01)
   GPIO.output(24, True) # E high
   time.sleep(0.01)
   GPIO.output(24, False) # E low
   time.sleep(0.01)
   GPIO.output(18, False)
   GPIO.output(21, False)
   GPIO.output(22, False)
   GPIO.output(23, False)
   if bits[4]=="1" :
      GPIO.output(23, True)
   if bits[5]=="1" :
      GPIO.output(22, True)
   if bits[6]=="1" :
      GPIO.output(21, True)
   if bits[7]=="1" :
      GPIO.output(18, True)
   time.sleep(0.01)
   GPIO.output(24, True) # E high
   time.sleep(0.01)
   GPIO.output(24, False) # E low
   time.sleep(0.01)

if __name__ == '__main__':
   main()
