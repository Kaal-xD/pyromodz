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

from uuid import uuid4

import pyromodz
from pyromodz import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~pyromodz.types.InlineQueryResultCachedAudio`
    - :obj:`~pyromodz.types.InlineQueryResultCachedDocument`
    - :obj:`~pyromodz.types.InlineQueryResultCachedAnimation`
    - :obj:`~pyromodz.types.InlineQueryResultCachedPhoto`
    - :obj:`~pyromodz.types.InlineQueryResultCachedSticker`
    - :obj:`~pyromodz.types.InlineQueryResultCachedVideo`
    - :obj:`~pyromodz.types.InlineQueryResultCachedVoice`
    - :obj:`~pyromodz.types.InlineQueryResultArticle`
    - :obj:`~pyromodz.types.InlineQueryResultAudio`
    - :obj:`~pyromodz.types.InlineQueryResultContact`
    - :obj:`~pyromodz.types.InlineQueryResultDocument`
    - :obj:`~pyromodz.types.InlineQueryResultAnimation`
    - :obj:`~pyromodz.types.InlineQueryResultLocation`
    - :obj:`~pyromodz.types.InlineQueryResultPhoto`
    - :obj:`~pyromodz.types.InlineQueryResultVenue`
    - :obj:`~pyromodz.types.InlineQueryResultVideo`
    - :obj:`~pyromodz.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "pyromodz.Client"):
        pass
