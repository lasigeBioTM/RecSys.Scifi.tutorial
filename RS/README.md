# README #

This module creates a recommendation dataset with the format of <user, item, rating, item_name, year>, where users are authors from research articles, the items are biomedical entities from multi-field ontologies, and
the ratings are the number of articles an author wrote about an item. 



### Requirements: ###
* python > 3
* numpy
* configargparse
* pandas
* scipy
* sklearn
* lenskit
* cffi
* unidecode
* unicode
* rdflib
* pubmed-lookup==0.2.3
* Bio==0.4.1
* entrezpy==2.1.3
* requests==2.6.0

### Data: ###
* Original documents: https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge 
* Entities Documents: From https://github.com/lasigeBioTM/SciRec2021-CORD19/NER/data/comm_use_subset/


### Running: ###
* configure config file

````
python create_dataset.py
````

* output: csv file with user, item, rating columns

