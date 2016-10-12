class Car():
	def __init__(self, car_name, model, doors):
		self.car_name = car_name
		self.model = model
		self.doors = doors
	def fullname(self):
		return '{} {} {}'.format(self.car_name, self.model, self.doors)
	def carname(self):
		return self.car_name
	def model(self):
		return self.model

Toyota= Car('Toyota', 'corolla', '4 door')
WRX= Car('Subaru', 'Impreza', '5 door')

print(Toyota.fullname())
print(WRX.fullname())

