import datetime

class lis:
	
	def __init__(self):
		now = datetime.datetime.now().replace(microsecond=0)
		print(now)

print(lis().__init__)