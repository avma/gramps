#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2003  Donald N. Allingham
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id$

"Names with SoundEx code of ..."

import Filter
import soundex
from gettext import gettext as _

class MatchSndEx2(Filter.Filter):
    "Names with SoundEx code of ..."

    def match(self,person):
        return self.text == soundex.soundex(person.getPrimaryName().getSurname())

#------------------------------------------------------------------------
#
# 
#
#------------------------------------------------------------------------
Filter.register_filter(MatchSndEx2,
                       description=_("Names with the SoundEx code of ..."),
                       label=_("SoundEx Code"),
                       qualifier=1)
