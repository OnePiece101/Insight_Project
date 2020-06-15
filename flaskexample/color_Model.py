from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

def ColorID(df, bgr_vals):    
    l = []
    for i in range(df.shape[0]):
        l.append([float(e) for e in df.bgr_mean[i].strip('()').split(',')])
        Z = np.array(l,dtype='float32')
    kmeans = KMeans(n_clusters=15).fit(Z)
    df['color_label'] = kmeans.labels_
    centers = kmeans.cluster_centers_
    df['color_distance'] = 0
    for j in range(len(centers)):
        idx = df[df['color_label'] == j].index
        df['color_distance'][idx] = np.sqrt(((centers[j]-Z[idx])**2).sum(axis=1))
    label = kmeans.predict(bgr_vals)
    if np.sqrt(((bgr_vals[0]-centers[label[0]])**2).sum()) <= df[df['color_label'] == label[0]].color_distance.max():
        df_result = df[df['color_label'] == label[0]]
        df_result['color_distance'] = np.sqrt(((Z[df['color_label'] == label[0]]-bgr_vals[0])**2).sum(axis=1))
        df_result = df_result.sort_values(by='color_distance')[:5]
        return df_result
    else:
        return "Sorry, the color you're looking is very special and we couldn't find a good match in our database."
    