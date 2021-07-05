
###############################################################################
#                                                                             #  
# @author: Matilde Pato                                                       #  
# @email: matilde.pato@gmail.com                                              #
# @date: 31 Mar 2021                                                          #
# @version: 1.0                                                               #  
# Lasige - FCUL                                                               #
#  (Adapted from Márcia Barros, Pedro Ruas, Diana Sousa)                      #  
# @last update:                                                               #  
#   version 1.1:                                                              #      
#   (author:   )                                                              # 
#                                                                             #   
#                                                                             #  
###############################################################################

import os
import pandas as pd
import json
import unidecode

# --------------------------------------------------------------------------- #

def list_files_in_directory(path):
    '''
    Return a list containing the names of the entries in the 
        directory given by path
    :param path: path of the directory, which needs to be explored
    '''
    return os.listdir(path)
    # f = []
    # for (dirpath, dirnames, filenames) in os.walk(path_to_dir):
    #     f.extend(filenames)
    #     break
    # print(f)    
    #return f

# --------------------------------------------------------------------------- #

def open_json_file_pd(path, file):
    '''
    Convert a JSON string to pandas object, and return a dataframe
    :param path: path of the directory, which needs to be explored
           file: name of json file 
    '''
    return pd.read_json(path + file, orient = 'index')

# --------------------------------------------------------------------------- #

def validateJSON(jsonData):
    '''
    Method to validate it as per the standard convention.
    :param  jsonData: name of json
    :return boolean
    '''
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

# --------------------------------------------------------------------------- #

def open_json_file(path, file):
    '''
    Open JSON file object and returns the json object as dictionary
    :param path: directory, which needs to be explored
           file: name of json file 
    '''
    if file.startswith('PMC'):
        ext = '.xml.json'
    else:
        ext = '.json'
    with open(path + file + ext, encoding='utf-8') as json_file:
        return json.load(json_file)

# --------------------------------------------------------------------------- #

def get_entities(data):

    my_dict = data.loc['entities'][0]
    return pd.DataFrame(my_dict.items(), columns=['entities', 'count'])
      
# --------------------------------------------------------------------------- #

def get_entities_id(df):

    df['entities_id'] = df.entities.str.split(pat="/").str[-1]
    return df

# --------------------------------------------------------------------------- #

def get_id(data):
    '''
    Get paper id
    :param data: json file of the article
    :return: paper_id
    '''
    return data['paper_id']

# --------------------------------------------------------------------------- #

def get_article_id(data):
    return data.loc['id'].values[0]

# --------------------------------------------------------------------------- #

def get_article_title(data):
    return data['metadata']['title']

# --------------------------------------------------------------------------- #

def get_authors_names(data):

    list_of_authors = []
    for p in data['metadata']['authors']:
        
        if len(p['first']) == 0 or len(p['last']) == 0:
           continue
        else:
            # remove all characters except alphabets from a string to unidecode
            first = unidecode.unidecode( ''.join(m for m in p['first'] if m.isalpha()))
            middle = unidecode.unidecode( ''.join(m for m in p['middle'] if m.isalpha()))
            last = unidecode.unidecode( ''.join(m for m in p['last'] if m.isalpha()))

            list_of_authors.append(first + ', '+ middle + ' '+ last)

    return list_of_authors