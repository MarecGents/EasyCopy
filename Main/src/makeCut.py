from . import getFile
import os
from .setting import SettingControl

CH_PATH = "res\\locales\\ch.json"

def cut_method(exePath, operate, pathList):
	# config = getFile.get_file(exePath, "res\\config.json")
	# if not config["SourcePath"] and config["AimPath"]:
	# 	print("路劲缺失，无法执行\"复制\"|\"粘贴\"操作")
	# 	# raise SystemExit()
	# 	return -1
	# 	pass
	
	# 步骤1：定义文件夹路径
	# 源文件夹路径  从这里将文件复制
	src_dir = pathList[0]
	# 目标文件夹路径（如果不存在，它将被创建）  文件将在这里被粘贴
	dst_dir = pathList[1]
	# 备份文件夹路径
	backupPath = exePath + f"backup\\backup" + str(len(os.listdir(exePath + "backup")) + 1)
	# 步骤2：创建备份文件夹（如果不存在）
	getFile.checkup_([dst_dir, backupPath])
	LogList = []
	LogList.append(f"{getFile.getTime()} | method:{operate}\n"
	               f"From:{src_dir}\n"
	               f"To:{dst_dir}\n")
	
	if SettingControl(exePath).backup_if():
		LogList.extend(getFile.move_file(dst_dir, backupPath))
		pass
	if operate == (getFile.get_file(exePath, CH_PATH))["copymethod"]:
		LogList.extend(getFile.copy_file(src_dir, dst_dir))
		pass
	elif operate == (getFile.get_file(exePath, CH_PATH))["cutmethod"]:
		LogList.extend(getFile.move_file(src_dir, dst_dir))
		pass
	getFile.writeLog(exePath, LogList)
	return 1
	pass
