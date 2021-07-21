# [RecSys.Scifi: Recommender Systems Datasets in Scientific Fields](https://lasigebiotm.github.io/RecSys.Scifi/)


<p align="center">
<img src="https://lasigebiotm.github.io/RecSys.Scifi/assets/img/recommender-bg.jpg" width="50%" height="50%">
</p>


Tutorial at the [ACM Conference on Knowledge Discovery and Data Mining (KDD)](https://www.kdd.org/kdd2021/)
Aug 14-18, 2021 

Schedule: Aug. 15, 2021 4:00 AM - 7:00 AM (Singapore Time)

## Table of Contents
  * [0. Prerequirements](#0-prerequirements)
  * [1. Download the repository](#1-download-the-repository)
  * [2. Preparation](#2-preparation)
  * [3. Open the tutorial](#3-open-the-tutorial)
  * [4. Close and Shutdown Jupyter Notebook](#4-close-and-shutdown-jupyter-notebook)
  * [5. Remove the created virtual environment](#5-remove-the-created-virtual-environment)
   

## 0. Prerequirements

- OS: Ubuntu 18.04 LTS or higher, OS X

- Python 3.8

- Browser (Firefox or Google Chrome)


## 1. Download the repository

a) With git clone:

```
git clone git@github.com:lasigeBioTM/RecSys.Scifi.tutorial.git

cd RecSys.Scifi.tutorial/
```

b) By retrieving directly the repository zip file 

```
wget https://github.com/lasigeBioTM/RecSys.Scifi.tutorial/archive/refs/heads/main.zip

unzip main.zip

cd RecSys.Scifi.tutorial-main/
```



## 2. Preparation

a) **If [Anaconda](https://docs.conda.io/en/latest/miniconda.html) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is installed**:

- Create virtual environment

```
conda create --name recsys_scifi python=3.8
```

- Activate the created virtual environment:

```
conda activate recsys_scifi
```

- Install dependencies:

```
python3.8 -m pip install -r requirements.txt
```

- Add the virtual environment to Jupyter:

```
ipython kernel install --user --name=recsys_scifi
```


b) **With [venv](https://docs.python.org/3/library/venv.html) module**:

- Install venv package and create virtual environment:

```
sudo apt install python3.8-venv

python3.8 -m venv recsys_scifi
```

- Activate the created virtual environment:

```
source recsys_scifi/bin/activate 
```

- Install dependencies:

```
python3.8 -m pip install -r requirements.txt
```

- Add the virtual environment to Jupyter:

```
ipython kernel install --user --name=recsys_scifi
```


## 3. Open the tutorial

- To start the Notebook Server run the following command:

```
jupyter notebook
```

Which will open http://localhost:8888/notebooks/ in the default browser.

- Open the file 'tutorial.ipynb'.

- Click on 'Kernel' > 'Change kernel' > 'recsys_scifi' to ensure the tutorial is running on the created virtual environment.


## 4. Close and Shutdown Jupyter Notebook

**a) Shutdown Jupyter Notebook Files from the dashboard**

- In the Kernel Sessions tab, click on 'SHUTDOWN' for the appropriate notebook to terminate the session for that notebook.

or

- In the File Browser tab and selecting 'Kernel' > 'Shutdown Kernel'.


**b) Shutdown the Jupyter Notebook Local Server**

You can also close your terminal by typing the command ```exit``` and hitting Enter.

## 5. Remove the created virtual environment

**a) Anaconda or Miniconda**


- Deactivate the created virtual environment:

```
conda deactivate
```

- Remove the virtual environment and all packages:

```
conda env remove --name recsys_scifi
```


**b) venv**


- Deactivate the created virtual environment:

```
deactivate
```

- Remove the virtual environment and all packages:

```
rm -r recsys_scifi

jupyter kernelspec uninstall recsys_scifi
```
