from math import atan, tan, pi

ft = lambda w : lambda t : atan( 1/tan( w*t ) )/w
fc = lambda w : lambda t : atan( 1/(tan(pi/8) * tan( w*t )) )/w

L1 = lambda L : lambda t : ( t, 0, -L/4 )
L2 = lambda L : lambda t : ( -L/8, t, ft( 2*pi/L )( t ) )
L3 = lambda L : lambda t : ( t, -L/8, ft( 2*pi/L )( t ) )
L4 = lambda L : lambda t : ( 0, t, -L/4 )
L5 = lambda L : lambda t : ( t, -L/16, fc( 2*pi/L )( t ) )
L6 = lambda L : lambda t : ( -L/16, t, fc( 2*pi/L )( t ) )

scale = lambda s : lambda f : lambda t : f( s*t )

def topology( L : float = 0.010 ):
    unify = scale( -L/8 )
    LINES = [
        unify( L1( L ) ),
        unify( L2( L ) ),
        unify( L3( L ) ),
        unify( L4( L ) ),
        unify( L5( L ) ),
        unify( L6( L ) ),
        ]

    CORNERS = [
        (    0,    0,-L/4),
        ( -L/8,    0,-L/4),
        ( -L/8, -L/8,-L/8),
        (    0, -L/8,-L/4),
        (    0,-L/16,-L/4 ),
        (-L/16, -L/8,fc(2*pi/L)( -L/8 ) ),
        ( -L/8,-L/16,fc(2*pi/L)( -L/8 ) ),
        (-L/16,    0,-L/4 ),
        (-L/16,-L/16,fc(2*pi/L)( -L/16 )),
    ]
    return LINES, CORNERS