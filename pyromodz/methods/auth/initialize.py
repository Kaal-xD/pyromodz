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

import asyncio
import logging

import pyromodz

log = logging.getLogger(__name__)


class Initialize:
    async def initialize(
        self: "pyromodz.Client",
    ):
        """Initialize the client by starting up workers.

        This method will start updates and download workers.
        It will also load plugins and start the internal dispatcher.

        Raises:
            ConnectionError: In case you try to initialize a disconnected client or in case you try to initialize an
                already initialized client.
        """
        if not self.is_connected:
            raise ConnectionError("Can't initialize a disconnected client")

        if self.is_initialized:
            raise ConnectionError("Client is already initialized")

        self.load_plugins()

        await self.dispatcher.start()

        self.updates_watchdog_task = asyncio.create_task(self.updates_watchdog())

        self.is_initialized = True
