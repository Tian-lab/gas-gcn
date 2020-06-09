import os

ALL = [0]*60
Wrong = [0]*60
with open('./runs/ntu_cv_agcn_test_joint_right.txt') as trueFile:
    predict_true = trueFile.readlines()
    for line in predict_true:
        predict = line.split(',')[1]
        predict = int(predict)
        ALL[predict] += 1


with open('./runs/ntu_cv_agcn_test_joint_wrong.txt') as wrongFile:
    predict_wrong = wrongFile.readlines()
    for line in predict_wrong:
        predict = line.split(',')[2]
        predict = int(predict)
        Wrong[predict] += 1

for i in range(60):
    accuracy = (ALL[i]-Wrong[i])/ALL[i]
    print(accuracy)

