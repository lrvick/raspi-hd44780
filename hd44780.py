#!/usr/bin/python

import RPi.GPIO as GPIO

PIN_RS = 24
PIN_E = 23
PIN_DB4 = 4
PIN_DB5 = 17
PIN_DB6 = 21
PIN_DB7 = 22

def main():

    GPIO.setmode(GPIO.BCM) # use BCM I/O names
    GPIO.setup(PIN_E, GPIO.OUT)
    GPIO.setup(PIN_RS, GPIO.OUT)
    GPIO.setup(PIN_DB4, GPIO.OUT)
    GPIO.setup(PIN_DB5, GPIO.OUT)
    GPIO.setup(PIN_DB6, GPIO.OUT)
    GPIO.setup(PIN_DB7, GPIO.OUT)
    lcd_cmd(0x33) # $33 8-bit mode
    lcd_cmd(0x32) # $32 8-bit mode
    lcd_cmd(0x28) # $28 8-bit mode
    lcd_cmd(0x0C) # $0C 8-bit mode
    lcd_cmd(0x06) # $06 8-bit mode
    lcd_cmd(0x01) # $01 8-bit mode
    lcd_string("I'm Raspberry Pi")
    lcd_cmd(0xC0) # next line
    lcd_string("  Take a byte!")


def lcd_cmd(bits):
   bits=bin(bits)
   bits=bits[2:]
   zeros=(8-len(bits))*"0"
   bits=zeros+bits
   GPIO.output(PIN_RS, False)
   GPIO.output(PIN_DB4, False)
   GPIO.output(PIN_DB5, False)
   GPIO.output(PIN_DB6, False)
   GPIO.output(PIN_DB7, False)
   if bits[0]=="1" :
      GPIO.output(PIN_DB7, True)
   if bits[1]=="1" :
      GPIO.output(PIN_DB6, True)
   if bits[2]=="1" :
      GPIO.output(PIN_DB5, True)
   if bits[3]=="1" :
      GPIO.output(PIN_DB4, True)
   GPIO.output(PIN_E, True)
   GPIO.output(PIN_E, False)
   GPIO.output(PIN_DB4, False)
   GPIO.output(PIN_DB5, False)
   GPIO.output(PIN_DB6, False)
   GPIO.output(PIN_DB7, False)
   if bits[4]=="1" :
      GPIO.output(PIN_DB7, True)
   if bits[5]=="1" :
      GPIO.output(PIN_DB6, True)
   if bits[6]=="1" :
      GPIO.output(PIN_DB5, True)
   if bits[7]=="1" :
      GPIO.output(PIN_DB4, True)
   GPIO.output(PIN_E, True)
   GPIO.output(PIN_E, False)

def lcd_string(message):
   msg_len = len(message)
   for i in range(msg_len):
      lcd_char(message[i])

def lcd_char(bits):
   bits=bin(ord(bits))
   bits=bits[2:]
   zeros=(8-len(bits))*"0"
   bits=zeros+bits
   GPIO.output(PIN_RS, True)
   GPIO.output(PIN_DB4, False)
   GPIO.output(PIN_DB5, False)
   GPIO.output(PIN_DB6, False)
   GPIO.output(PIN_DB7, False)
   if bits[0]=="1" :
      GPIO.output(PIN_DB7, True)
   if bits[1]=="1" :
      GPIO.output(PIN_DB6, True)
   if bits[2]=="1" :
      GPIO.output(PIN_DB5, True)
   if bits[3]=="1" :
      GPIO.output(PIN_DB4, True)
   GPIO.output(PIN_E, True)
   GPIO.output(PIN_E, False)
   GPIO.output(PIN_DB4, False)
   GPIO.output(PIN_DB5, False)
   GPIO.output(PIN_DB6, False)
   GPIO.output(PIN_DB7, False)
   if bits[4]=="1" :
      GPIO.output(PIN_DB7, True)
   if bits[5]=="1" :
      GPIO.output(PIN_DB6, True)
   if bits[6]=="1" :
      GPIO.output(PIN_DB5, True)
   if bits[7]=="1" :
      GPIO.output(PIN_DB4, True)
   GPIO.output(PIN_E, True)
   GPIO.output(PIN_E, False)

if __name__ == '__main__':
   main()
