import sublime, sublime_plugin

class OpenSublimeProjectFileCommand(sublime_plugin.WindowCommand):
	def run(self):
		sublime_project_file = self.window.project_file_name()
		self.window.open_file(sublime_project_file)

		try:
			self.window.open_file(sublime_project_file)
		except TypeError:
			message = "[Open .sublime-project File]: No .sublime-project file found]"
			print(message)
			sublime.status_message(message)
