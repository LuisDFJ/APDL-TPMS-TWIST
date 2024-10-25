import os


def getRecipe( dir : str ):
    return f"""
if exist {dir}\\Results_Angle_Torque.txt (
    echo Skipped: {dir} >> log.txt
)
else (
    echo Running {dir}
    ANSYS241.exe -b nolist -dir {dir}/res -j results -i {dir}/program.ansys -o {dir}/o.log
    if exist {dir}\\res\\*.rst (
        del /S {dir}\\res\\*.rst
    ) else (
        echo Failed: {dir} >> log.txt
    )
    if exist {dir}\\res\\*.rdb del /S {dir}\\res\\*.rdb
    if exist {dir}\\res\\*.db del /S {dir}\\res\\*.db
    if exist {dir}\\res\\*.esav del /S {dir}\\res\\*.esav
    if exist {dir}\\res\\*.r001 del /S {dir}\\res\\*.r001
    
    echo Completed: {dir} >> log.txt
)       
"""

def execBuilder( path : str ):
    with open( f"{path}/run.bat", "w" ) as pFile:
        print( "echo Log File: >> log.txt", file=pFile )
        for dir in next( os.walk( path ) )[1]:
            print( getRecipe( dir ), file=pFile )