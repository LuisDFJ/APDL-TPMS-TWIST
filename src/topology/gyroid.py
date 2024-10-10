from math import atan, sin, cos, asin, pi

ft = lambda w : lambda t : -atan( sin( w*t ) )/w
fc = lambda w : lambda t : -atan ( 1/cos( w*t ) )/w
fs = lambda w : lambda t : asin( sin( 2*w*t )/2 )/w

L1 = lambda L : lambda t : ( t, 0, ft( 2*pi/L )( t ) )
L2 = lambda L : lambda t : ( 0, ft( 2*pi/L )( -t ), -t )
L3 = lambda L : lambda t : ( t, -fc( 2*pi/L )( t ), -L/4 )
L4 = lambda L : lambda t : ( L/4, t, fc( 2*pi/L )( t ) )
L5 = lambda L : lambda t : ( t, t, -fs( 2*pi/L )( t ) - t )

scale = lambda s : lambda f : lambda t : f( s*t )

def topology( L : float = 0.010 ):
    unify = scale( L/4 )
    LINES = [
        unify( L1( L ) ),
        unify( L2( L ) ),
        unify( L3( L ) ),
        unify( L4( L ) ),
        unify( L5( L ) )
        ]

    CORNERS = [
        (  0,  0,   0),
        (L/4,  0,-L/8),
        (  0,L/8,-L/4),
        (L/4,L/4,-L/4)
    ]
    return LINES, CORNERS