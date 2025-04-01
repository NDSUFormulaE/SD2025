Class CCCVCharger:
	def     __init__(self, charge_voltage, charging_current, termination_current):
		self.charge_voltage = charge_voltage
		self.charging_current = charging_current
		self.termination_current = termination_current
		self.voltage = 0
		self.current = 0
		self.is_charging = False
		
	def    charge(self)
	          self.is_charging = True
	          print ("charging started")
	
	          while self.is_charging:
	
		          if self.voltage < self.charge_voltage:
		              print (f"CC Mode: Voltage = {self.voltage:.2f}V, Current = {self.charging_current:.2f}A")
			   self.current += 0.1
			   self.current = self.charging_current
			
			else:
			   print (f"CV Mode: Voltage = {self.voltage:.2f}V, Current = {self.charging_current:.2f}A")
			   self.current -= 0.05
			
			If self.current <=self.termination_current:
			   self.stop_charging()
			
	Def get_voltage(self):
	       return self.voltage
	
	Def get_current(self):
	       return self.current
	
	Def stop_charging(self):
	       self.is_charging = False
	       print("Charging Complete")
	
	charger = CCCVCharger (charge_voltage=58.8, charging_current=16.0, termination_current=0.2)
	charger.charge()
	
	print(f"Final Voltage: {charger.get_voltage():.2f}V")
	print(f"Final Current: {charger.get_current():.2f}A")