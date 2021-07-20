# RecSys.Scifi.tutorial

[*Recommender Systems Datasets in Scientific Fields*](https://lasigebiotm.github.io/RecSys.Scifi/)

Tutorial at ACM Conference on Knowledge Discovery and Data Mining (KDD)
Aug 14-18, 2021 Schedule: Aug. 15, 2021 4:00 AM - 7:00 AM (Singapore Time)

## Download the repository

1. With git clone:

```
git clone git@github.com:lasigeBioTM/RecSys.Scifi.tutorial.git

cd RecSys.Scifi.tutorial/
```

2. 

```
wget https://github.com/lasigeBioTM/RecSys.Scifi.tutorial/archive/refs/heads/main.zip

unzip main.zip

cd RecSys.Scifi.tutorial-main/
```

**With [Anaconda](https://docs.conda.io/en/latest/miniconda.html) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and Python 3.8**


## Preparation

1. Create virtual environment

```
conda create --name recsys_scifi python=3.8
```

2. Activate the created virtual environment:

```
conda activate recsys_scifi
```

3. Install dependencies:

```
python3.8 -m pip install -r requirements.txt
```

4. Add the virtual environment to Jupyter:

```
ipython kernel install --user --name=recsys_scifi
```


**Virtual Environment with Virtualenv/venv**

1. Create virtual environment:

```
sudo apt install python3.8-venv

python3.8 -m venv recsys_scifi
```

2. Activate the created virtual environment:

```
source recsys_scifi/bin/activate 
```

3. Install dependencies:

```
python3.8 -m pip install -r requirements.txt
```

4. Add the virtual environment to Jupyter:

```
ipython kernel install --user --name=recsys_scifi
```


## Open tutorial

1. Run the following command:

```
jupyter notebook
```

Which will open http://localhost:8888/notebooks/ in the browser.

2. Open the file 'tutorial.ipynb'.

3. Click on 'Kernel' > 'Change kernel' > 'recsys_scifi' to ensure the tutorial is running on the created virtual environment.


## Close tutorial

1. Close and Shutdown Jupyter Notebook

1.1. Shutdown Jupyter Notebook Files from the dashboard

In the Kernel Sessions tab, click SHUTDOWN for the appropriate notebook to terminate the session for that notebook.

or,

In the File Browser tab and selecting Kernel > then Shutdown Kernel.

1.2. Shutdown the Jupyter Notebook Local Server

You can also close your terminal by typing the command ```exit``` and hitting Enter.


**With [Anaconda](https://docs.conda.io/en/latest/miniconda.html) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and Python 3.8**


2. Deactivate the created virtual environment:

```
conda deactivate
```

3. Remove the virtual environment and all packages:

```
conda env remove --name recsys_scifi
```


**Virtual Environment with Virtualenv/venv**


2. Deactivate the created virtual environment:

```
deactivate
```

3. Remove the virtual environment and all packages:

```
rm -r recsys_scifi

jupyter kernelspec uninstall recsys_scifi
```
