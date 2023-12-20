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


class GetDiscussionRepliesCount:
    async def get_discussion_replies_count(
        self: "pyromodz.Client",
        chat_id: Union[int, str],
        message_id: int,
    ) -> int:
        """Get the total count of replies in a discussion thread.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Message id.

        Example:
            .. code-block:: python

                count = await app.get_discussion_replies_count(chat_id, message_id)
        """

        r = await self.invoke(
            raw.functions.messages.GetReplies(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                offset_id=0,
                offset_date=0,
                add_offset=0,
                limit=1,
                max_id=0,
                min_id=0,
                hash=0
            )
        )

        return r.count
