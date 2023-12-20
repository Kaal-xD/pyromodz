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

from typing import List
from typing import Optional
from typing import Union

import pyromodz
from pyromodz import raw
from pyromodz import types


class GetSimilarChannels:
    async def get_similar_channels(
        self: "pyromodz.Client",
        chat_id: Union[int, str]
    ) -> Optional[List["types.Chat"]]:
        """Get similar channels.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            List of :obj:`~pyromodz.types.Chat`: On success, the list of channels is returned.

        Example:
            .. code-block:: python

                channels = await app.get_similar_channels(chat_id)
                print(channels)
        """
        chat = await self.resolve_peer(chat_id)

        if isinstance(chat, raw.types.InputPeerChannel):
            r = await self.invoke(
                raw.functions.channels.GetChannelRecommendations(
                    channel=chat
                )
            )

            return types.List([types.Chat._parse_channel_chat(self, chat) for chat in r.chats]) or None
        else:
            raise ValueError(f'The chat_id "{chat_id}" belongs to a user or chat')
