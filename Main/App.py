import pathlib

from src import GUI


if __name__ == "__main__":
	nowPath = str(pathlib.Path().absolute()) + "\\"
	mainloop = GUI.CutTools(exePath=nowPath).root.mainloop()
	pass
