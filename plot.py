import os
import sys
import json
import matplotlib.pyplot as plt


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

# Rectangular : [ 0.022, 0.021, 0.020, 0.019, 0.018 ],
# Circular    : [ 0.011, 0.0105,0.010, 0.0095,0.009 ]

filters = [
    #("SECTION", "Circular"),
    #("BASE", "0.022")
    ("THICKNESS", "0.0006")
]
title = ""
for var, dat in filters:
    title = title + f"{var}: {dat}  "

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
    
def plot( data : list ):
    for entry in data:
        t = float( entry["THICKNESS"] )
        b = entry["BASE"] 
        legend = f"T: {t}, B: {b}"
        data = entry["DATA"]
        plt.plot( data[0], data[1], MK.next() )
        plt.annotate( legend, ( data[0][-1] - 0.05, data[1][-1] ) )
    plt.title( title )
    plt.xlabel( "Angle [rad]" )
    plt.ylabel( "Torque [Nm]" )
    #plt.legend( legend )
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
                data = filterData( results, filters )
                plot( data )

        else:
            print( f"File [{pathfile}] does not exists." )

    else:
        print( "Provide a directory." )