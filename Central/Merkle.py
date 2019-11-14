# 0. Import the needed library
import Crypto.Hash.SHA256 as SHA256
from collections import OrderedDict

class Merkle:

	# 2. Initiate the class object
	def __init__(self,listoftransaction=None):
		self.listoftransaction = listoftransaction
		self.past_transaction = OrderedDict()

	# 3. Create the Merkle Tree  
	def create_tree(self):

		# 3.0 Continue on the declaration
		listoftransaction = self.listoftransaction
		past_transaction = self.past_transaction
		temp_transaction = []

		# 3.1 Loop until the list finishes
		for index in range(0,len(listoftransaction),2):

			# 3.2 Get the most left element 
			current = listoftransaction[index]

			# 3.3 If there is still index left get the right of the left most element
			if index+1 != len(listoftransaction):
				current_right = listoftransaction[index+1]

			# 3.4 If we reached the limit of the list then make a empty string
			else:
				current_right = ''

			# 3.5 Apply the Hash 256 function to the current values
			current_hash = SHA256.new(bytearray(current, 'ascii')).hexdigest()

			# 3.6 If the current right hash is not a '' <- empty string
			if current_right != '':
				current_right_hash = SHA256.new(bytearray(current_right, 'ascii')).hexdigest()

			# 3.7 Add the Transaction to the dictionary 
			past_transaction[listoftransaction[index]] = current_hash

			# 3.8 If the next right is not empty
			if current_right != '':
				past_transaction[listoftransaction[index+1]] = current_right_hash

			# 3.9 Create the new list of transaction
			if current_right != '':
				temp_transaction.append(current_hash + current_right_hash)

			# 3.01 If the left most is an empty string then only add the current value
			else:
				temp_transaction.append(current_hash)

		# 3.02 Update the variables and rerun the function again 
		if len(listoftransaction) != 1:
			self.listoftransaction = temp_transaction
			self.past_transaction = past_transaction

			# 3.03 Call the function repeatly again and again until we get the root 
			self.create_tree()

	# 4. Return the past Transaction 
	def Get_past_transacion(self):
		return self.past_transaction

	# 5. Get the root of the transaction
	def Get_Root_leaf(self):
		last_key = list(self.past_transaction.keys())[-1]
		return self.past_transaction[last_key]