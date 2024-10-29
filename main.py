import os
import shutil
from src.TemplateBuilder import TemplateBuilder, unpack
from src.ExecBuilder import execBuilder
from src import EXPERIMENTS




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
    
    execBuilder( "./out" )
                