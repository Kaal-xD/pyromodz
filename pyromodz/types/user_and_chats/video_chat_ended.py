#  Pyromodz - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024- Kaal-xD <https://github.com/Kaal-xD>
#
#  Pyromodz is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyromodz is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyromodz.  If not, see <http://www.gnu.org/licenses/>.

from pyromodz import raw
from ..object import Object


class VideoChatEnded(Object):
    """A service message about a voice chat ended in the chat.

    Parameters:
        duration (``int``):
            Voice chat duration; in seconds.
    """

    def __init__(
        self, *,
        duration: int
    ):
        super().__init__()

        self.duration = duration

    @staticmethod
    def _parse(action: "raw.types.MessageActionGroupCall") -> "VideoChatEnded":
        return VideoChatEnded(duration=action.duration)
