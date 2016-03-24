import sublime, sublime_plugin

class CopyrightmeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = self.view.visible_region()
		settings_file = sublime.load_settings('Preferences.sublime-settings');

		if settings_file.has('copyright_text'):
			text = settings_file.get('copyright_text')
		else:
			text = 'Please add the copyright_text to User Preferences'

		if text not in self.view.substr(region):
			self.view.insert(edit, 0, text + '\n\n')
