SIMTYPE     = [ "shell" ]
L           = [ (0.010,1) ]
THICKNESS   = [ 0.0006 , 0.0005, 0.0004 ]
LAYERS      = [ 6,8,10 ]
TOPOLOGY    = [ ("diamond",2), ("gyroid",5) ]      
SECTION     = { 
    "Rectangular" : [ 0.022, 0.020, 0.018 ],
    "Circular"    : [ 0.011, 0.0105, 0.0095,0.009 ]
}

EXPERIMENTS   = []

for stype in SIMTYPE:
    for top, n in TOPOLOGY:
            for lay in LAYERS:
                for sec in SECTION.keys():
                    for base in SECTION[sec]:
                        for l,divisor in L:
                            for t in THICKNESS:
                                EXPERIMENTS.append( (stype, top, lay, sec, base, l, divisor, t, n) )

PLOTS_FILTERS = {}
for top, _ in TOPOLOGY:
        PLOTS_FILTERS[top] = {}
        for sec in SECTION.keys():
            PLOTS_FILTERS[top][sec] = []
            for base in SECTION[sec]:
                for lay in LAYERS:
                    PLOTS_FILTERS[top][sec].append(
                        [
                            ( "TOPOLOGY", top ),
                            ( "LAYERS",   str(lay+1) ),
                            ( "SECTION",  sec ),
                            ( "BASE",     str(base) ),
                        ]
                    )