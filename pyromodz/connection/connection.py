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
from typing import Optional
from .transport import TCP, TCPAbridged
from ..session.internals import DataCenter

log = logging.getLogger(__name__)

class Connection:
    MAX_CONNECTION_ATTEMPTS = 3

    def __init__(self, dc_id: int, test_mode: bool, ipv6: bool, proxy: dict, media: bool = False):
        """
        Initialize Connection object.

        Parameters:
        - dc_id: Data center ID
        - test_mode: Boolean indicating test mode
        - ipv6: Boolean indicating IPv6 usage
        - proxy: Dictionary containing proxy details
        - media: Boolean indicating media usage
        """
        self.dc_id = dc_id
        self.test_mode = test_mode
        self.ipv6 = ipv6
        self.proxy = proxy
        self.media = media
        self.address = DataCenter(dc_id, test_mode, ipv6, media)
        self.protocol: TCP = None

    async def connect(self):
        """
        Attempt to establish a connection with the specified parameters.
        """
        for i in range(Connection.MAX_CONNECTION_ATTEMPTS):
            self.protocol = TCPAbridged(self.ipv6, self.proxy)

            try:
                log.info("Connecting...")
                await self.protocol.connect(self.address)
            except OSError as e:
                log.warning("Unable to connect due to network issues: %s", e)
                await self.protocol.close()
                await asyncio.sleep(1)
            else:
                log.info("Connected! %s DC%s%s - IPv%s",
                         "Test" if self.test_mode else "Production",
                         self.dc_id,
                         " (media)" if self.media else "",
                         "6" if self.ipv6 else "4")
                break
        else:
            log.warning("Connection failed after multiple attempts.")
            raise ConnectionError("Unable to establish connection after multiple attempts.")

    async def close(self):
        """
        Close the connection.
        """
        await self.protocol.close()
        log.info("Disconnected")

    async def send(self, data: bytes):
        """
        Send data over the connection.

        Parameters:
        - data: Bytes to be sent.
        """
        await self.protocol.send(data)

    async def recv(self) -> Optional[bytes]:
        """
        Receive data from the connection.

        Returns:
        - Optional bytes received.
        """
        return await self.protocol.recv()
