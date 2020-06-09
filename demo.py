from __future__ import print_function
import argparse
import os
import time
import numpy as np
import yaml
import pickle
from collections import OrderedDict
# torch
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
from tqdm import tqdm
from tensorboardX import SummaryWriter
import shutil
import random
import inspect
import torch.backends.cudnn as cudnn
from model import agcn
from feeders import feeder
import graph
output_device = 0
weights = './ntu_cv_agcn_joint_sw-46-63168.pt'
def load_data(data_path,label_path,vid):
    loader = torch.utils.data.DataLoader(
        dataset=feeder.Feeder(data_path, label_path),
        batch_size=64,
        shuffle=False,
        num_workers=2)
    if vid is not None:
        sample_name = loader.dataset.sample_name
        sample_id = [name.split('.')[0] for name in sample_name]
        index = sample_id.index(vid)
        data, label, index = loader.dataset[index]
        data = data.reshape((1,) + data.shape)
    print(data.shape)
    return data, label,index

def test(skeleton_data):
    model = agcn.Model
    skeleton_data = torch.from_numpy(skeleton_data)
    data =skeleton_data.cuda(0).float()
    weight = torch.load(weights)
    new_state_dict = OrderedDict()
    weight = OrderedDict(
        [[k.split('module.')[-1],
          v.cuda(output_device)] for k, v in weight.items()])
    model = model(num_class=60, num_point=25, num_person=2, graph='graph.ntu_rgb_d.Graph',
                  graph_args={'labeling_mode': 'spatial'})
    model.load_state_dict(weight)
    model= model.eval().cuda(0)
    output = model(data)
    value, predict_label = torch.max(output.data, 1)
    return predict_label

if __name__ == '__main__':
    data_path = "./data/ntu/xview-1/val_data.npy"
    label_path = "./data/ntu/xview-1/val_label.pkl"
    video_id='S004C001P003R001A034'
    skeleton_data, label, _ = load_data(data_path,label_path,video_id)
    predict_label = test(skeleton_data)
    print(predict_label.item(),label)
