import os
import sys
import cv2

def filesIn( path : str, match : str ):
    return [ file for file in next( os.walk( path ) )[2] if match in file ]

if __name__ == "__main__":
    if len( sys.argv ) > 1:
        path = sys.argv[1]
        if os.path.isdir( path ):
            for dir in next( os.walk( path ) )[1]:
                pathdir = os.path.join( path, dir )

                vwtr = cv2.VideoWriter( os.path.join( pathdir, 'video.mp4' ),  cv2.VideoWriter_fourcc(*'mp4v'), 3, (1077,810) ) 
                for file in  filesIn( pathdir, ".jpg" ) :
                    filepath = os.path.join( pathdir, file )
                    vwtr.write( cv2.imread( filepath ) )

                vwtr.release()

        else:
            print( "Directory does not exists." )

    else:
        print( "Provide a directory." )