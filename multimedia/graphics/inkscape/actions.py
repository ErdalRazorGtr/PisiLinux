#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf('-vfi')
    autotools.configure("--prefix=/usr \
                         --enable-lcms \
                         --enable-poppler-cairo \
                         --disable-dependency-tracking \
                         --with-python \
                         --with-perl")
    pisitools.dosed("src/widgets/desktop-widget.h", "commands_toolbox,", "commands_toolbox")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LIB", "ChangeLog", "NEWS", "README")
