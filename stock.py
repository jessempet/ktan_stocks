import ystockquote
import csv

class SP():
	"""
	Creates an S&P500 object that contains a dictionary of all SP500 stock companies
	"""
	def __init__(self,symbol = "None"):
	#Initialize file to be pointed to 
		self.spFile = 'C:\Users\jmpet\Desktop\sp500.csv'
		#self.spFile = PATH_TO_CSV
		
		self.spDict = {}
		#open CSV and parse it in to a readable dictionary 
		with open(self.spFile, mode='r') as infile:
			reader = csv.reader(infile)
			self.spDict = {rows[0]:rows[1] for rows in reader}
	
	#syntax sp = SP() --> print sp["SYMBOL"] --> "Name corresponding to symbol"
	def __getitem__(self,key):
		return self.spDict[key]
	
	#syntax sp = SP() --> symbol in sp --> True or False
	def __contains__(self, symbol):
		if str(symbol) in self.spDict:
			return True
	#Necessary to call object within another object 
	def __call__(self,symbol):
		return self.__getitem__(symbol)

class Stock():
	"""
	Creates and object for each stock 
	"""
	
	#Default constructor creating object attributes to be sent to yahoo finance api 
	def __init__(self, symbol, startDate=0, endDate=0):
		self.symbol = symbol
		self.startDate = startDate
		self.endDate = endDate
		#this line of code will populate historical stock data in to a parse-able dictionary
		self.dayDict = ystockquote.get_historical_prices(self.symbol, self.startDate, self.endDate)
		for key in self.dayDict:
			for currentDate in key:
				self.adj = self.dayDict[currentDate]['Adj Close']
				self.close = self.dayDict[currentDate]['Close']
				self.high = self.dayDict[currentDate]['High']
				self.low = self.dayDict[currentDate]['Low']
				self.open = self.dayDict[currentDate]['Open']
				self.volume = self.dayDict[currentDate]['Volume']
		#Instantiating an SP object to print out the name corresponding to the symbol
		self.sp500 = SP(self.symbol)
	
	#syntax stock = stock() --> print stock["date  in YYYY-MM-DD"] --> returns dictionary returned by 
	#ystockquote
	          
	def __str__(self):
		return "Adj Close: %s\nClose: %s\n High: %s\nLow: %s\nOpen: %s\nVolume: %s\n" % (self.adj, self.close, self.high, self.low, self.open, self.volume)  
		
		
def main():
	#debug
	sp500 = SP()
	symbol = raw_input("Enter in the symbol >>> ")
	startDate = raw_input("Enter the start date in YYYY-MM-DD format >>> ")
	endDate = raw_input ("Enter the end date in YYY-MM-DD format >>> ")
	stock = Stock(symbol, startDate, endDate)
	
if __name__ == '__main__':
	main()
