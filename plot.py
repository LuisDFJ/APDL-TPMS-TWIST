import os
import sys
import json
import matplotlib.pyplot as plt
from src import PLOTS_FILTERS

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Helvetica"
})

class MarkerRoulette:
    MARKERS = ( '', '.', '*' )
    LINES   = ( '-', '--', '-.', ':' )
    def __init__(self) -> None:
        self.iter = self.__iter()

    def next( self ):
        return next( self.iter )

    def __iter(self):
        while True:
            for l in MarkerRoulette.LINES:
                for m in MarkerRoulette.MARKERS:
                    yield l+m

MK = MarkerRoulette()

def filterData( data : list, match : tuple | list ):
    if len( match ) == 1: match = match[0]
    if isinstance( match, list ):
        m = match.pop()
        return filterData( filterData( data, match ), m )
    else:
        nData = []
        for entry in data:
            if entry[ match[0] ] == match[1]:
                nData.append( entry )
        return nData
    
def plot( results : list ):
    for top in PLOTS_FILTERS.keys():
        for sec in PLOTS_FILTERS[top].keys():
            plt.figure()
            for filter in PLOTS_FILTERS[top][sec]:
                data_x = []
                data_y = []
                title = " ".join( [ f"{s[0:3]}: {v}" for s, v in filter ] )
                for entry in filterData( results, filter ):
                    data_x.append( float( entry["THICKNESS"] ) )
                    data_y.append( entry["SLOPE"] * float( entry["LAYERS"] ) * float( entry["LENGTH"] ) )
                
                dx = [ x for x,_ in sorted( zip( data_x, data_y ), key= lambda k : k[0] ) ]
                dy = [ y for _,y in sorted( zip( data_x, data_y ), key= lambda k : k[0] ) ]
                plt.plot( dx, dy, MK.next() )    
                if len( dx ):
                    plt.annotate( title, ( dx[-1] - 0.00005, dy[-1] ) )
            
            plt.xlabel( r"Thickness [$m$]" )
            plt.ylabel( r"$\left<GJ\right>$ [$Nm^2/rad$]" )
            plt.grid( True )
    plt.show()

if __name__ == "__main__":
    if len( sys.argv ) > 1:
        path = sys.argv[1]
        pathfile = os.path.join( path, "results.json" )
        if os.path.isfile( pathfile ):
            results = []
            with open( pathfile, "r" ) as pFile:
                results = json.load( pFile )
                plot( results )

        else:
            print( f"File [{pathfile}] does not exists." )

    else:
        print( "Provide a directory." )