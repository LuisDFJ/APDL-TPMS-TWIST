import os
import sys
import json
import matplotlib.pyplot as plt
import numpy as np
from src import PLOTS_FILTERS

plt.rcParams.update({
#    "text.usetex": True,
    "font.family": "Times New Roman"
})

class MarkerRoulette:
    MARKERS = ( '', '.', '*' )
    LINES   = ( '-', '--', '-.', ':' )
    COLOR   = ( '#ffbe0b', '#fb5607', '#ff006e', '#8338ec', '#3a86ff' )
    def __init__(self) -> None:
        self.iter_t = self.__iter_type()
        self.iter_c = self.__iter_color()

    def next( self, getColor = False ):
        if getColor:
            return next( self.iter_t ), next( self.iter_c )
        else:
            return next( self.iter_t )

    def __iter_type(self):
        while True:
            for l in MarkerRoulette.LINES:
                for m in MarkerRoulette.MARKERS:
                    yield l+m
    
    def __iter_color(self):
        while True:
            for c in MarkerRoulette.COLOR:
                yield c

MK = MarkerRoulette()

def filterData( data : list, match : tuple | list ):
    if len( match ) == 1: match = match[0]
    if isinstance( match, list ):
        m = match.pop()
        return filterData( filterData( data, match ), m )
    else:
        nData = []
        for entry in data:
            if entry[ match[0] ] == match[1].replace(" ", ""):
                nData.append( entry )
        return nData
    
def plot( results : list ):
    for top in PLOTS_FILTERS.keys():
        for sec in PLOTS_FILTERS[top].keys():
            plt.figure()
            plt.title( f"Topology: {top.upper()} $\qquad$ Sec: {sec}", fontsize=18 )
            for base in PLOTS_FILTERS[top][sec].keys():
                try:
                    title = "$\ell$: {0} mm".format( float( base ) * 1000 )
                except:
                    title = "$\ell$: {0} mm".format( [ b*1000 for b in base ] )
                for filter in PLOTS_FILTERS[top][sec][base]:
                    data_x = []
                    data_y = []
                    for entry in filterData( results, filter ):
                        data_x.append( 1000 * float( entry["THICKNESS"] ) )
                        data_y.append( (1000**2 ) * entry["SLOPE"] * float( entry["LAYERS"] ) * float( entry["LENGTH"] ) )
                    
                    dx = [ x for x,_ in sorted( zip( data_x, data_y ), key= lambda k : k[0] ) ]
                    dy = [ y for _,y in sorted( zip( data_x, data_y ), key= lambda k : k[0] ) ]
                    plt.plot( dx, dy, MK.next() )    
                if len( dx ):
                    plt.annotate( title, ( dx[-1] - 0.005, dy[-1] + 10**3 ), fontsize=14 )
            
            plt.xlabel( r"Thickness $\left[mm\right]$", fontsize=16 )
            plt.ylabel( r"$\left<GJ\right>$ $\left[N\cdot mm^2\right]$", fontsize=16 )
            plt.xticks(fontsize=14)
            plt.yticks(fontsize=14)
            plt.grid( True )

def getMean( data : list ):
    N = len( data )
    M = len( data[0] )
    return [ sum( [ data[j][i] for j in range( N ) ] )/N for i in range( M ) ]

def getMax( data : list ):
    N = len( data )
    M = len( data[0] )
    return [ max( [ data[j][i] for j in range( N ) ] ) for i in range( M ) ]

def getMin( data : list ):
    N = len( data )
    M = len( data[0] )
    return [ min( [ data[j][i] for j in range( N ) ] ) for i in range( M ) ]


def plot_combined( results : list ):
    plt.figure()
    plt.title( f"Apparent Torsional Stiffness", fontsize=18 )
    for top in PLOTS_FILTERS.keys():
        for sec in PLOTS_FILTERS[top].keys():
            data = []
            for base in PLOTS_FILTERS[top][sec].keys():
                for filter in PLOTS_FILTERS[top][sec][base]:
                    data_x = []; data_y = []
                    for entry in filterData( results, filter ):
                        data_x.append( 1000 * float( entry["THICKNESS"] ) )
                        data_y.append( (1000**2 ) * entry["SLOPE"] * float( entry["LAYERS"] ) * float( entry["LENGTH"] ) )
                    
                    dx = [ x for x,_ in sorted( zip( data_x, data_y ), key= lambda k : k[0] ) ]
                    dy = [ y for _,y in sorted( zip( data_x, data_y ), key= lambda k : k[0] ) ]
                    data.append( dy )
            line_type, line_color = MK.next( True )
            plt.plot( dx, getMean( data ), line_type, color=line_color, linewidth=2 )
            plt.fill_between( dx, getMin(data), getMax(data), alpha=0.2, edgecolor=line_color, facecolor=line_color, linewidth=1 )
            plt.annotate( f"{top} - {sec}", ( dx[-1] - 0.005, getMean( data )[-1] + 10**3 ), fontsize=14 )
            
    plt.xlabel( r"Thickness $\left[mm\right]$", fontsize=16 )
    plt.ylabel( r"$\left<GJ\right>$ $\left[N\cdot mm^2\right]$", fontsize=16 )
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid( True )

if __name__ == "__main__":
    if len( sys.argv ) > 1:
        path = sys.argv[1]
        pathfile = os.path.join( path, "results.json" )
        if os.path.isfile( pathfile ):
            results = []
            with open( pathfile, "r" ) as pFile:
                results = json.load( pFile )
                plot( results )
                #plot_combined( results )
                plt.show()


        else:
            print( f"File [{pathfile}] does not exists." )

    else:
        print( "Provide a directory." )