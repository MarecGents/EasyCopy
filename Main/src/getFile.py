import os
import json
import shutil
from datetime import datetime
import sys
import subprocess
import platform

USUAL_FILE_END = []
def get_file(exePath,filePath):
	path = exePath + f"{filePath}"
	f_open = open(path, "r+", encoding="utf-8")
	config = json.load(f_open)
	f_open.close()
	return config


def rewrite_file(exePath,filePath, data):
	path = exePath + filePath
	f_write = open(path, "w+", encoding="utf-8")
	json.dump(data, f_write, indent=4)
	f_write.close()
	pass


def get_real_path(now_path, relative_path):
	path = os.path.abspath(now_path + relative_path)
	return path


def checkup_(pathList):
	for path in pathList:
		if os.path.exists(path):
			continue
			pass
		if "." in path.split(os.path.sep)[-1]:
			with open(path, "w+", encoding="utf-8") as f:
				emptyJson = {}
				json.dump(emptyJson, f, indent=4, ensure_ascii=False)
				pass
			continue
		else:
			os.makedirs(path, exist_ok=True)
			continue
		pass
	pass


def move_file(source, dest):
	LogList = []
	for root_source, dirs_source, files_source in os.walk(source, topdown=False):
		# 构造相对于source的路径
		rel_path = os.path.relpath(root_source, source)
		# 构造目标路径（在folder_A中）
		target_path_dest = os.path.join(dest, rel_path)
		# 确保目标目录存在
		os.makedirs(target_path_dest, exist_ok=True)
		for file_source in files_source:
			src_file = os.path.join(root_source, file_source)
			dst_file = os.path.join(target_path_dest, file_source)
			shutil.move(src_file, dst_file)
			# print(f"已复制文件{src_file}到{dst_file}")
			LogList.append(f"{getTime()}:已剪切文件{src_file}到{dst_file}")
			pass
		for dir_name in dirs_source:
			dir_path = os.path.join(root_source, dir_name)
			try:
				os.rmdir(dir_path)  # 尝试删除空文件夹
				# print(f"已删除空文件夹: {dir_path}")
				LogList.append(f"{getTime()}:已删除空文件夹: {dir_path}")
			except OSError:
				# 如果文件夹不是空的，os.rmdir()会抛出OSError异常
				# 我们忽略这个异常，继续处理下一个文件夹
				pass
		pass
	return LogList
	pass

def copy_file(source, dest):
	LogList = []
	for root_source, dirs_source, files_source in os.walk(source, topdown=False):
		# 构造相对于source的路径
		rel_path = os.path.relpath(root_source, source)
		# 构造目标路径（在folder_A中）
		target_path_dest = os.path.join(dest, rel_path)
		# 确保目标目录存在
		os.makedirs(target_path_dest, exist_ok=True)
		for file_source in files_source:
			src_file = os.path.join(root_source, file_source)
			dst_file = os.path.join(target_path_dest, file_source)
			shutil.copy2(src_file, dst_file)
			# print(f"已复制文件{src_file}到{dst_file}")
			LogList.append(f"{getTime()}:已复制文件{src_file}到{dst_file}")
			pass
		pass
	return LogList
	pass

def writeLog(exePath,LogList):
	fileName = f"log-{getTime()}.txt"
	logPath = exePath + "Logs\\" + fileName
	f_write = open(logPath, "w+", encoding="utf-8")
	content = "\n".join(LogList)
	f_write.write(content)
	f_write.close()
	pass

def getTime():
	# 获取当前的日期和时间
	now = datetime.now()
	formatted_now = now.strftime("%Y-%m-%d_%H-%M-%S_%f")[:-3]
	return formatted_now
	pass


def compare_paths(path1, path2):
	# 将两个路径转换为绝对路径
	abs_path1 = os.path.abspath(path1)
	abs_path2 = os.path.abspath(path2)
	
	# 比较两个绝对路径是否相同
	return abs_path1 == abs_path2

def open_path(path):
	if not os.path.isdir(path):
		print(f"The specified path is not a directory: {path}")
		return
	if platform.system() == "Windows":
		os.startfile(path)
	elif platform.system() == "Darwin":
		subprocess.Popen(["open", path])
	else:  # Linux and others
		subprocess.Popen(["xdg-open", path])
	pass