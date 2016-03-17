import sublime, sublime_plugin

class CopyrightmeCommand(sublime_plugin.TextCommand):
	def run(self, edit, text):
		region = self.view.visible_region()

		if text not in self.view.substr(region):
			self.view.insert(edit, 0, text + '\n\n')
			
