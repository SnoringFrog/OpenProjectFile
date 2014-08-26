Open Current .sublime-project File
==================================

This plugin provides a quick way to accesss the .sublime-project file of the current Sublime project. Simply open a Sublime project and use the keyboard shortcut (`Alt+Shift+P`) or via toolbar option in the `Project` menu to open the associated .sublime-project file for opening. This makes it easy to set up project-specific settings and the like. 

******************************************************

**_Update_**: Turns out this plugin is mostly overkill. You can add these three snippets to the proper files in `[Sublime installation]/Packages/User/` to get the keyboard shortcut, toolbar menu entry, and command palette entry that my plugin provides. Pretty much the only benefit of using my plugin is that these three things will get set up for you automatically and all of the settings get collected into their own directory.

**Keyboard Shortcut** (Default.sublime-keymap):
```json
{
  "keys":["alt+shift+p"], 
  "command": "open_file", 
  "args":{"file": "${project}"}
}
```

**Menu Entry** (Main.sublime-menu; I added mine to the bottom of the `Project` toolbar entry): 
```json
{
  "caption": "Open Project File", 
  "command": "open_file",
  "args": {"file": "${project}"} 
}
```

**Command Palette Entry** (Default.sublime-commands):
```json
{
  "caption": "Project: Open .sublime-project File", 
  "command": "open_file",
  "args": {"file": "${project}"} 
}
```


