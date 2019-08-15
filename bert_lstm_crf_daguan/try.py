import torch.nn as nn
from pytorch_pretrained_bert.modeling import BertModel
from model.crf import CRF
from torch.autograd import Variable
import torch

# f = open('data/train.txt',encoding='utf-8').readlines()
# print(f[0])
# print(f[0].split(' '))
# f1 = open('data/normal_daguan_train.txt',encoding='utf-8').readlines()
# print(f1[0])
# print(f1[0].split(' '))

import pickle
# vocab_file = './data/my_bert/daguan_vocab.txt'
# with open(vocab_file, 'rb') as f:
#     word2id = pickle.load(f)
a = {'111':0,'2231':1,'3214':2,'UNK':3}
df = open('try_vocab.txt','wb')
pickle.dump(a, df)
df.close()

with open('try_vocab.txt', 'rb') as f:
    word2id = pickle.load(f)

print(word2id)
print(word2id.get('2231'))
print(word2id.get('12314',3))