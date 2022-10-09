#import pygame
import datetime
import sys
import colours
#import main
import tkinter as tk
from gpio import LED


plat1GreenLED = LED(17)
plat1AmberLED = LED(27)
plat1RedLED = LED(22)

plat2GreenLED = LED(23)
plat2AmberLED = LED(24)
plat2RedLED = LED(25)

def plat1(state):
    if state == "onTime":
        plat1GreenLED.on()
        plat1AmberLED.off()
        plat1RedLED.off()

    elif state == "late":
        plat1GreenLED.off()
        plat1AmberLED.on()
        plat1RedLED.off()

    elif state == "vLate":
        plat1GreenLED.off()
        plat1AmberLED.off()
        plat1RedLED.on()

    elif state == "canceled":
        plat1GreenLED.off()
        plat1AmberLED.on()
        plat1RedLED.on()

def plat2(state):
    if state == "onTime":
        plat2GreenLED.on()
        plat2AmberLED.off()
        plat2RedLED.off()

    elif state == "late":
        plat2GreenLED.off()
        plat2AmberLED.on()
        plat2RedLED.off()

    elif state == "vLate":
        plat2GreenLED.off()
        plat2AmberLED.off()
        plat2RedLED.on()

    elif state == "canceled":
        plat2GreenLED.off()
        plat2AmberLED.on()
        plat2RedLED.on()


