#!/usr/bin/env python
# coding: utf-8

import torch, torchvision
torch.set_grad_enabled(False);

checkpoint = torch.hub.load_state_dict_from_url(
            url='https://dl.fbaipublicfiles.com/detr/detr-r50-e632da11.pth',
            map_location='cpu',
            check_hash=True)

# Remove class weights
del checkpoint["model"]["class_embed.weight"]
del checkpoint["model"]["class_embed.bias"]

# Save
torch.save(checkpoint, 'detr/detr-r50_no-class-head.pth')

