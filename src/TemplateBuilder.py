from src.topology.gyroid import topology as gtop
from src.topology.diamond import topology as dtop

def unpack( v : tuple | float, n : float = 1 ):
    if isinstance( v, float ):
        return tuple( [ v/n ] )
    return [ i/n for i in v ]

class TemplateBuilder:
    def __init__(self,
        stype : str  = "shell",
        l : float    = 0.010,
        t : float    = 0.0005,
        lay : int    = 5,
        base : float = 0.020,
        top : str    = "gyroid", 
        sec : str    = "Rectangular",
        N : int     = 5 ):
        self.stype = stype
        self.l = l
        self.t = t
        self.lay  = lay
        self.base = base
        self.top  = top
        self.sec  = sec
        self.N    = N
        self.initRecipe()
        self.compilePoints()

    def initRecipe( self ):
        self.recipe = [
                ( f"./geometry/{self.stype}/{self.top}/Cell_Points.ansys",              [] ),
                ( f"./geometry/{self.stype}/{self.top}/Patch_{self.N}.ansys",[] ),
                ( f"./geometry/{self.stype}/{self.top}/Triperiodic_Cell.ansys",         [] ),
                ( f"./geometry/{self.stype}/{self.top}/Unit_Cell.ansys",                [] ),
                ( f"./geometry/{self.stype}/Base_Layer.ansys",                          [] ),
                ( f"./geometry/{self.stype}/section/{self.sec}.ansys",                  [ *self.base ] ),
                ( f"./geometry/{self.stype}/Repeat_Layers.ansys",                       [self.lay] ),
                (  "./postprocess.ansys",                                               [] ),
        ]

    def compilePoints( self ):
        if self.top == "gyroid":
            top = gtop
        elif self.top == "diamond":
            top = dtop

        LINES, CORNERS = top( self.l )
        c = 1
        with open( f"./geometry/{self.stype}/{self.top}/Cell_Points.ansys", "w" ) as pFile:
            for p in CORNERS:
                print( f"K,{c},", end="", file=pFile )
                print( *p, sep=",", file=pFile )
                c += 1

            for line in LINES:
                for p in range( 1, self.N ):
                    print( f"K,{c},", end="", file=pFile )
                    print( *line( p/self.N ), sep=",", file=pFile )
                    c += 1

    def compileRecipe( self ):
        TEXT_ARGS = []
        for file, args in self.recipe:
            with open( file, "r" ) as pFile:
                TEXT_ARGS.append( pFile.read().format( *args ) )

        TEMPLATE = ""
        with open( f"./geometry/{self.stype}/template.ansys", "r" ) as pFile:
            TEMPLATE = pFile.read()
        
        return TEMPLATE, TEXT_ARGS

    def compile( self, path : str ):
        TEMPLATE, TEXT_ARGS = self.compileRecipe()
        TNAME = str(self.t * 1000).replace(".","")
        with open( f"{path}/program.ansys", "w" ) as pFile:
            ANSYS_FILE = TEMPLATE.format( self.l, self.t, *TEXT_ARGS )
            
            I = ANSYS_FILE.find( "XXX" )
            if I != -1:
                ANSYS_FILE = ANSYS_FILE[:I]
            
            pFile.write( ANSYS_FILE )

    def writeConfigs( self, path : str ):
        base = self.base if len( self.base ) > 1 else self.base[0]
        with open( f"{path}/config.txt", "w" ) as pFile:
            print( f"LENGTH:    {self.l}", file=pFile )
            print( f"THICKNESS: {self.t}", file=pFile )
            print( f"SECTION:   {self.sec}", file=pFile )
            print( f"BASE:      {base}", file=pFile )
            print( f"TOPOLOGY:  {self.top}", file=pFile )
            print( f"LAYERS:    {self.lay + 1}", file=pFile )

    