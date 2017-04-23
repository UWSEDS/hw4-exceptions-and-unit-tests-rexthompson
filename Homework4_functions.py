# DATA 515 - Spring 2017
# Homework 4
# Rex Thompson
# 4/23/17

##### FUNCTIONS #####

import os
import requests

def get_data(url):
    '''
    Downloads the data if it is not present locally.
    Takes no action if the data are already present.
    Throws an exception if the URL does not exist.
    
    arguments
    ---------
    url : url of website to download
    
    Note: filename following the last '/' in the given url will be checked against the working directory.
    
    '''
    
    filename = os.path.basename(url)  # extract filename from url
    if os.path.exists(filename):      # check if file exists in working directory
        status = 'file already exists' # for unit test
        print('A file named \'' + filename + '\' already exists in your working directory.')
    else:
        # try to download the data
        print('Attempting to download \'' + url + '\'')
        req = requests.get(url)
        # print('status code = ' + str(req.status_code))
        if req.status_code == 404:
            raise Exception("'{0}' not found.".format(url))
        else:
            assert req.status_code == 200 # if the download failed, this line will generate an error
            status = 'URL found' # for unit test
            print('File successfully downloaded')
        with open(filename, 'wb') as f:
            f.write(req.content)
    return status


def delete_data(url):
    '''
    Removes the data if it is present locally.

    arguments
    ---------
    url : url of website to download
    
    Note: filename following the last '/' in the given url will be checked against the working directory.
    
    '''
    
    filename = os.path.basename(url)  # define filename from url
    if os.path.exists(filename):  # check if file exists in working directory
        print('Deleting \'' + filename + '\'')
        os.remove(filename)
        status = 'deleted existing file' # for unit test
    else:
        print('File not found. Nothing deleted.')
        status = 'file does not exist' # for unit test
    return status
