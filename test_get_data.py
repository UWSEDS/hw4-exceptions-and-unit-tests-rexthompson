# DATA 515 - Spring 2017
# Homework 4
# Rex Thompson
# 4/23/17

##### UNIT TESTS - get_data.py #####

''' Unit tests for get_data.py '''

import unittest
import os
import uuid
import shutil
from Homework4_functions import get_data

class TestGetData(unittest.TestCase):

	# Test if a file is present locally
	def testPresentLocally(self):
		# SETUP
		expectedResult = 'file already exists'
		fakeFilename = str(uuid.uuid4()) + '.txt' # generate fake filename
		f = open(fakeFilename, 'wb') # create file with fake filename
		f.close()
		url = 'https://google.com/' + fakeFilename # append fake filename to fake url

		# RUN FUNCTION
		result = get_data(url)
		# import pdb; pdb.set_trace()
		
		# CLEANUP
		os.remove(fakeFilename) # remove fake file
		
		# ASSERTION
		self.assertEqual(result, expectedResult) # check for correct output


	# Test if a file is not present locally, and the URL points to a file that exists
	# NOTE: the url below MUST be a working address!!!
	def testURLExists(self):
		# SETUP
		expectedResult = 'URL found'
		url = 'https://data.seattle.gov/resource/4xy5-26gy.csv' # working URL
		wd = os.getcwd() # save current working directory
		fakeDir = str(uuid.uuid4()) # create path to new fake directory
		os.mkdir(fakeDir) # create new fake directory
		os.chdir(fakeDir) # go to new fake directory

		# RUN FUNCTION
		result = get_data(url) # run function
		# import pdb; pdb.set_trace()

		# CLEANUP
		os.chdir(wd) # step up one level in directory
		shutil.rmtree(fakeDir) # delete fake directory

		# ASSERTION
		self.assertEqual(result, expectedResult) # check for correct output


	# Test if the URL does not point to a file that exists
    # NOTE: the url below MUST be a NON-working address!!!
	def testURLDoesNotExist(self):
		# SETUP
		expectedResult = 'URL not found'
		url = 'https://data.seattle.gov/resource/4xy5-26gyFAKEFAKEFAKSE.csv' # non-working URL

		# RUN FUNCTION AND ASSERTION
		try:
			result = get_data(url)
		except:
			self.assertTrue(True) # only executed if function call returns exception
		else:
			self.assertTrue(False) # only execute if function call does not return exception

if __name__ == '__main__':
	unittest.main()
