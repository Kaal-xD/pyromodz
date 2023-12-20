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
from typing import List

import pyromodz
from .idle import idle


async def compose(
    clients: List["pyromodz.Client"],
    sequential: bool = False
):
    """Run multiple clients at once.

    This method can be used to run multiple clients at once and can be found directly in the ``pyromodz`` package.

    If you want to run a single client, you can use Client's bound method :meth:`~pyromodz.Client.run`.

    Parameters:
        clients (List of :obj:`~pyromodz.Client`):
            A list of client objects to run.

        sequential (``bool``, *optional*):
            Pass True to run clients sequentially.
            Defaults to False (run clients concurrently)

    Example:
        .. code-block:: python

            import asyncio
            from pyromodz import Client, compose


            async def main():
                apps = [
                    Client("account1"),
                    Client("account2"),
                    Client("account3")
                ]

                ...

                await compose(apps)


            asyncio.run(main())

    """
    if sequential:
        for c in clients:
            await c.start()
    else:
        await asyncio.gather(*[c.start() for c in clients])

    await idle()

    if sequential:
        for c in clients:
            await c.stop()
    else:
        await asyncio.gather(*[c.stop() for c in clients])
