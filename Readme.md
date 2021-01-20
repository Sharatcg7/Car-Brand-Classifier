
## Car Brand Classification
Tasks-

- ML Training pipeline to train the pre-trained CNN to classify 3 different car brands.
- Inference Script to run the prediction on a random picture from a given URLs and provide their matching probabilities on each of the brands
- Classification model, returns the most similar image to sample S from the
training data set for a given a random sample S 

### Dependency installation

````bash
conda env update --file environment.yaml 
source activate car_brand
````
or 

````bash
pip install -r requirements.txt 
````


### Data download
Automated web scraping script to downloads the data from the google 
````bash
cd utils/
python data_scraper.py ---car-brand audi
````

### Data preparation
Once the images are downloaded, split the train, val. test data set as mentioned below.

Project directory tree should be look like this:
````bash
$ROOT/
├── /data
│   ├── test
│   │   ├── audi
│   │   ├── benz
│   │   └── bmw
│   ├── train
│   │   ├── audi
│   │   ├── benz
│   │   └── bmw
│   └── val
│       ├── audi
│       ├── benz
│       └── bmw
|
├── /inference_data
├── /output
├── /utils
│   |── driver
│   |    └── geckodriver
│   └── data_scraper.py
├── /config.json 
├── /model_interface.ipynb
└── /model_training.ipynb

````

### Model Training 

````bash
model_training.ipynb
````
Open this in jupyter notebook to train the model.

Script Functionalities- 
1. Loads the dataset according the data split
2. Build model
3. Train model
4. Save model
5. Test prediction
6. convert the H5 to pb file

### Model Inference 

````bash
model_inference .ipynb
````
Script Functionalities- 
1. Downloads the random picture from the given URls
2. Loads the data and saved H5 model
3. Inference on random downloaded test samples  
4. Returns the most similar image to sample S from the
training data set


### Results

| Sr. No | Model | Model Size | epochs | optimizer | train Acc | Val ACC |
|:--------:|:--------:|:--------:|:--------:|:----------------:|:------------------:|:----------------:|
| 1 | MobileNet2 | 14 MB |30 | Adam  | 70.05 | 84.38 | 
| 2 | ResNet50 | 98 MB |30 | Adam  |  34.47 | 39.58 |

## Contributors
* **Sharat Gujamagadi**

## Contact
* **Sharat Gujamagadi** (sharatcg7@gmail.com)