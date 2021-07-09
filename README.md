# RecSys.Scifi.tutorial

[*Recommender Systems Datasets in Scientific Fields*](https://lasigebiotm.github.io/RecSys.Scifi/)

Tutorial at ACM Conference on Knowledge Discovery and Data Mining (KDD)
Aug 14-18, 2021 Schedule: Aug. 15, 2021 4:00 AM - 7:00 AM (Singapore Time)


## Preparation

1. Create virtual environment with conda and python=3.6:

```
conda create --name recsys_scifi python=3.6
```

2. Activate the created virtual environment

```
source activate recsys_scifi
```

3. Install dependencies:

```
python3.6 -m pip install -r requirements.txt
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
