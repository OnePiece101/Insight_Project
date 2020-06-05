from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

def ColorID(df, bgr_vals):    
    l = []
    for i in range(df.shape[0]):
        l.append([float(e) for e in df.rgb_mean[i].strip('()').split(',')])
        Z = np.array(l,dtype='float32')
    kmeans = KMeans(n_clusters=5,init='random',random_state=0).fit(Z)
    df['color_label'] = kmeans.labels_
    label = kmeans.predict(bgr_vals)
    return df[df['color_label'] == label[0]]