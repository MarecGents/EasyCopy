import os

from src import GUI
# from src import getFile
# from src import makeCut

# use this code when using pyinstaller
nowPath = os.path.abspath(os.path.dirname(os.path.realpath(__file__))+"\\..") + "\\"
# use this code when debugging
# nowPath = os.path.abspath(os.path.dirname(os.path.realpath(__file__))) + "\\"

mainloop = GUI.CutTools(exePath=nowPath).root.mainloop()
