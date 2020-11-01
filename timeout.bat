@ECHO OFF

@REM Activate the environment
call conda activate base

@REM Run the application
python .\Vitali_Lupusor_Python_test.py %*
