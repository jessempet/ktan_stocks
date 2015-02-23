import ystockquote
import csv
import datetime
import urllib2

class SP():
	"""
	Creates an S&P500 object that contains a dictionary of all SP500 stock companies
	"""
	def __init__(self,symbol = "None"):
	#Initialize file to be pointed to 
		
		self.spFile = '/home/jesse/Desktop/Python/ktan_stocks-master/sp500.csv'
		
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
	def __init__(self, symbol, startDate='', endDate=''):
		self.symbol = symbol
		self.startDate = startDate
		self.endDate = endDate
		#this line of code will populate historical stock data in to a parse-able dictionary
		
		#Instantiating an SP object to print out the name corresponding to the symbol
		self.sp500 = SP(self.symbol)
		
	def getData(self):
		info = ystockquote.get_historical_prices(self.symbol, self.startDate, self.endDate)
		return info
	#syntax stock = stock() --> print stock["date  in YYYY-MM-DD"] --> returns dictionary returned by 
	#ystockquote

	         
	def __str__(self):
		return "%s\t%s\t%s" % (self.symbol,self.startDate,self.endDate)
	
		
def main():
	#debug
	sp500 = SP()
	spFile = '/home/jesse/Desktop/Python/ktan_stocks-master/sp500.csv'

	with open(spFile, 'r') as f:
		reader = csv.reader(f)
		symbols = [rows[0] for rows in reader]

	startDate = raw_input("Enter the start date in YYYY-MM-DD format >>> ")
	endDate = raw_input ("Enter the end date in YYY-MM-DD format >>> ")
	print "writing to file..."
	a = datetime.datetime.now()
	with open('sp500_avgs.csv', 'wo') as f:
		writer = csv.writer(f)
		titles = ["Day", "Close","High", "Low","Open", "Volume", "Symbol"]
		writer.writerow(titles)
		for sym in symbols:
			try:
				
					
					stock = Stock(sym.upper(), startDate, endDate)
					data = stock.getData()
					days = [keys for keys in data.keys()]
					adj = [float(data.values()[i]['Adj Close']) for i in range(len(data))]
					close = [float(data.values()[i]['Close']) for i in range(len(data))]
					high = [float(data.values()[i]['High']) for i in range(len(data))]
					low = [float(data.values()[i]['Low']) for i in range(len(data))]
					op = [float(data.values()[i]['Open']) for i in range(len(data))]
					volume = [int(data.values()[i]['Volume']) for i in range(len(data))]
					
					
					syms = [sym for i in range(len(zip(days,close,high,low,op,volume)))]
					rows =  zip(days,close,high,low,op,volume, syms)
					for row in rows:
						writer.writerow(row)
			except urllib2.HTTPError, error:
				contents = error.read()

	b = datetime.datetime.now()

	print "Write complete! in %s" % (b-a)
	
if __name__ == '__main__':
	main()
