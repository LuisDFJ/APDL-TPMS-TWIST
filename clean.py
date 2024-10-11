import os
import shutil

PATH  = "./out"
PATHC = "./out_clean"

if __name__ == "__main__":
    for dir in next( os.walk( PATH ) )[1]:
        pathdirc = os.path.join( PATHC, dir )
        pathdir = os.path.join( PATH, dir )
        pathres = os.path.join( pathdir, "res" )

        if os.path.isdir( pathres ):
        
            if os.path.isdir( pathdirc ): shutil.rmtree( pathdirc )
            os.makedirs( pathdirc )

            
            for file in next( os.walk( pathdir ) )[2]:
                if ".txt" in file:
                    shutil.copyfile( os.path.join( pathdir, file ), os.path.join( pathdirc, file ) )

        
            for file in next( os.walk( pathres ) )[2]:
                if ".jpg" in file:
                    shutil.copyfile( os.path.join( pathres, file ), os.path.join( pathdirc, file ) )
