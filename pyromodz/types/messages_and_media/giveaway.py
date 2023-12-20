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

from datetime import datetime
from typing import List

import pyromodz
from pyromodz import raw
from pyromodz import types
from pyromodz import utils
from ..object import Object


class Giveaway(Object):
    """A Giveaway.

    Parameters:
        channels (List of :obj:`~pyromodz.types.Chat`):
            Get the list of channels you need to subscribe to.

        quantity (``int``):
            Number of subscriptions.

        months (``int``):
            Number of months for which a subscription is given.

        until_date (:py:obj:`~datetime.datetime`):
            Date when the giveaway will end.

        only_new_subscribers (``bool``):
            True if the giveaway is for new subscribers only.

        only_for_countries (List of ``str``, *optional*):
            Countries for which the giveaway is available in iso2 format.
    """

    def __init__(
            self,
            *,
            client: "pyromodz.Client" = None,
            channels: List["types.Chat"] = None,
            quantity: int = None,
            months: int = None,
            until_date: datetime = None,
            only_new_subscribers: bool = None,
            only_for_countries: List[str] = None
    ):
        super().__init__(client)

        self.channels = channels
        self.quantity = quantity
        self.months = months
        self.until_date = until_date
        self.only_new_subscribers = only_new_subscribers
        self.only_for_countries = only_for_countries

    @staticmethod
    def _parse(
            client,
            giveaway: "raw.types.MessageMediaGiveaway",
            channels: dict
    ) -> "Giveaway":
        return Giveaway(
            channels=types.List(types.Chat._parse_channel_chat(client, channels.get(i)) for i in giveaway.channels),
            quantity=giveaway.quantity,
            months=giveaway.months,
            until_date=utils.timestamp_to_datetime(giveaway.until_date),
            only_new_subscribers=giveaway.only_new_subscribers,
            only_for_countries=types.List(giveaway.countries_iso2) or None,
            client=client
        )
