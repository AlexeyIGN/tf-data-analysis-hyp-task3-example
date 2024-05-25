import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 1017890038 # Ваш chat ID, не меняйте название переменной

def solution(control, test) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    statistic, p_value = ttest_ind(control, test, alternative = 'greater')
    mean = 4563.65
    var = 23067579472.51
    alpha = 0.01
    
    if p_value < 0.01:
        return True
    else:
        return False
