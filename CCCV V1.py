from machine import Pin, ADC
import time

VOLTAGE_SCALE = ?
CURRENT_SCALE = ?

class CCCVCharger:
    def __init__(self, charge_voltage, charging_current, termination_current):
        self.charge_voltage = charge_voltage
        self.charging_current = charging_current
        self.termination_current = termination_current

        self.voltage = 0.0
        self.current = 0.0
        self.is_charging = False

        self.voltage_sensor = ADC(26)  # GP26 = ADC0
        self.current_sensor = ADC(27)  # GP27 = ADC1

        self.fault_gate_driver = Pin(0, Pin.IN)
        self.fault_current_sensor = Pin(13, Pin.IN)
        self.output_control = Pin(1, Pin.OUT)

        self.cc_mode_led = Pin(14, Pin.OUT)
        self.cv_mode_led = Pin(15, Pin.OUT)

    def read_voltage(self):
        adc_val = self.voltage_sensor.read_u16()
        voltage = (adc_val / 65535.0) * 3.3 * VOLTAGE_SCALE
        self.voltage = voltage
        return voltage

    def read_current(self):
        adc_val = self.current_sensor.read_u16()
        current = (adc_val / 65535.0) * 3.3 * CURRENT_SCALE
        self.current = current
        return current

    def start_charging(self):
        if self.fault_gate_driver.value() == 1:
            print("Gate driver fault detected! Abortion.")
            return
        if self.fault_current_sensor.value() == 1:
            print("Current sensor fault detected! Abortion.")
            return

        self.is_charging = True
        self.output_control.value(1)
        print("Charging started.")

        while self.is_charging:
            voltage = self.read_voltage()
            current = self.read_current()

            if voltage < self.charge_voltage:
                self.cc_mode_led.value(1)
                self.cv_mode_led.value(0)
                print(f"CC Mode: Voltage = {voltage:.2f}V, Current = {current:.2f}A")
            else:
                self.cc_mode_led.value(0)
                self.cv_mode_led.value(1)
                print(f"CV Mode: Voltage = {voltage:.2f}V, Current = {current:.2f}A")

            if current <= self.termination_current:
                self.stop_charging()
                break

            if self.fault_gate_driver.value() == 1 or self.fault_current_sensor.value() == 1:
                print("Fault occurred during charging! Stop.")
                self.stop_charging()
                break

            time.sleep(1)

    def stop_charging(self):
        self.is_charging = False
        self.output_control.value(0)
        self.cc_mode_led.value(0)
        self.cv_mode_led.value(0)
        print("Charging complete or interrupted.")

    def get_voltage(self):
        return self.voltage

    def get_current(self):
        return self.current

charger = CCCVCharger(charge_voltage=58.8, charging_current=16.0, termination_current=0.2)
charger.start_charging()

print(f"Final Voltage: {charger.get_voltage():.2f}V")
print(f"Final Current: {charger.get_current():.2f}A")

	
	charger = CCCVCharger (charge_voltage=58.8, charging_current=16.0, termination_current=0.2)
	charger.charge()
	
	print(f"Final Voltage: {charger.get_voltage():.2f}V")
	print(f"Final Current: {charger.get_current():.2f}A")
