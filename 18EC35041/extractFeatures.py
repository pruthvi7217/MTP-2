from scipy.spatial import Delaunay
from classes import Parallel
from pathlib import Path
from pymongo import MongoClient as mc
import numpy as np
import pprint
import math

def basicFeatures(mpts, triangles):
    fv = []
    for t in triangles:
        vertices = [mpts[i] for i in t]
        l1 = ((vertices[1][0]-vertices[2][0])**2+(vertices[1][1]-vertices[2][1])**2)**0.5
        l2 = ((vertices[0][0]-vertices[2][0])**2+(vertices[0][1]-vertices[2][1])**2)**0.5
        l3 = ((vertices[0][0]-vertices[1][0])**2+(vertices[0][1]-vertices[1][1])**2)**0.5
        alpha1 = math.acos((l2*l2+l3*l3-l1*l1)/(2*l2*l3))
        alpha2 = math.acos((l1*l1+l3*l3-l2*l2)/(2*l3*l1))
        alpha3 = math.acos((l2*l2+l1*l1-l3*l3)/(2*l2*l1))
        alpha_max = max(alpha1,max(alpha2,alpha3))
        if alpha_max>(2/3)*math.pi:
            continue
        alpha=math.cos(alpha_max)
        p=l1+l2+l3
        s=p/2
        a=(s*(s-l1)*(s-l2)*(s-l3))**0.5
        beta=(p*p)/a
        gamma=max(l1,max(l2,l3))/min(l1,min(l2,l3))
        fv.append((alpha, beta, gamma))
    return fv
if __name__ == "__main__":

    database = mc("10.5.18.101")
    print(type(database))
    print(database.list_database_names())
    print("------------------------------------------------------------------------------------------------------------------")
    db  = mc("10.5.18.101")["BI"]
    ans = db['Anguli_200k_1M'].find_one()
    pts = [[float(i[0]), float(i[1])] for i in ans['mv']]
    dtri = Delaunay(pts)

    fv = basicFeatures(pts, dtri.simplices)
    for i in fv[:20]:
        print(i)
    
    
