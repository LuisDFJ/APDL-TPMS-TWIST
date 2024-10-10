import os
import shutil
from src.TemplateBuilder import TemplateBuilder
from src.ExecBuilder import execBuilder

L           = [ (0.010,1) ]
THICKNESS   = [ 0.0006 , 0.0005, 0.0004 ]
LAYERS      = [ 5 ]
TOPOLOGY    = [ "gyroid" ]      
SECTION     = { 
    "Rectangular" : [ 0.022, 0.021, 0.020, 0.019, 0.018 ],
    "Circular"    : [ 0.011, 0.0105,0.010, 0.0095,0.009 ]
}

if __name__ == "__main__":
    c = 1
    shutil.rmtree( "./out/" )
    
    for top in TOPOLOGY:
        for lay in LAYERS:
            for sec in SECTION.keys():
                for base in SECTION[sec]:
                    for l,divisor in L:
                        for t in THICKNESS:
                            TB = TemplateBuilder( l,t,lay,base/divisor,top,sec )
                            filepath = f"./out/res{c}"
                            c += 1
                            os.makedirs( filepath )
                            TB.compile( filepath )
                            TB.writeConfigs( filepath )
    
    execBuilder( "./out" )
                