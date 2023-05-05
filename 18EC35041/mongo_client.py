from pymongo import MongoClient as mc
from scipy.spatial import Delaunay
import numpy as np
# from triangulation_core.linear_algebra import lexigraphic_sort
# from triangulation_core.triangulation import triangulate as triangulate
import matplotlib.pyplot as plt 
if __name__ == "__main__":

    db_client = mc("10.5.18.101")
    ans = db_client.BI.Anguli_200k_1M

    first = ans.find_one()
    d = first
    a = ans.find()
    dc = a.next()
    print(dc.keys())
    #print(dir(ans.find()))
    pts = [[float(i[0]), float(i[1])] for i in d['mv']]
    #print(pts)
    
    pts = np.array(pts)
    dtri = Delaunay(pts)
    #print(dtri.simplices)
    plt.triplot(pts[:,0], pts[:,1], dtri.simplices)
    plt.plot(pts[:,0], pts[:,1], 'o')
    plt.show()

    meta = db_client.BI.meta
    mf = meta.find()
    #print(mf.next())

    x = np.linspace(0,20,1)
    plt.plot(x, np.sin(x))
    plt.show()
    