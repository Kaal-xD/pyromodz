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

from typing import Union, Optional

import pyromodz
from pyromodz import raw


class SetSlowMode:
    async def set_slow_mode(
        self: "pyromodz.Client",
        chat_id: Union[int, str],
        seconds: Optional[int]
    ) -> bool:
        """Set the slow mode interval for a chat.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            seconds (``int`` | ``None``):
                Seconds in which members will be able to send only one message per this interval.
                Valid values are: 0 or None (off), 10, 30, 60 (1m), 300 (5m), 900 (15m) or 3600 (1h).

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Set slow mode to 60 seconds
                await app.set_slow_mode(chat_id, 60)

                # Disable slow mode
                await app.set_slow_mode(chat_id, None)
        """

        await self.invoke(
            raw.functions.channels.ToggleSlowMode(
                channel=await self.resolve_peer(chat_id),
                seconds=seconds or 0
            )
        )

        return True
