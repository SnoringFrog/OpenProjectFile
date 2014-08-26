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

#If empty, fill out basic shell?

#Find good keyboard shortcut for this

#Also find .sublime-workspace file?

"""
{
    "folders":
    [
        {
            "path": "src",
            "folder_exclude_patterns": ["backup"]
        },
        {
            "path": "docs",
            "name": "Documentation",
            "file_exclude_patterns": ["*.css"]
        }
    ],
    "settings":
    {
        "tab_size": 8
    },
    "build_systems":
    [
        {
            "name": "List",
            "cmd": ["ls"]
        }
    ]
}
"""