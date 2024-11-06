# Free-end Experiments 2

#SIMTYPE     = [ "shell" ]
#L           = [ (0.010,1) ]
#THICKNESS   = [ 0.0005 ]
#LAYERS      = [ 9 ]
#TOPOLOGY    = [ ("diamond",2), ("gyroid",5) ]
#SECTION     = { 
#    "Rectangular" : [ 0.022, 0.020, 0.018, 0.016 ],
#    "Circular"    : [ 0.011, 0.0105, 0.0095, 0.009 ],
#    "AsymmetricA"  : [ (0.022, 0.001), (0.022, 0.002), (0.022, 0.003), (0.022, 0.004),
#                       (0.020, 0.001), (0.020, 0.002), (0.020, 0.003), (0.020, 0.004),
#                       (0.018, 0.001), (0.018, 0.002), (0.018, 0.003), (0.018, 0.004), ]
#}

# WIP

SIMTYPE     = [ "strut" ]
L           = [ (0.005,1) ]
THICKNESS   = [ 0.0009, 0.0008, 0.0007, 0.0006, 0.0005, 0.0004, 0.0003 ]
LAYERS      = [ 19 ]
TOPOLOGY    = [ ("bcc",4), ("fcc",4), ("cubic",4), ("diamond",4), ("fluorite",4), ("octet",4) ]
SECTION     = { 
    "Rectangular" : [ 0.022, 0.020, 0.018 ],
    "Circular"    : [ 0.011, 0.0105, 0.0095, 0.009 ],
    "AsymmetricA"  : [ (0.022, 0.001), (0.020, 0.001), (0.018, 0.001) ]
}

# BCC Strut Experiments

#SIMTYPE     = [ "strut" ]
#L           = [ (0.005,1) ]
#THICKNESS   = [ 0.0009, 0.0008, 0.0007, 0.0006, 0.0005, 0.0004, 0.0003 ]
#LAYERS      = [ 19 ]
#TOPOLOGY    = [ ("bcc",4) ]
#SECTION     = { 
#    "Circular" : [ 0.014 ],
#}

# Free-end Experiments

#SIMTYPE     = [ "shell" ]
#L           = [ (0.010,1) ]
#THICKNESS   = [ 0.0005 ]
#LAYERS      = [ 9 ]
#TOPOLOGY    = [ ("diamond",2), ("gyroid",5) ]
#SECTION     = { 
#    "Rectangular" : [ 0.020 ],
#    "Circular"    : [ 0.011 ],
#    "AsymmetricA"  : [ (0.020, 0.001) ]
#}

# Asymmetric Experiments

#SIMTYPE     = [ "shell" ]
#L           = [ (0.010,1) ]
#THICKNESS   = [ 0.0009, 0.0008, 0.0007, 0.0006, 0.0005, 0.0004, 0.0003 ]
#LAYERS      = [ 9 ]
#TOPOLOGY    = [ ("diamond",2), ("gyroid",5) ]
#SECTION     = { 
#    "Rectangular" : [ 0.022, 0.020, 0.018 ],
#    "Circular"    : [ 0.011, 0.0105, 0.0095, 0.009 ],
#    "AsymmetricA"  : [ (0.022, 0.001), (0.020, 0.001), (0.018, 0.001) ]
#}

# Symmetric Experiments

#SIMTYPE     = [ "shell" ]
#L           = [ (0.010,1) ]
#THICKNESS   = [ 0.0006, 0.0005, 0.0004 ]
#LAYERS      = [ 6,8,10 ]
#TOPOLOGY    = [ ("diamond",2), ("gyroid",5) ]
#SECTION     = { 
#    "Rectangular" : [ 0.022, 0.020, 0.018 ],
#    "Circular"    : [ 0.011, 0.0105, 0.0095,0.009 ],
#}

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
            PLOTS_FILTERS[top][sec] = {}
            for base in SECTION[sec]:
                PLOTS_FILTERS[top][sec][base] = []
                for lay in LAYERS:
                    PLOTS_FILTERS[top][sec][base].append(
                        [
                            ( "TOPOLOGY", top ),
                            ( "LAYERS",   str(lay+1) ),
                            ( "SECTION",  sec ),
                            ( "BASE",     str(base if isinstance( base, float ) else list(base)) ),
                        ]
                    )