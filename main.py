import torch
import numpy as np
import random
import os
from train import train
from train_minlm import train_minlm

if __name__ == '__main__':
    """
    以下是需要调整的参数，别的都不需要改，直接运行脚本即可
    """

    description = "这里可以给本次实验加一些描述"
    EPOCHS = 15

    ALPHA_VITKD = [0.00003]
    
    BETA_VITKD = 0
    
    GAMA_VITKD = [0]
    
    #train_type = cae,mae, pkd_skip , pkd_first, pkd_last,kd,baseline,tiny,minlm
    train_type = "mae"

    #数据集有以下几种类型：hotel , shopping , waimai , movie
    data_set_type = "hotel"

    
    MASK_RATE = 0.5
    
    #注意力模块的参数
    REGRESSOER_DEPT = 3
    REGRESSOER_NUM_HEADS = 8
    """
    """



    BATCH_SIZE = 32
    LR = 0.00001
    NUM_LABELS = 2

    T_KD_LAYERS = [0, 3, 6, 9, 12]
    S_KD_LAYERS = [0, 2, 4, 6, 8]

    max_len_dict = {"hotel":150,"waimai":70,"shopping":150,"movie":100,"data4":120}
    MAX_SEQ_LEN = max_len_dict[data_set_type]
    
    
    



    for ALPHA_VITKD_item in ALPHA_VITKD:
        for GAMA_VITKD_item in GAMA_VITKD:
            seed_value = 2020  # 设定随机数种子
            np.random.seed(seed_value)
            random.seed(seed_value)
            os.environ['PYTHONHASHSEED'] = str(seed_value)  # 为了禁止hash随机化，使得实验可复现。
            torch.manual_seed(seed_value)  # 为CPU设置随机种子
            torch.cuda.manual_seed(seed_value)  # 为当前GPU设置随机种子（只用一块GPU）
            torch.cuda.manual_seed_all(seed_value)  # 为所有GPU设置随机种子（多块GPU）
            torch.backends.cudnn.deterministic = True

            #训练
            if train_type == "minlm":
                train_minlm(description = description,
                    MAX_SEQ_LEN = MAX_SEQ_LEN,
                    BATCH_SIZE = BATCH_SIZE,
                    LR = LR,
                    EPOCHS = EPOCHS,
                    NUM_LABELS = NUM_LABELS,
                    # 蒸馏损失相关参数
                    ALPHA_VITKD = ALPHA_VITKD_item,
                    BETA_VITKD = BETA_VITKD,
                    GAMA_VITKD = GAMA_VITKD_item,
                    MASK_RATE = MASK_RATE,
                    REGRESSOER_DEPT = REGRESSOER_DEPT,
                    REGRESSOER_NUM_HEADS = REGRESSOER_NUM_HEADS,
                    T_KD_LAYERS = T_KD_LAYERS,
                    S_KD_LAYERS = S_KD_LAYERS,
                    train_type = train_type,
                    data_set_type = data_set_type)
            else:  
                train(description = description,
                    MAX_SEQ_LEN = MAX_SEQ_LEN,
                    BATCH_SIZE = BATCH_SIZE,
                    LR = LR,
                    EPOCHS = EPOCHS,
                    NUM_LABELS = NUM_LABELS,
                    # 蒸馏损失相关参数
                    ALPHA_VITKD = ALPHA_VITKD_item,
                    BETA_VITKD = BETA_VITKD,
                    GAMA_VITKD = GAMA_VITKD_item,
                    MASK_RATE = MASK_RATE,
                    REGRESSOER_DEPT = REGRESSOER_DEPT,
                    REGRESSOER_NUM_HEADS = REGRESSOER_NUM_HEADS,
                    T_KD_LAYERS = T_KD_LAYERS,
                    S_KD_LAYERS = S_KD_LAYERS,
                    train_type = train_type,
                    data_set_type = data_set_type)
