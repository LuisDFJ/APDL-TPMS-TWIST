def topology( L : float = 0.010 ):
    c = [
       ( 0, 0, 1 ),
       ( 0, 0,-1 ),
       ( 0, 1, 0 ),
       ( 0,-1, 0 ),
       ( 1, 0, 0 ),
       (-1, 0, 0 )
    ]
    r = [-1,1]
    CORNERS = [ ( x*L/2, y*L/2, z*L/2 ) for x in r for y in r for z in r ]
    CENTERS = [ ( x*L/2, y*L/2, z*L/2 ) for x,y,z in c ]
    return [], CENTERS + CORNERS