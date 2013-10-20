# coding=utf-8
"""
build exe
"""
__author__ = "indrajit"
from cx_Freeze import setup, Executable

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
path = []

GUI2Exe_Target_1 = Executable(script="main.py", base='Win32GUI', targetDir=r"dist", targetName="parse_table.exe",
                              compress=True, copyDependentFiles=True, appendScriptToExe=False,
                              appendScriptToLibrary=False)
setup(
    version="0.1",
    description="No Description",
    author="indrajit",
    name="source",
    options={"build_exe": {"includes": includes,
                           "excludes": excludes,
                           "packages": packages,
                           "path": path}
    },
    executables=[GUI2Exe_Target_1], requires=['cx_Freeze']
)