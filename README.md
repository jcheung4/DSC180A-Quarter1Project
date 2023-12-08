# StreetWatch - Detecting Wildfire Risk Using StreetView Imagery

The goals of this project is to identify SDG&E assets and to quantify the ability to identify risks from dmaaged infrastructure. [DETR](https://github.com/facebookresearch/detr/) will be used to train an object detection model that will be able to identify power poles as well as surface structures while Google StreetView will be used as the publicly accessible data source.

## Data Sources:
Training images are obtained using the [Google Street View Static API](https://developers.google.com/maps/documentation/streetview/overview).

1. The [streetwatch](https://github.com/pdashk/streetwatch) repository outlines how to download all the images into an output folder: `images`.
2. After running `python scripts/collect_images.py` in streetwatch, move the `images` output folder into the `data` directory of this repository.


## Setup

### Conda Environment
After cloning repository, navigate to root level and run:
```
conda env create -f environment.yml
```

### DETR Model
You must clone the DETR repository in order to train the model:
```
git clone https://github.com/woctezuma/detr.git
cd detr
git checkout finetune
cd ..
```

### Create Training and Validation Datasets
After adding `images` folder to root directory, run:
```
python scripts/train_val_split.py
```
*MORE ON RESULT*

### Training and Fine-Tuning the Model:
Run the cells in the `train_detr.ipynb` in order to train and fine-tune the model.

# Project Structure

```
├── data/               <- Local data files only (do not commit)
│
├── scripts/            <- Python scripts to run in command line
│
├── .gitignore          <- Git ignore file
│
├── environment.yml     <- Conda environment file
│
└── README.md           <- The top-level README for repo
```



