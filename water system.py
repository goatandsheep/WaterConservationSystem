#[Floor][Room][Number]

boolean go = true

class Shower:
	def __init__(self, floor, room, number):
		self.floor = floor
		self.room = room
		self.number = number
		self.occupied = false
	
	def get_floor(self):
		return self.floor
	def get_room(self):
		return self.room
	def get_number(self):
		return self.number
	def get_occupied(self):
		return self.occupied


class Sink:
	
	def __init__(self, floor, room, number):
		self.floor = floor
		self.room = room
		self.number = number
		self.occupied = false
	
	def get_floor(self):
		return self.floor
	def get_room(self):
		return self.room
	def get_number(self):
		return self.number
	def get_occupied(self):
		return self.occupied
	

class Toilet:
	
	def __init__(self, floor, room, number):
		self.floor = floor
		self.room = room
		self.number = number
		self.occupied = false
		self.tankFull = false
	
	def get_floor(self):
		return self.floor
	def get_room(self):
		return self.room
	def get_number(self):
		return self.number
	def get_occupied(self):
		return self.occupied
	def get_tankFull(self):
		return self.tankFull
	
	def fillTank():
		#Where to get water from?
		self.tankFull = True
	
	def flush():
		if ((get_tankFull())!):
			fillTank()
		
		self.tankFull = False #i.e. fill, then empty
	
	def doorOpen():
		if((get_occupied())!):
			self.occupied = true
			if ((get_tankFull)!):
				fillTank()
		else:
			self.occupied = false	#leave washroom