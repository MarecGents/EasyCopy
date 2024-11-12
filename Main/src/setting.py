from . import getFile

SETTING_PATH = "res\\settings\\file_settings.json"


class SettingControl:
	
	def __init__(self, exePath):
		self.exePath = exePath
		self.file_settings = getFile.get_file(self.exePath, SETTING_PATH)
		pass
	
	def backup_if(self):
		return self.file_settings['setting']['backup']
	
	def only_copy(self):
		return self.file_settings['setting']['only_copy']
	
	def only_cut(self):
		return self.file_settings['setting']['only_cut']
	
	def save_backup(self,value):
		self.file_settings['setting']['backup'] = (True if value ==True else False)
		self.save_settings()
		pass
	def save_only_copy(self,value):
		self.file_settings['setting']['only_copy'] = (True if value ==True else False)
		self.save_settings()
		pass
	def save_only_cut(self,value):
		self.file_settings['setting']['only_cut'] = (True if value ==True else False)
		self.save_settings()
		pass
	
	def save_settings(self):
		getFile.rewrite_file(self.exePath, SETTING_PATH, self.file_settings)
	pass