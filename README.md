# gedit-nautilus

Right click on any file(s) and open in a Text Editor (gedit).

Adds an "Open in Text Editor" item to the Nautilus context menu, for all files.

The `TEXTEDITOR` variable can be changed in the script to support other editors

## Requirements

You must have the `python-nautilus` package installed

For Ubuntu:

```bash
sudo apt install python-nautilus
```

## Installation

1. Place gedit-nautilus.py in ~/.local/share/nautilus-python/extensions/

2. Restart Nautilus

```bash
pkill nautilus
```
