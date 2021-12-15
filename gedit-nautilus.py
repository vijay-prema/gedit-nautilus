# Text Editor Nautilus Extension
# Right click on any file(s) and open in a text editor
# Default Gedit, configure TEXTEDITOR below
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script was written by vijay-prema and is released to the public domain

from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to vscode
TEXTEDITOR = 'gedit'

# what name do you want to see in the context menu?
EDITORNAME = 'Text Editor'

class TextEditorExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_editor(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

        call(TEXTEDITOR + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, window, files):
        item = Nautilus.MenuItem(
            name='TextEditorOpen',
            label='Open in ' + EDITORNAME,
            tip='Opens the selected files with Text Editor'
        )
        item.connect('activate', self.launch_editor, files)

        return [item]

