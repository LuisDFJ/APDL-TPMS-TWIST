import os
import shutil
from src.TemplateBuilder import TemplateBuilder, unpack
from src.ExecBuilder import execBuilder
from src import EXPERIMENTS

import sys



if __name__ == "__main__":
    c = 1
    if os.path.isdir( "./out/" ): shutil.rmtree( "./out/" )
    for stype, top, lay, sec, base, l, divisor, t, n in EXPERIMENTS:
        TB = TemplateBuilder( stype,l,t,lay,unpack( base, divisor ),top,sec,n )
        filepath = f"./out/res{c}"
        c += 1
        os.makedirs( filepath )
        TB.compile( filepath )
        TB.writeConfigs( filepath )
    
    cores = None
    for i in range( len( sys.argv ) - 1 ):
        if sys.argv[i] == "--cores":
            try:
                cores = int( sys.argv[i+1] )
            except:
                cores = None
    if not isinstance( cores, type(None) ):
        print( f"Simulations Generated for DMP Processing using {cores} cores." )
    else:
        print( f"Simulations Generated for SMP Processing using default cores (4)." )
    execBuilder( "./out", cores )
                