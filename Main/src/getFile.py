import os
import json
import shutil

NOW_PATH = os.path.dirname(os.path.abspath(__file__))
RES_PATH = "/../res"  # relative to this .py file


def get_file(filename):
	path = get_real_path(NOW_PATH, RES_PATH) + f"\\{filename}"
	f_open = open(path, "r+", encoding="utf-8")
	config = json.load(f_open)
	f_open.close()
	return config


def rewrite_file(filename, data):
	path = get_real_path(NOW_PATH, RES_PATH) + f"\\{filename}"
	f_write = open(path, "w+", encoding="utf-8")
	json.dump(data, f_write, indent=4)
	f_write.close()
	pass


def get_real_path(now_path, relative_path):
	path = os.path.abspath(now_path + relative_path)
	return path


def checkup_(pathList):
	for path in pathList:
		if not os.path.exists(path):
			os.makedirs(path)
			pass
		pass
	pass


def move_file(source, dest):
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
			print(f"已复制文件{src_file}到{dst_file}")
			pass
		for dir_name in dirs_source:
			dir_path = os.path.join(root_source, dir_name)
			try:
				os.rmdir(dir_path)  # 尝试删除空文件夹
				print(f"已删除空文件夹: {dir_path}")
			except OSError:
				# 如果文件夹不是空的，os.rmdir()会抛出OSError异常
				# 我们忽略这个异常，继续处理下一个文件夹
				pass
		pass
	pass
