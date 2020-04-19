#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# COPYRIGHT (C) 2016-2017 Michael Labouebe <gfarmerfr@free.fr>
# COPYRIGHT (C) 2009-2010 Quinox <quinox@users.sf.net>
# COPYRIGHT (C) 2009 Hedonist <ak@sensi.org>
# COPYRIGHT (C) 2006-2009 Daelstorm <daelstorm@gmail.com>
# COPYRIGHT (C) 2008-2009 eL_vErDe <gandalf@le-vert.net>
#
# GNU GENERAL PUBLIC LICENSE
#    Version 3, 29 June 2007
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
    To install Nicotine+ on a GNU/Linux distribution run:
    sudo python setup.py install
"""

import sys
import os

from os.path import join

ICON_SIZES = ('16x16', '32x32', '48x48', '64x64', '96x96')
LANGUAGES = ('da', 'de', 'es', 'fi', 'fr', 'hu', 'it', 'lt', 'nl', 'pl', 'pt_BR', 'sk', 'sv')


def install(src, dest):
    for path, dirs, files in os.walk(src):
        print(f'install -d {join(sys.prefix, dest, path)}')
        for f in files:
            print(f'install {join(path, f)} {join(sys.prefix, dest, path)}')


install('doc', 'share/doc/nicotine')

install('manpages', 'share/man/man1')

for size in ICON_SIZES:
    install(f'files/icons/{size}', f'share/icons/hicolor/{size}/apps')

install('files/icons/scalable', 'share/icons/hicolor/scalable/apps')

install('files/nicotine.desktop', 'share/applications')

for lang in LANGUAGES:
    install(f'languages/{lang}', f'share/locale')

install('sounds', 'share/nicotine')
