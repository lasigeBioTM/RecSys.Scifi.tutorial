
###############################################################################
#                                                                             #  
# @author: Márcia Barros                                                      #  
# @email:                                                          #
# @date: 17 Feb 2021                                                          #
# @version: 1.0                                                               #  
# Lasige - FCUL                                                               #
#                                                                             #  
# @last update:                                                               #  
#   version 1.1: 31 Mar 2021                                                  #      
#   (author: Matilde Pato, matilde.pato@gmail.com)                            # 
#                                                                             #   
#                                                                             #  
###############################################################################

import unidecode
import numpy as np
import pandas as pd

# --------------------------------------------------------------------------- #

def get_user_item_rating(lst, df):
    '''
    Append <user, item, rating> tuple
    :param  lst: list of authors (or, users)
            df: dataframe with entities        
    :return dataframe with user, item and rating equal to 1        
    '''
    user_item_rating = []

    for author in lst:
        for entity in df.entities_id:
            user_item_rating.append([author, entity, 1])

    return user_item_rating

# --------------------------------------------------------------------------- #

def id_to_index(df):
    """
    maps the values to the lowest consecutive values
    :param df: pandas Dataframe with columns user, item, rating
    :return: pandas Dataframe with the columns index_item and index_user
    """

    index_user = np.arange(0, len(df.user.unique()))

    df_user_index = pd.DataFrame(df.user.unique(), columns=["user"])
    df_user_index["new_index"] = index_user

    df["index_user"] = df["user"].map(df_user_index.set_index('user')["new_index"]).fillna(0)
    #print(df)
    return df


# --------------------------------------------------------------------------- #

def remove_accents(a):
    return unidecode.unidecode(a.decode('utf-8'))

# --------------------------------------------------------------------------- #

def remove_accents_from_authors(records_df, column):
    records_df[column] = records_df[column].astype('unicode')
    records_df[column] =  records_df[column].str.normalize('NFKD').str.\
        encode('ascii', errors='ignore').str.decode('utf-8')

    # for i in range(records_df[column].size):
    #
    #     for b in range(len(records_df[column][i])):
    #         records_df[column][i][b] = unidecode.unidecode(records_df[column][i][b])

    return records_df

# --------------------------------------------------------------------------- #


def get_authors_metadata(data, label, ident):
    
    authors = data[data.label == ident].authors.values[0].split(';')
    for a in authors:
        a = a.split(',')
        first = unidecode.unidecode( ''.join(m for m in a[1] if m.isalpha()))
        last = unidecode.unidecode( ''.join(m for m in a[0] if m.isalpha()))
    return first + ', '+  last