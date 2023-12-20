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

from typing import Union

import pyromodz
from pyromodz import raw


class GetChatPhotosCount:
    async def get_chat_photos_count(
        self: "pyromodz.Client",
        chat_id: Union[int, str]
    ) -> int:
        """Get the total count of photos for a chat.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``int``: On success, the user profile photos count is returned.

        Example:
            .. code-block:: python

                count = await app.get_chat_photos_count("me")
                print(count)
        """

        peer_id = await self.resolve_peer(chat_id)

        if isinstance(peer_id, raw.types.InputPeerChannel):
            r = await self.invoke(
                raw.functions.messages.GetSearchCounters(
                    peer=peer_id,
                    filters=[raw.types.InputMessagesFilterChatPhotos()],
                )
            )

            return r[0].count
        else:
            r = await self.invoke(
                raw.functions.photos.GetUserPhotos(
                    user_id=peer_id,
                    offset=0,
                    max_id=0,
                    limit=1
                )
            )

            if isinstance(r, raw.types.photos.Photos):
                return len(r.photos)
            else:
                return r.count
