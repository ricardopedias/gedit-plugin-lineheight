# Incrementa os espaços entre as linhas no editor
# Copyright: Copyright (C) 2020 Ricardo Pereira
# Website: https://github.com/ricardopedias/gedit-plugin-lineheight

from gi.repository import GObject, Gtk, Gedit

class LineSpacing(GObject.Object, Gedit.ViewActivatable):
    __gtype_name__ = "LineSpacing"
    view = GObject.property(type=Gedit.View)
    pixels = 5 # <<-- mude para ajustar as entrelinhas (o padrão é 0)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        if self.view:
            self.view.set_pixels_below_lines(self.pixels)

    def do_deactivate(self):
        if self.view:
            self.view.set_pixels_below_lines(0)
