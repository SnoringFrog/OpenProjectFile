**_Update_**: Turns out this plugin is mostly overkill (I had a feeling it should be, but I couldn't find the options I needed)

So, rather than install this plugin, you can just set up the following keyboard shortcut/menu entry/command palette entry:

**Keyboard Shortcut** (.sublime-keymap):
```json
{
  "keys":["alt+shift+p"], 
  "command": "open_file", 
  "args":{"file": "${project}"}"
  }
```

**Menu Entry** (.sublime-menu; I added mine to the bottom of the `Project` toolbar entry): 
```json
{
  "caption": "Open Project File", 
  "command": "open_file",
  "args": {"file": "${project}"} 
}
```

**Command Palette Entry** (.sublime-commands):
```json
{
  "caption": "Project: Open .sublime-project File", 
  "command": "open_file",
  "args": {"file": "${project}"} 
}
```

Pretty much the only thing you'll gain from using my plugin is the fact that the shortcut key combo will be visible in the toolbar menu item and that you'll be able to access this from the Command Palette. Other than that, it just saves you the time of making these modifications yourself. 

******************************************************


Open Current .sublime-project File
==================================

This plugin provides a quick way to accesss the .sublime-project file of the current Sublime project. Simply open a Sublime project and use the keyboard shortcut (`Alt+Shift+P`) or via toolbar option in the `Project` menu to open the associated .sublime-project file for opening. This makes it easy to set up project-specific settings and the like. 
