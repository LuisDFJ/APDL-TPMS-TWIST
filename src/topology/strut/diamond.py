def topology( L : float = 0.010 ):
    c = [
       ( 0, 0, 1 ),
       ( 0, 0,-1 ),
       ( 0, 1, 0 ),
       ( 0,-1, 0 ),
       ( 1, 0, 0 ),
       (-1, 0, 0 )
    ]
    w = [
        (-1,-1,-1),
        (-1, 1, 1),
        ( 1,-1, 1),
        ( 1, 1,-1),
    ]
    CORNERS = [ ( x*L/2, y*L/2, z*L/2 ) for x,y,z in w ]
    CENTERS = [ ( x*L/2, y*L/2, z*L/2 ) for x,y,z in c ]
    INODES  = [ ( x*L/4, y*L/4, z*L/4 ) for x,y,z in w ]
    return [], INODES + CENTERS + CORNERS