# -*- coding: utf-8 -*-
# @Author: ding zeyuan
# @Date:   2019-7-5 18:24:32

l2i_dic = {u'B-解剖部位': 1, u'B-影像检查': 2, u'B-疾病和诊断': 3, u'B-药物': 4, u'B-手术': 5, u'B-实验室检验': 6, u'I-解剖部位': 7,
           u'I-影像检查': 8, u'I-疾病和诊断': 9, u'I-药物': 10, u'I-手术': 11, u'I-实验室检验': 12, u'E-解剖部位': 13, u'E-影像检查': 14,
           u'E-疾病和诊断': 15,
           u'E-药物': 16, u'E-手术': 17, u'E-实验室检验': 18, u'S-解剖部位': 19, u'S-影像检查': 20, u'S-疾病和诊断': 21, u'S-药物': 22,
           u'S-手术': 23, u'S-实验室检验': 24, "<pad>": 25, "<start>": 26, "<eos>": 27, "O": 0}

i2l_dic = {0:"O",1:u'B-解剖部位', 2:u'B-影像检查', 3:u'B-疾病和诊断',4:u'B-药物',5:u'B-手术',6:u'B-实验室检验',7:u'I-解剖部位',
               8:u'I-影像检查',9:u'I-疾病和诊断',10:u'I-药物',11:u'I-手术',12:u'I-实验室检验',13:u'E-解剖部位', 14:u'E-影像检查',15: u'E-疾病和诊断',
                16:u'E-药物',17:u'E-手术',18:u'E-实验室检验',19:u'S-解剖部位', 20:u'S-影像检查', 21:u'S-疾病和诊断',22:u'S-药物',23:u'S-手术',24:u'S-实验室检验',
            25:"<pad>", 26:"<start>", 27:"<eos>"}


train_file = './data/train.txt'
dev_file = './data/test.txt'
vocab_file = './data/bert/vocab.txt'

save_model_dir =  './data/model/'

max_length = 300
batch_size = 8
epochs = 2
tagset_size = len(l2i_dic)
use_cuda = False





l2i_dic = {"O": 0, "a-M": 1, "b-B": 2, "b-E": 3, "a-B": 4, "a-E": 5, "c-B": 6,
           "c-E": 7, "c-M": 8, "b-M": 9, "b-S": 10, "c-S": 11, "a-S": 12,"<pad>": 13,"<start>": 14, "<eos>": 15}

i2l_dic = {0: "O", 1: "a-M", 2: "b-B", 3: "b-E", 4: "a-B", 5: "a-E",
           6: "c-B", 7: "c-E", 8: "c-M", 9: "b-M", 10: "b-S", 11: "c-S", 12: "a-S",13:"<pad>", 14:"<start>", 15:"<eos>"}

train_file = './data/com_train.txt'
dev_file = './data/com_test.txt'
vocab_file = './data/my_bert/daguan_vocab.txt'

save_model_dir =  './data/model/'

max_length = 300
batch_size = 8
epochs = 2
tagset_size = len(l2i_dic)
use_cuda = False