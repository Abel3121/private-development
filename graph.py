import datetime

class lis:
	
	def __init__(self):
		now = 0
		future = 0

	def output(self):
		now = datetime.datetime.now().replace(microsecond=0)
		return now

print(lis().output())