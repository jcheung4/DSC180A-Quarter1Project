# StreetWatch - Detecting Wildfire Risk Using StreetView Imagery

The goals of this project is to identify SDG&E assets and to quantify the ability to identify risks from dmaaged infrastructure. [DETR](https://github.com/facebookresearch/detr/) will be used to train an object detection model that will be able to identify power poles as well as surface structures while Google StreetView will be used as the publicly accessible data source.

## Data Sources:
**Training images** are obtained using the [Google Street View Static API](https://developers.google.com/maps/documentation/streetview/overview).

1. The [streetwatch](https://github.com/pdashk/streetwatch) repository outlines how to download all the images into an output folder: `images`.
2. After running `python scripts/collect_images.py` in streetwatch, move the `images` output folder into the `data` directory of this repository.


**Image annotations** in COCO json format will be needed for the model to train on. Training and validation annotations should be placed within the `data/annotations` directory and be named `custom_train.json` and `custom_val.json` respectively.
> [!NOTE]
> For the streetwatch data specifically, the annotations have already been added in the `data/annotations` directory as the original source is a private Sharepoint within our subject domain.

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

### Create Training/Validation Datasets and Prepare files to train model
After adding `images` folder to root directory and cloning the DETR repository, run:
```
python scripts/initialize.py
```
This will download the model's "base" which will be used in the training process.

### Train the Model
In order to train the model, run the following:
```
python detr/main.py \
  --dataset_file "custom" \
  --coco_path "data" \
  --output_dir "outputs" \
  --resume "detr/detr-r50_no-class-head.pth" \
  --num_classes 3 \
  --epochs 1 \
  --device cuda
```
The parameters preceded by "--" may be modified accordingly such as the number of epochs to train for or what directory output files will be saved to.
> [!IMPORTANT]
> A GPU is required to timely train the model.

### Visualize Model Results
Run the cells within the `Model-Visualization.ipynb` file to display image examples of training/validation data as well as graphs on specfiic fields of interest.

# Project Structure

```
├── data/               <- Local data files only (do not commit)
│   ├── annotations
│       ├── custom_train.json
│       ├── custom_val.json
│   ├── training_imgs
│   ├── validation_imgs
│
├── scripts/            <- Python scripts to run in command line
│
├── .gitignore          <- Git ignore file
│
├── environment.yml     <- Conda environment file
│
└── README.md           <- The top-level README for repo
```



