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
from pyromodz import raw, utils


class SendInlineBotResult:
    async def send_inline_bot_result(
        self: "pyromodz.Client",
        chat_id: Union[int, str],
        query_id: int,
        result_id: str,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        message_thread_id: int = None,
        partial_reply: str = None
    ) -> "raw.base.Updates":
        """Send an inline bot result.
        Bot results can be retrieved using :meth:`~pyromodz.Client.get_inline_bot_results`

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            query_id (``int``):
                Unique identifier for the answered query.

            result_id (``str``):
                Unique identifier for the result that was chosen.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            reply_to_message_id (``int``, *optional*):
                If the message is a reply, ID of the original message.

            message_thread_id (``int``, *optional*):
                If the message is in a thread, ID of the original message.
            partial_reply (``str``, *optional*):
                Text to quote.
                for reply_to_message only.

        Returns:
            :obj:`~pyromodz.raw.base.Updates`: Currently, on success, a raw result is returned.

        Example:
            .. code-block:: python

                await app.send_inline_bot_result(chat_id, query_id, result_id)
        """

        reply_to = utils.get_reply_head_fm(message_thread_id, reply_to_message_id, partial_reply)

        return await self.invoke(
            raw.functions.messages.SendInlineBotResult(
                peer=await self.resolve_peer(chat_id),
                query_id=query_id,
                id=result_id,
                random_id=self.rnd_id(),
                silent=disable_notification or None,
                reply_to=reply_to
            )
        )
