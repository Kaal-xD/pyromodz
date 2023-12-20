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

from datetime import datetime

from pyromodz import raw, utils
from pyromodz import types
from ..object import Object


class InviteLinkImporter(Object):
    """The date and user of when someone has joined with an invite link.

    Parameters:
        date (:py:obj:`~datetime.datetime`):
            The time of when this user used the given link

        user (:obj:`~pyromodz.types.User`):
            The user that has used the given invite link
    """

    def __init__(
        self, *,
        date: datetime,
        user: "types.User"
    ):
        super().__init__(None)

        self.date = date
        self.user = user

    @staticmethod
    def _parse(client, invite_importers: "raw.types.messages.ChatInviteImporters"):
        importers = types.List()

        d = {i.id: i for i in invite_importers.users}

        for j in invite_importers.importers:
            importers.append(
                InviteLinkImporter(
                    date=utils.timestamp_to_datetime(j.date),
                    user=types.User._parse(client=None, user=d[j.user_id])
                )
            )

        return importers
