# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
def sk_bunch_to_df(data):
	
	return pd.DataFrame(data= np.c_[data['data'], data['target']],
                     columns= data['feature_names'] + ['target'])
 

def save_matplotlib_fig(dir,path,name,tight_layout=True,**kwargs):
    '''
    :param dir: base directory to search in
    :param path:  folder name
    :param name:  file name
    :param tight_layout: use tight layout
    :param kwargs: params passed to pyplot savefig (see docs)
    :return:
    '''
    if tight_layout:
        plt.tight_layout()
    save_path = os.path.join(dir,path,name)
    plt.savefig(save_path+".png",format="png",dpi=300,kwargs=kwargs)


