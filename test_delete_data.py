# DATA 515 - Spring 2017
# Homework 4
# Rex Thompson
# 4/23/17

##### UNIT TESTS - delete_data.py #####

''' Unit tests for delete_data.py '''

import unittest
import os
import uuid
import shutil
from Homework4_functions import delete_data

class TestDeleteData(unittest.TestCase):

	# Verify file deleted if it exists
	def testURLExists(self):
		# SETUP
		# expectedResult = 'deleted existing file'
		fakeFilename = str(uuid.uuid4()) + '.txt' # generate fake filename
		f = open(fakeFilename, 'wb') # create file with fake filename
		f.close()
		url = 'https://google.com/' + fakeFilename # append fake filename to fake url
		
		# RUN FUNCTION
		delete_data(url)
		# import pdb; pdb.set_trace()

		# ASSERTION
		self.assertFalse(os.path.exists(fakeFilename)) # check for correct output

	# Verify no action taken if file does not exist
	def testPresentLocally(self):
		# SETUP
		expectedResult = 'file does not exist'
		fakeFilename = str(uuid.uuid4()) + '.txt' # generate fake filename
		url = 'https://google.com/' + fakeFilename # append fake filename to fake url

		# RUN FUNCTION
		result = delete_data(url)
		# import pdb; pdb.set_trace()
		
		# ASSERTION
		self.assertEqual(result, expectedResult) # check for correct output

if __name__ == '__main__':
	unittest.main()
