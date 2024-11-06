import os
import shutil
from src.TemplateBuilder import TemplateBuilder, unpack
from src.ExecBuilder import execBuilder
from src import EXPERIMENTS

import sys

def parse_arguments():
    cores = None
    post = "default"
    force = False
    for i in range( len( sys.argv ) ):
        if sys.argv[i] == "--force" or sys.argv[i] == "-f":
            force = True
        if sys.argv[i] == "--cores" or sys.argv[i] == "-c":
            try:
                cores = int( sys.argv[i+1] )
            except:
                cores = None
        if sys.argv[i] == "--post" or sys.argv[i] == "-p":
            try:
                post = sys.argv[i+1]
            except:
                post = "default"

    return cores, post, force

if __name__ == "__main__":
    cores, post, force = parse_arguments()
    
    c = 1
    if os.path.isdir( "./out/" ) and force: shutil.rmtree( "./out/" )
    for stype, top, lay, sec, base, l, divisor, t, n in EXPERIMENTS:
        TB = TemplateBuilder( stype,l,t,lay,unpack( base, divisor ),top,sec,n, post )
        filepath = f"./out/res{c}"
        c += 1
        if force: os.makedirs( filepath )
        TB.compile( filepath )
        TB.writeConfigs( filepath )
    
    
    if not isinstance( cores, type(None) ):
        print( f"Simulations Generated for DMP Processing using {cores} cores with {post} processor." )
    else:
        print( f"Simulations Generated for SMP Processing using default cores (4) with {post} processor." )
    execBuilder( "./out", cores )
                