import os


def getRecipe( dir : str ):
    return f"""
IF exist {dir}\\Results_Angle_Torque.txt (
    echo Skipped: {dir} >> log.txt
) ELSE (
    echo Running {dir}
    ANSYS241.exe -acc nvidia -na 1 -np 6 -nt 2 -b nolist -dir {dir}/res -j results -i {dir}/program.ansys -o {dir}/o.log
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

def execBuilder( path : str ):
    with open( f"{path}/run.bat", "w" ) as pFile:
        print( "echo Log File: >> log.txt", file=pFile )
        for dir in next( os.walk( path ) )[1]:
            print( getRecipe( dir ), file=pFile )