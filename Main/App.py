import os

from src import GUI
# from src import getFile
# from src import makeCut


nowPath = os.path.abspath(os.path.dirname(os.path.realpath(__file__))+"\\..") + "\\"

mainloop = GUI.CutTools(exePath=nowPath).root.mainloop()
