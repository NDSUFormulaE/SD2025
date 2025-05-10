from machine import ADC
from time import sleep_ms
    
def ADCTOV(VADC):
    """Calculates the relative Voltage from the ADC"""
    k = 5/ 4095
    ADCVoltage = VADC * k
    return ADCVoltage

def VDIVADC(VinputADC):
    """Calcuateds the real Voltage at the Voltage div"""
    realVoltage = (VinputADC * 21100)/1000
    return realVoltage 

def CurrentSensorADC(CinputVolts):
    """Calcuateds the real Current from the hall effect Current Sensor"""
    realCurrent = (CinputVolts - 2.5) / 0.055
    return realCurrent