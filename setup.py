from cx_Freeze import setup, Executable

base = 'Win32GUI'    

executables = [Executable(
	script="DarkRP Timer.py",
	base=base,
	icon="icon.ico")]

packages = ["idna", 'tkinter', 'ctypes', 'time', 'winsound', 're']
includefiles = ['icon.ico', 'sound.wav', 'tcl86t.dll', 'tk86t.dll']
options = {
    'build_exe': {    
        'packages':packages,
		'include_files':includefiles
    },    
}

setup(
    name = "DarkRP Printer Timer",
    options = options,
    version = "1.0",
    description = 'A Timer Application intended to keep track of printers in DarkRP. Application made by Kazilii#7302 on discord. @KaziliiSB on Twitter.',
    executables = executables
)