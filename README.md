# daguan_ner_Bert_bilstm_crf
达观算法比赛ner任务，从训练bert到预测。

由于达观比赛数据是脱敏的，所以要使用词向量，需要自己训练。

bert的预训练可以使用 https://github.com/circlePi/Pretraining-Yourself-Bert-From-Scratch
得到，由于达观比赛的数据没有指定上下句，所以预训练时候，代码中只用到了mask任务。

训练好的bert放在，data/my_bert 文件夹下，名为“pytorch_bert.bin"。

整体效果受模型超参和bert本身的训练效果所致，这个模型的最好结果，也还没跑完。

我自己训练的bert可以从以下链接下载
链接:https://pan.baidu.com/s/113LG-wt9gIGDbRkaqd53Ww  密码:m891

有问题欢迎交流。
