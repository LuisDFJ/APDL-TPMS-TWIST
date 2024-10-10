import os

def execBuilder( path : str ):
    with open( f"{path}/run.bat", "w" ) as pFile:
        for dir in next( os.walk( path ) )[1]:
            print( f"echo Running {dir}", file=pFile )
            print( "ANSYS241.exe", end=" ", file=pFile )
            print( f"-b nolist -dir {dir}/res -j results -i {dir}/program.ansys -o {dir}/o.log", file=pFile, end="\n\n" )