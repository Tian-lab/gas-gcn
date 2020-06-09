import torch
import torch.nn as nn
import torch.nn.functional as F


class GatedCNN(nn.Module):
    '''
        In : (N, sentence_len)
        Out: (N, sentence_len, embd_size)
    '''
    def __init__(self, in_chs, out_chs, kernel_size, padding, stride):
        super(GatedCNN, self).__init__()
        # self.embd_size = embd_size
        self.conv = nn.Conv2d(in_chs, out_chs, kernel_size, padding=padding, stride=stride)
        self.conv_gate = nn.Conv2d(in_chs, out_chs, kernel_size, padding=padding, stride=stride)

    def forward(self, x):
        A = self.conv(x)
        B = self.conv_gate(x)
        output = A*F.sigmoid(B)
        return output