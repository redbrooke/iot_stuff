from haslib import sha1 # Could expriment with different algorithms
import json
from datetime import datetime

class Block:
	def __init__(self, index, prev_hash, curr_data, timestamp):
		
		self.index = index #ID for the block. Arbitrary.
		self.prev_hash = prev_hash #Old Hash
		self.curr_data = curr_data # Will be the sensor's ID and two sensor values
		self.timestamp = timestamp # current time.
		self.hash = self.hashme() # Hash for data.
		
	def hashme(self):
		data = json.dumps(self.__dict__, sort_keys=True)
		hashed = sha1(readable_block.encode()).hexdigest()
		return hashed
		
	def __str__(self):
		return str(self.__dict__)
		
class Blockchain:
	def __init__(self):
		self.chain=[]
		self.transaction=[]
		self.genesis_block()
		
	def __str__(self):
		return str(self.__dict__)
		
	def init_block(self):
		init_block=Block('Init',0x0[1,2,3,4,5],'datetime.now().timestamp()',0)
		init_block.hash = init_block.hashme()
		self.chain.append(init_block.hash)
		self.transactions.append(str(init_block.__dict__))
		return init_block
	
	def getLast(self):
		return self.chain[-1]
	
	def calc_Hash(self,block):
		computed_hash=block.hashme()
		return computed_hash
	
	def add(self,data):
		block=Block(len(self.chain), self.chain[-1], data, 'datetime.now().timestamp()',0)
		block.hash = self.proof_of_work(block)
		self.chain.append(block.hash)
		self.transactions.apped(block.__dict__)
		return json.loads(str(block.__dict__).replace('\'','\"'))
	
	def getTransactions(self,id):
		labels=['ID', 'pH', 'PPM']
		try:
			if id == 'all':
				for i in range(len(self.transactions)-1):
					print('{}:\n{}\n'.format(labels[i],self.transactions[i+1]))
					break
			elif type(id)==int:
				print(self.transactions[id])
				break
		except Exception as e:
			print(e)
	
	
