import sublime
import sublime_plugin
import Copyrightme.constants

# make constants a little more readable
placeholder = Copyrightme.constants.COPYRIGHT_PLACEHOLDER
sublime_settings = Copyrightme.constants.SUBLIME_SETTINGS_FILE
copyright_preset = Copyrightme.constants.COPYRIGHT_PRESET_OPTION

class CopyrightmeCommand(sublime_plugin.TextCommand):

	# initial
	def run(self, document):
		self.document = document;
		self.region = self.view.visible_region()
		self.settings_file = sublime.load_settings(sublime_settings)	

		self.insertCopyright(self.presetCopyright());

	# use preset option or if doesnt exist use placeholder
	def presetCopyright(self):
		if self.settings_file.has(copyright_preset):
			text = settings_file.get(copyright_preset)
		else:
			text = placeholder

		return text;

	# insert copyright text in the first line
	def insertCopyright(self, text):
		if text not in self.view.substr(self.region):
			self.view.insert(self.document, 0, text + '\n\n')
