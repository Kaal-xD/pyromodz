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


from .client import Client
from ..types.user_and_chats.chat import Chat as PyroChat
from ..utilities import should_patch, patch_into


@patch_into(PyroChat)
class Chat(PyroChat):
    _client: Client

    @should_patch()
    def listen(self, *args, **kwargs):
        return self._client.listen(*args, chat_id=self.id, **kwargs)

    @should_patch()
    def ask(self, text, *args, **kwargs):
        return self._client.ask(self.id, text, *args, **kwargs)

    @should_patch()
    def stop_listening(self, *args, **kwargs):
        return self._client.stop_listening(*args, chat_id=self.id, **kwargs)
