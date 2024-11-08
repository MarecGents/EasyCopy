import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import ttkbootstrap as ttks
import win32api
from src import makeCut
from src import getFile

CONFIG_PATH = "res\\config.json"


class CutTools:
	
	def __init__(self, exePath):
		self.exePath = exePath
		self.check_need_file()
		self.check_configJson()
		self.ch = getFile.get_file(self.exePath, "res\\locales\\ch.json")
		self.root = ttks.Window(
			title=self.ch["cuttools"],
			themename="morph",
			minsize=(650, 550),
		
		)
		self.root.iconbitmap(self.exePath + "res\\img\\EasyCopy.ico")
		screen_width, screen_height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
		self.root.maxsize = (screen_width, screen_height)
		self.root.geometry('%dx%d' % (screen_width / 3, screen_height / 2))
		
		tf = ttks.font
		
		self.Frame1()
		self.showFrame1()
		self.MainPage()
		self.showMainPage()
		pass
	
	def MainPage(self):
		self.buttonDefaultPath = ttks.Button(
			self.root,
			text=self.ch["defaultPath"],
			command=self.defaultPath
		)
		self.buttonReadConfig = ttks.Button(
			self.root,
			text=self.ch["readConifg"],
			command=self.readConfig
		)
		self.buttonCleanPath = ttks.Button(
			self.root,
			text=self.ch["cleanPath"],
			command=self.cleanPath
		)
		self.buttonCopy = ttks.Button(
			self.root,
			text=self.ch["start_copymethod"],
			command=lambda: self.start(self.ch["copymethod"])
		)
		self.buttonCut = ttks.Button(
			self.root,
			text=self.ch["start_cutmethod"],
			command=lambda: self.start(self.ch["cutmethod"])
		)
		
		
		pass
	
	def showMainPage(self):
		self.buttonReadConfig.place(relx=0.01, rely=0.3, relheight=0.10, relwidth=0.15)
		self.buttonDefaultPath.place(relx=0.2, rely=0.3, relheight=0.10, relwidth=0.12)
		self.buttonCleanPath.place(relx=0.36, rely=0.3, relheight=0.10, relwidth=0.12)
		self.buttonCopy.place(relx=0.85, rely=0.3, relheight=0.10, relwidth=0.12)
		self.buttonCut.place(relx=0.7, rely=0.3, relheight=0.10, relwidth=0.12)
		pass
	
	def Frame1(self):
		self.search_sourcepath_var = tk.StringVar(value=self.exePath)
		self.search_aimmingpath_var = tk.StringVar(value=self.exePath)
		self.frame1 = ttks.LabelFrame(
			self.root,
			text=self.ch["selectPath"],
			labelanchor='n'
		)
		self.lable1 = ttks.Label(
			self.frame1,
			text=self.ch["sourcepath"],
			# background="#FFFFFF",
		)
		self.entry1 = ttks.Entry(
			self.frame1,
			textvariable=self.search_sourcepath_var
		)
		self.button1 = ttks.Button(
			self.frame1,
			text=self.ch["selectPath"],
			command=self.sourcepathSelect
		)
		self.lable2 = ttks.Label(
			self.frame1,
			text=self.ch["aimmingpath"],
			# background="#FFFFFF",
		)
		self.entry2 = ttks.Entry(
			self.frame1,
			textvariable=self.search_aimmingpath_var
		)
		self.button2 = ttks.Button(
			self.frame1,
			text=self.ch["selectPath"],
			command=self.aimmingpathSelect
		)
		
		pass
	
	def showFrame1(self):
		self.frame1.place(relx=0.005, rely=0.01, relheight=0.25, relwidth=0.99)
		
		self.lable1.place(relx=0.02, rely=0.1, relheight=0.3, relwidth=0.08)
		self.entry1.place(relx=0.12, rely=0.1, relheight=0.3, relwidth=0.65)
		self.button1.place(relx=0.8, rely=0.075, relheight=0.35, relwidth=0.15)
		
		self.lable2.place(relx=0.02, rely=0.6, relheight=0.3, relwidth=0.09)
		self.entry2.place(relx=0.12, rely=0.6, relheight=0.3, relwidth=0.65)
		self.button2.place(relx=0.8, rely=0.575, relheight=0.35, relwidth=0.15)
		pass
	
	def sourcepathSelect(self):
		"""Callback for directory browse"""
		path = askdirectory(title=self.ch['selectPath'])
		if path:
			self.search_sourcepath_var.set(path)
			self.rewriteConfig()
	
	def aimmingpathSelect(self):
		"""Callback for directory browse"""
		path = askdirectory(title='Directory')
		if path:
			self.search_aimmingpath_var.set(path)
			self.rewriteConfig()
	
	def rewriteConfig(self):
		configJson = getFile.get_file(self.exePath, CONFIG_PATH)
		configJson["SourcePath"] = self.search_sourcepath_var.get()
		configJson["AimPath"] = self.search_aimmingpath_var.get()
		getFile.rewrite_file(self.exePath, CONFIG_PATH, configJson)
		pass
	
	def start(self, method):
		sourcePath = self.search_sourcepath_var.get()
		aimmingPath = self.search_aimmingpath_var.get()
		messageTitle = self.ch["operate"] + ":" + method
		if not sourcePath or not aimmingPath:
			self.messageShow(messageTitle, self.ch["cutFailed2"].replace("${s}", method))
			return
		elif (getFile.compare_paths(aimmingPath, self.exePath) or
		      getFile.compare_paths(sourcePath, self.exePath)):
			self.messageShow(messageTitle, self.ch["cutFailed1"].replace("${s}", method))
			return
		elif sourcePath == aimmingPath:
			self.messageShow(messageTitle, self.ch["cutFailed3"].replace("${s}", method))
			return
		status = makeCut.cut_method(self.exePath, method, [sourcePath, aimmingPath])
		if status == 1:
			self.messageShow(messageTitle, self.ch["cutSuccess"].replace("${s}", method))
		elif status == -1:
			self.messageShow(messageTitle, self.ch["cutFailed0"].replace("${s}", method))
		pass
	
	def readConfig(self):
		configJson = getFile.get_file(self.exePath, CONFIG_PATH)
		self.search_sourcepath_var.set(configJson["SourcePath"])
		self.search_aimmingpath_var.set(configJson["AimPath"])
		pass
	
	def defaultPath(self):
		self.search_sourcepath_var.set(self.exePath)
		self.search_aimmingpath_var.set(self.exePath)
		self.rewriteConfig()
		pass
	
	def cleanPath(self):
		self.search_sourcepath_var.set("")
		self.search_aimmingpath_var.set("")
		self.rewriteConfig()
		pass
	
	def check_need_file(self):
		pathList = [
			self.exePath + "backup\\",
			self.exePath + "Logs\\",
			self.exePath + CONFIG_PATH
		]
		getFile.checkup_(pathList)
		pass
	
	def check_configJson(self):
		configJson = getFile.get_file(self.exePath, CONFIG_PATH)
		if "SourcePath" in configJson and "AimPath" in configJson:
			return True
		else:
			configJson = {
				"SourcePath": "",
				"AimPath": ""
			}
			getFile.rewrite_file(self.exePath, CONFIG_PATH, configJson)
		pass
	
	def messageShow(self, title, message):
		messagebox.showinfo(title=title, message=message, parent=self.root)
		pass
	
	pass

# CutTools().root.mainloop()
