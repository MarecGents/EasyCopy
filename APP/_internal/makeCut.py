from src import getFile
import os


def cut(exePath):
	config = getFile.get_file(exePath, "res\\config.json")
	if not config["SourcePath"] and config["AimPath"]:
		print("路劲缺失，无法执行\"复制\"|\"粘贴\"操作")
		raise SystemExit()
		pass
	# 步骤1：定义文件夹路径
	# 源文件夹路径  从这里将文件复制
	src_dir = config["SourcePath"]
	# 目标文件夹路径（如果不存在，它将被创建）  文件将在这里被粘贴
	dst_dir = config["AimPath"]
	# 备份文件夹路径
	backupPath = exePath + f"backup\\backup" + str(len(os.listdir(exePath + "backup")) + 1)
	
	# 步骤2：创建备份文件夹（如果不存在）
	getFile.checkup_([dst_dir, backupPath])
	LogList = []
	# 步骤3： 移动目标文件夹下的文件到备份文件夹
	LogList.extend(getFile.move_file(dst_dir, backupPath))
	LogList.extend(getFile.move_file(src_dir, dst_dir))
	
	getFile.writeLog(exePath,LogList)
	pass
