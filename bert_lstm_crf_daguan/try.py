import torch.nn as nn
from pytorch_pretrained_bert.modeling import BertModel
from model.crf import CRF
from torch.autograd import Variable
import torch

def test():
    return  Variable(
        torch.randn(2 * 2, 2, 2)), Variable(
        torch.randn(2 * 2, 2, 2))

a,b = test()
print(a)
print(b)