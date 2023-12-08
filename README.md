# StreetWatch - Detecting Wildfire Risk Using StreetView Imagery

The goals of this project is to identify SDG&E assets and to quantify the ability to identify risks from dmaaged infrastructure. [DETR](https://github.com/facebookresearch/detr/) will be used to train an object detection model that will be able to identify power poles as well as surface structures while Google StreetView will be used as the publicly accessible data source.

## Data Sources:
Training images are obtained using the [Google Street View Static API](https://developers.google.com/maps/documentation/streetview/overview).

The [streetwatch](https://github.com/pdashk/streetwatch) repository outlines how to download all the images into the `images` folder.


## Setup

### Conda Environment
After cloning repo, navigating to root level and run:
```
conda env create -f environment.yml
```
