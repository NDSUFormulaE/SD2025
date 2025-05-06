def ADCTOV(VADC, V_ref):
    """Calculates the relative Voltage from the ADC"""
    ADCVoltage = (VADC * 4096) * V_ref
    return ADCVoltage

def VDIVADC(VinputADC):
    """Calcuateds the real Voltage at the Voltage div"""
    realVoltage = (VinputADC * 21100)/1000
    return realVoltage 

def ASensorADC(CinputADC):
    """Calcuateds the real Current from the hall effect Current Sensor"""
    realCurrent = (CinputADC - 2.5) / 0.055
    return realCurrent