#  Pyromodz - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-2022 Kaal-xD <https://github.com/Kaal-xD>
#
#  This file is part of Pyromodz.
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


class SetChatReaction:
    async def set_chat_reactions(
            self: "pyromodz.Client",
            chat_id: Union[int, str],
            available_reactions: list
    ) -> bool:
        """Set the default emoji to use in chat.

        Use :meth:`~pyromodz.Client.set_chat_reactions` to set one or more emoji for the chat to react to messages..

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            available_reactions: List of ``str``

        Returns:
            ``bool``: On success, true is returned

        Example:
            .. code-block:: python

                app.set_chat_reactions(chat_id, [❤️, 👍])
        """
        try:
            await self.invoke(
                raw.functions.messages.SetChatAvailableReactions(
                    peer=await self.resolve_peer(chat_id),
                    available_reactions=available_reactions,
                )
            )
        except Exception:
            return False
