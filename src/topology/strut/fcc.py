def topology( L : float = 0.010 ):
    r = [-L/2,L/2]
    c = [
       ( 0, 0, 1 ),
       ( 0, 0,-1 ),
       ( 0, 1, 0 ),
       ( 0,-1, 0 ),
       ( 1, 0, 0 ),
       (-1, 0, 0 )
    ]
    CORNERS = [ ( x, y, z) for x in r for y in r for z in r ]
    CENTERS = [ ( x*L/2, y*L/2, z*L/2 ) for x,y,z in c ]
    return [], CENTERS + CORNERS