from src.topology.gyroid import topology as gtop

class TemplateBuilder:
    N = 5
    def __init__(self,
        l : float    = 0.010,
        t : float    = 0.0005,
        lay : int    = 5,
        base : float = 0.020,
        top : str    = "gyroid", 
        sec : str    = "Rectangular" ):
        self.l = l
        self.t = t
        self.lay  = lay
        self.base = base
        self.top  = top
        self.sec  = sec
        self.initRecipe()
        self.compilePoints()

    def initRecipe( self ):
        self.recipe = [
                ( f"./geometry/{self.top}/Cell_Points.ansys",       [] ),
                ( f"./geometry/{self.top}/Triperiodic_Cell.ansys",  [] ),
                ( f"./geometry/{self.top}/Unit_Cell.ansys",         [] ),
                (  "./geometry/Base_Layer.ansys",                   [] ),
                ( f"./geometry/{self.sec}.ansys",                   [self.base] ),
                (  "./geometry/Repeat_Layers.ansys",                [self.lay] ),
                (  "./postprocess.ansys",                           [] ),
        ]

    def compilePoints( self ):
        if self.top == "gyroid":
            top = gtop

        LINES, CORNERS = top( self.l )
        c = 1
        with open( f"./geometry/{self.top}/Cell_Points.ansys", "w" ) as pFile:
            for p in CORNERS:
                print( f"K,{c},", end="", file=pFile )
                print( *p, sep=",", file=pFile )
                c += 1

            for line in LINES:
                for p in range( 1, TemplateBuilder.N ):
                    print( f"K,{c},", end="", file=pFile )
                    print( *line( p/TemplateBuilder.N ), sep=",", file=pFile )
                    c += 1

    def compileRecipe( self ):
        TEXT_ARGS = []
        for file, args in self.recipe:
            with open( file, "r" ) as pFile:
                TEXT_ARGS.append( pFile.read().format( *args ) )

        TEMPLATE = ""
        with open( "./template.ansys", "r" ) as pFile:
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
        with open( f"{path}/config.txt", "w" ) as pFile:
            print( f"LENGTH:    {self.l}", file=pFile )
            print( f"THICKNESS: {self.t}", file=pFile )
            print( f"SECTION:   {self.sec}", file=pFile )
            print( f"BASE:      {self.base}", file=pFile )
            print( f"TOPOLOGY:  {self.top}", file=pFile )

    