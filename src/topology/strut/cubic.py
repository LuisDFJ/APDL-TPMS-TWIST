def topology( L : float = 0.010 ):
    r = [-L/2,L/2]
    CORNERS = [ ( x, y, z) for x in r for y in r for z in r ]
    return [], CORNERS