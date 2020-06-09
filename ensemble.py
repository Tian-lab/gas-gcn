import argparse
import pickle

import numpy as np
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--datasets', default='ntu/xsub', choices={'kinetics', 'ntu/xsub', 'ntu/xview', 'ntu120/xsub','ntu120/xsetup'},
                    help='the work folder for storing results')
parser.add_argument('--alpha', default=1, help='weighted summation')
arg = parser.parse_args()

dataset = arg.datasets
label = open('./data/NTU-RGB-D_120/xsetup-1/val_label.pkl', 'rb')
label = np.array(pickle.load(label))
r1 = open('./work_dir/' + dataset + '/agcn_test_joint_sw/epoch1_test_score.pkl', 'rb')
r1 = list(pickle.load(r1).items())
r2 = open('./work_dir/' + dataset + '/agcn_test_bone_sw/epoch1_test_score.pkl', 'rb')
r2 = list(pickle.load(r2).items())
r3 = []

for i in range(len(r1)):
    flag = 0
    filename = r1[i][0]
    for j in range(len(r2)):
        if filename == r2[j][0]:
            predict = [r2[j][0],r2[j][1]]
            r3.append(predict)
            flag = 1
    if flag == 0:
        print('fail')
r2 = r3
right_num = total_num = right_num_5 = 0
for i in tqdm(range(len(label[0]))):
    _, l = label[:, i]
    _, r11 = r1[i]
    _, r22 = r2[i]
    r = r11 + r22 * arg.alpha
    rank_5 = r.argsort()[-5:]
    right_num_5 += int(int(l) in rank_5)
    r = np.argmax(r)
    right_num += int(r == int(l))
    total_num += 1
acc = right_num / total_num
acc5 = right_num_5 / total_num
print(acc, acc5)
