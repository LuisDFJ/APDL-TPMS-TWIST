import os
import sys
import json

def parseConfig( filepath : str ) -> dict :
    config = {}
    with open( filepath, "r" ) as pFile:
        for line in pFile.readlines():
            var = line.replace( " ", "" ).replace("\n","").split(":")
            config[ var[0] ] = var[1]
    return config

def parseData( filepath : str ) -> list :
    angle  = []
    torque = []
    with open( filepath, "r" ) as pFile:
        for line in pFile.readlines():
            var = line.replace( " ", "" ).replace( "\n", "" ).split( "," )
            angle .append( float(var[0]) )
            torque.append( float(var[1]) )
    return [ angle, torque ]

if __name__ == "__main__":
    if len( sys.argv ) > 1:
        path = sys.argv[1]
        if os.path.isdir( path ):
            formatRes = []
            for dir in next( os.walk( path ) )[1]:
                dirPath     = os.path.join( path, dir )
                configPath  = os.path.join( dirPath, "config.txt" )
                resPath     = os.path.join( dirPath, "Results_Angle_Torque.txt" )
                if os.path.isfile( configPath ) and os.path.isfile( resPath ):
                    entry = parseConfig( configPath )
                    data  = parseData( resPath )
                    entry["DATA"] = data
                    formatRes.append( entry )
            with open( os.path.join( path, "results.json" ), "w" ) as pFile:
                json.dump( formatRes, pFile, indent=2 )

        else:
            print( "Directory does not exists." )

    else:
        print( "Provide a directory." )