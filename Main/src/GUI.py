import os
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import ttkbootstrap as ttks
import win32api
from src import makeCut
from src import getFile
import pathlib


class CutTools:
	
	def __init__(self, exePath):
		self.exePath = exePath
		getFile.checkup_(exePath + "backup\\")
		self.ch = getFile.get_file(self.exePath, "res\\locales\\ch.json")
		self.root = ttks.Window(
			title=self.ch["cuttools"],
			themename="morph",
			minsize=(650, 550)
		
		)
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
		self.buttonStart = ttks.Button(
			self.root,
			text=self.ch["start"],
			command=self.start
		)
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
		
		pass
	
	def showMainPage(self):
		self.buttonStart.place(relx=0.8, rely=0.8, relheight=0.15, relwidth=0.15)
		self.buttonDefaultPath.place(relx=0.6, rely=0.8, relheight=0.15, relwidth=0.15)
		self.buttonReadConfig.place(relx=0.4, rely=0.8, relheight=0.15, relwidth=0.15)
		pass
	
	def Frame1(self):
		self.search_sourcepath_var = tk.StringVar(value=str(pathlib.Path().absolute()))
		self.search_aimmingpath_var = tk.StringVar(value=str(pathlib.Path().absolute()))
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
			self.rewrite("SourcePath", self.search_sourcepath_var.get())
	
	def aimmingpathSelect(self):
		"""Callback for directory browse"""
		path = askdirectory(title='Directory')
		if path:
			self.search_aimmingpath_var.set(path)
			self.rewrite("AimPath", self.search_aimmingpath_var.get())
	
	def rewrite(self, key, value):
		configJson = getFile.get_file(self.exePath, "res\\config.json")
		configJson[key] = value
		getFile.rewrite_file(self.exePath, "res\\config.json", configJson)
		pass
	
	def start(self):
		nowPath = os.path.dirname(os.path.abspath(__file__))
		if self.search_aimmingpath_var.get() is nowPath or self.search_sourcepath_var.get() is nowPath:
			messagebox.showinfo(title=self.ch["operate"], message=self.ch["cutFailed1"], parent=self.root)
			return
		makeCut.cut(self.exePath)
		messagebox.showinfo(title=self.ch["operate"], message=self.ch["cutSuccess"], parent=self.root)
		pass
	
	def readConfig(self):
		configJson = getFile.get_file(self.exePath, "res\\config.json")
		self.search_sourcepath_var.set(configJson["SourcePath"])
		self.search_aimmingpath_var.set(configJson["AimPath"])
		pass
	
	def defaultPath(self):
		self.search_sourcepath_var.set(os.path.dirname(os.path.abspath(__file__)))
		self.search_aimmingpath_var.set(os.path.dirname(os.path.abspath(__file__)))
		pass
	
	pass

# CutTools().root.mainloop()
