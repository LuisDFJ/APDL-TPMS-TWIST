import os

def progressBar(i,N):
    E = 25
    progress = "#"*int( E*(i/N) ) + " "*(E - int( E*(i/N) ) )
    return f"""
cls
echo Progress: [{progress}] {i}/{N}
"""

def getPreamble():
    return f"""
@ECHO OFF
echo Log File: >> log.txt
"""

def getRecipe( dir : str, cores : int | None, part : tuple ):
    if isinstance( cores, type(None) ):
        parallel_processing = ""
    else:
        parallel_processing = f"-dis -np {cores} "
    return f"""
{progressBar(*part)}
IF exist {dir}\\Results_Angle_Torque.txt (
    echo Skipped: {dir} >> log.txt
) ELSE (
    echo Running {dir}
    ANSYS241.exe {parallel_processing}-b nolist -dir {dir}/res -j results -i {dir}/program.ansys -o {dir}/o.log
    IF exist {dir}\\res\\*.rst (
        del /S {dir}\\res\\*.rst
    ) ELSE (
        echo Failed: {dir} >> log.txt
    )
    IF exist {dir}\\res\\*.rdb del /S {dir}\\res\\*.rdb
    IF exist {dir}\\res\\*.db del /S {dir}\\res\\*.db
    IF exist {dir}\\res\\*.esav del /S {dir}\\res\\*.esav
    IF exist {dir}\\res\\*.r001 del /S {dir}\\res\\*.r001
    
    echo Completed: {dir} >> log.txt
)       
"""

def execBuilder( path : str, cores : int | None = None ):
    with open( f"{path}/run.bat", "w" ) as pFile:
        print( getPreamble(), file=pFile )
        dirs = next( os.walk( path ) )[1]
        for i, dir in enumerate( dirs ):
            print( getRecipe( dir, cores, (i+1,len(dirs)) ), file=pFile )