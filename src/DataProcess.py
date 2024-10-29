import os
import json

import numpy as np

def calcSlope( results_path : str ):
    with open( results_path, "r" ) as pFile:
        results = json.load( pFile )
        for entry in results:
            entry["SLOPE"] = lestSquares( entry["DATA"], 2 )
    with open( results_path, "w" ) as pFile:
        json.dump( results, pFile, indent=2 )

def lestSquares( data, N ):
    n = len( data[0] )
    phi = lambda x : [ x**p for p in range( N ) ]
    A = np.zeros( (N,N) )
    b = np.zeros( (N,1) )
    for i in range( N ):
        for j in range( N ):
            A[i,j] = sum( [ phi( data[0][k] )[j] * phi( data[0][k] )[i] for k in range( n ) ] )
        b[i] = sum( [ data[1][k] * phi( data[0][k] )[i] for k in range( n ) ] )
    return np.linalg.solve( A, b )[1,0]