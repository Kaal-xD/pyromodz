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

import logging

import pyromodz
from pyromodz import raw
from pyromodz import types

log = logging.getLogger(__name__)


class RecoverPassword:
    async def recover_password(
        self: "pyromodz.Client",
        recovery_code: str
    ) -> "types.User":
        """Recover your password with a recovery code and log in.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            recovery_code (``str``):
                The recovery code sent via email.

        Returns:
            :obj:`~pyromodz.types.User`: On success, the authorized user is returned and the Two-Step Verification
            password reset.

        Raises:
            BadRequest: In case the recovery code is invalid.
        """
        r = await self.invoke(
            raw.functions.auth.RecoverPassword(
                code=recovery_code
            )
        )

        await self.storage.user_id(r.user.id)
        await self.storage.is_bot(False)

        return types.User._parse(self, r.user)
