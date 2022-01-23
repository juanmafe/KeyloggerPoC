# This script is a keylogger for educational purposes only.
# Author: @juanmafe.
# GPLv3 2022.

from Properties import Properties
from CheckFile import CheckFile

class OpenFile():

	def open_keylog():
		CheckFile.check_keylog_file()
		with open(Properties.path_keylog_file, "r") as fileOpened:
			CheckFile.clear_dirty_console_by_opened_files()
			print(fileOpened.read())
			fileOpened.close()

	
	def open_credentials():
		CheckFile.check_credentials_file()
		with open(Properties.path_credentials_file, "r") as fileOpened:
			CheckFile.clear_dirty_console_by_opened_files()
			print(fileOpened.read())
			fileOpened.close()

#EOF