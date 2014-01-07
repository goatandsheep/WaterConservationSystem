#[Floor][Room][Number]

go = true

#floors = 4				#randomly chose 4 as an example
#rooms[0:(floors-1)] = 1

def closest(floor, room, source):
	for i in range (floor:numFloors,0:floor):
		for j in range (room:numRooms[i],0:room):
			for k in range(0:numSource):
				if (source[i][j][k]):
					break
	return [i, j, k]

#polymorphism would be helpful here, so that you could have a Peripheral class with the inits
#then again, it won't improve performance; only simplicity of program and less typing
	
#class WaterFountain

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
	
	def waterOn():
		while ():	#water on):
			waterOn = true
			while(waterOn):
				[floor,room,number] = closest(floor, room)	#, Toilet)
				
			

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
		
	def senseHand():
		[floor,room,number] = closest(floor, room#, Toilet)
		
	

class Toilet:	#only thing not connected to clean water source
	
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
	
	def fillTank(floor,room,number):#shower/sink?
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