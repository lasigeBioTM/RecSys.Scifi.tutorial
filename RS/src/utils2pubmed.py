###############################################################################
#                                                                             #  
# @author: Matilde Pato (Adapted from André Lamurias)                         #  
# @email: matilde.pato@gmail.com                                              #
# @date: 31 Mar 2021                                                          #
# @version: 1.0                                                               #  
# Lasige - FCUL                                                               #
#                                                                             #  
# @last update:                                                               #  
#   version 1.1:                                                              #      
#   (author: )                                              #  
###############################################################################
#
# This file get abstracts, authors, year based on PubMed
#

### -- PMID
from metapub import PubMedFetcher
from Bio import Entrez
Entrez.email = 'matilde.pato@gmail.com'

# --------------------------------------------------------------------------- #

def get_pmid(pmcid):
    '''
    Return PubMed ID
    
    :param  pmcid:
    :return pmid:         
    '''
    fetch = PubMedFetcher()
    article = fetch.article_by_pmcid(pmcid)
    return article.pmid

# --------------------------------------------------------------------------- #

def get_year_by_metapub(pmcid):
    '''
    Get PubMed year using metapub

    :param  pmcid:
    :return year         
    '''
    fetch = PubMedFetcher()
    article = fetch.article_by_pmcid(pmcid)
    return article.year

# --------------------------------------------------------------------------- #

def get_title_by_metapub(pmcid):
    '''
    Return PubMed ID
    
    :param  pmcid:
    :return pmid:         
    '''
    fetch = PubMedFetcher()
    #article = fetch.article_by_pmid(pmid)
    article = fetch.article_by_pmcid(pmcid)
    return article.title

# --------------------------------------------------------------------------- #

def get_title_by_bio(pmid):
    ''' 
    Get PubMed year using Bio

    :param  pmid: PMID' article
    :return year
    '''
    handle = Entrez.esummary(db="pubmed", id=pmid, retmode="xml")
    record = Entrez.parse(handle)
    return record['Title']

# --------------------------------------------------------------------------- #

def get_abstract_by_bio(pmid):
    ''' 
    Get PubMed year using Bio

    :param  pmid: PMID' article
    :return year
    '''
    handle = Entrez.efetch(db="pubmed", id=pmid, retmode="xml")
    record = Entrez.read(handle)
    handle.close()
    article = record['PubmedArticle'][0]['MedlineCitation']
    abstract = str()
            
    if 'Abstract' in article['Article'].keys(): # Some documents have no english abstract
        eng_content = article['Article']['Abstract']
    for element in eng_content['AbstractText']:
        abstract += element
    return abstract


# --------------------------------------------------------------------------- #

def get_year_by_bio(pmid):
    ''' 
    Get PubMed year using Bio

    :param  pmid: PMID' article
    :return year
    '''
    handle = Entrez.esummary(db="pubmed", id=pmid, retmode="xml")
    record = Entrez.parse(handle)
    return record['PubDate'].split()[0]

# --------------------------------------------------------------------------- #

def get_authors_by_bio(pmid):
    ''' 
    Get PubMed year using Bio

    :param  pmid: PMID' article
    :return authors dictionary
    '''
    handle = Entrez.efetch(db="pubmed", id=pmid, retmode="xml")
    record = Entrez.read(handle)
    handle.close()
    article = record['PubmedArticle'][0]['MedlineCitation']
    authors = list()
    if 'AuthorList' in article['Article'].keys():# Get authors info: only consider articles with at least 1 author
            
        for author in article['Article']['AuthorList' ]:             
            if 'ForeName' in author.keys() and 'LastName' in author.keys(): #Some authors are collective, e.g. 'ColectiveAuthor'
                author_dict = {"first": author['ForeName'], "last": author['LastName']}            
                authors.append(author_dict) 
    return authors

# --------------------------------------------------------------------------- #

def get_authors_by_metapub(pmid):
    '''
    Get PubMed year using metapub

    :param  pmcid:
    :return year         
    '''
    fetch = PubMedFetcher()
    article = fetch.article_by_pmid(pmid)
    return article.authors    

# --------------------------------------------------------------------------- #

def check_authors_by_bio(pmid):
    ''' 

    :param  pmid: PMID' article
    :return year
    '''
    handle = Entrez.efetch(db="pubmed", id=pmid, retmode="xml")
    record = Entrez.read(handle)
    handle.close()
    article = record['PubmedArticle'][0]['MedlineCitation']
    # Get authors info: only consider articles with at least 1 author
    if 'AuthorList' in article['Article'].keys():
        return True
    return False


# --------------------------------------------------------------------------- #

def check_authors_by_metapub(pmcid):
    ''' 

    :param  pmid: PMID' article
    :return year
    '''
    fetch = PubMedFetcher()
    article = fetch.article_by_pmcid(pmcid)
    if article.authors:
        return True
    return False