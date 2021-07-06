
###############################################################################
#                                                                             #  
# @author: Matilde Pato                                                       #  
# @email: matilde.pato@gmail.com                                              #
# @date: 29 Apr 2021                                                          #
# @version: 1.0                                                               #  
# Lasige - FCUL                                                               #
#                                                                             #  
# @last update:                                                               #  
#   version 1.1:                                                              #      
#   (author:   )                                                              # 
#                                                                             #   
#                                                                             #  
###############################################################################

import os
from pathlib import Path
from urllib.parse import quote
import unidecode

# --------------------------------------------------------------------------- #

def new_file(file):

    try:
        if not os.path.isfile(file):
            f = open(file, 'w')
    except OSError as error:
        print(error)  

# --------------------------------------------------------------------------- #

def get_blacklist(file):
    '''
    Return all articles to be removed, due some errors found there
    :param  file: name of file where the list will be found
    :return lst_articles: list of articles
    '''

    lst_articles = []
    if os.path.isfile(file):
        with open(file, 'r') as f:
            black_list = [content for content in f.readlines()]
        lst_articles.extend(black_list) 
        f.close()
    return  lst_articles       

# --------------------------------------------------------------------------- #

def set_blacklist(file, line):
    '''
    This function receives the article to and saves them in the
    blacklist file. The backlist contains all invalid articles, such
    as non-authors, non-entities, and others
    :param  filename: name of txt file
            line: all content
    :return none        
    '''
    
    new_file(file)
    with open(file, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n')
        f.write(content)
        f.close()

# --------------------------------------------------------------------------- #

def save_final_data(data, path):
    """
    Save data to csv file
    :param data: pandas Dataframe with columns <user, item, rating, ...>
    :param path: path to the csv file
    :return
    """
    if not os.path.exists(os.path.dirname(path)):
        Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)   
    data.to_csv(path, index=False, header=False)
    
# --------------------------------------------------------------------------- #

def save_metadata(file, line):
    '''
    This function will save all metadata about the process in txt file
    :param  filename: name of txt file
            line: all content
    :return none        
    '''

    new_file(file)    
    with open(file, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n')
        f.write('------------------------------------------------------' + '\n' + content)
        f.close()