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

import pyromodz
from pyromodz.parser.html import HTML


# expected: the expected unparsed HTML
# text: original text without entities
# entities: message entities coming from the server

def test_html_unparse_bold():
    expected = "<b>bold</b>"
    text = "bold"
    entities = pyromodz.types.List(
        [pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.BOLD, offset=0, length=4)])

    assert HTML.unparse(text=text, entities=entities) == expected


def test_html_unparse_italic():
    expected = "<i>italic</i>"
    text = "italic"
    entities = pyromodz.types.List(
        [pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.ITALIC, offset=0, length=6)])

    assert HTML.unparse(text=text, entities=entities) == expected


def test_html_unparse_underline():
    expected = "<u>underline</u>"
    text = "underline"
    entities = pyromodz.types.List(
        [pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.UNDERLINE, offset=0, length=9)])

    assert HTML.unparse(text=text, entities=entities) == expected


def test_html_unparse_strike():
    expected = "<s>strike</s>"
    text = "strike"
    entities = pyromodz.types.List(
        [pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.STRIKETHROUGH, offset=0, length=6)])

    assert HTML.unparse(text=text, entities=entities) == expected


def test_html_unparse_spoiler():
    expected = "<spoiler>spoiler</spoiler>"
    text = "spoiler"
    entities = pyromodz.types.List(
        [pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.SPOILER, offset=0, length=7)])

    assert HTML.unparse(text=text, entities=entities) == expected


def test_html_unparse_url():
    expected = '<a href="https://pyromodz.org/">URL</a>'
    text = "URL"
    entities = pyromodz.types.List([pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.TEXT_LINK,
                                                                 offset=0, length=3, url='https://pyromodz.org/')])

    assert HTML.unparse(text=text, entities=entities) == expected


def test_html_unparse_code():
    expected = '<code>code</code>'
    text = "code"
    entities = pyromodz.types.List(
        [pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.CODE, offset=0, length=4)])

    assert HTML.unparse(text=text, entities=entities) == expected


def test_html_unparse_pre():
    expected = """<pre language="python">for i in range(10):
    print(i)</pre>"""

    text = """for i in range(10):
    print(i)"""

    entities = pyromodz.types.List([pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.PRE, offset=0,
                                                                 length=32, language='python')])

    assert HTML.unparse(text=text, entities=entities) == expected


def test_html_unparse_mixed():
    expected = "<b>aaaaaaa<i>aaa<u>bbbb</u></i></b><u><i>bbbbbbccc</i></u><u>ccccccc<s>ddd</s></u><s>ddddd<spoiler>dd" \
               "eee</spoiler></s><spoiler>eeeeeeefff</spoiler>ffff<code>fffggggggg</code>ggghhhhhhhhhh"
    text = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhh"
    entities = pyromodz.types.List(
        [pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.BOLD, offset=0, length=14),
         pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.ITALIC, offset=7, length=7),
         pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.UNDERLINE, offset=10, length=4),
         pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.UNDERLINE, offset=14, length=9),
         pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.ITALIC, offset=14, length=9),
         pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.UNDERLINE, offset=23, length=10),
         pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.STRIKETHROUGH, offset=30, length=3),
         pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.STRIKETHROUGH, offset=33, length=10),
         pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.SPOILER, offset=38, length=5),
         pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.SPOILER, offset=43, length=10),
         pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.CODE, offset=57, length=10)])

    assert HTML.unparse(text=text, entities=entities) == expected


def test_html_unparse_escaped():
    expected = "<b>&lt;b&gt;bold&lt;/b&gt;</b>"
    text = "<b>bold</b>"
    entities = pyromodz.types.List(
        [pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.BOLD, offset=0, length=11)])

    assert HTML.unparse(text=text, entities=entities) == expected


def test_html_unparse_escaped_nested():
    expected = "<b>&lt;b&gt;bold <u>&lt;u&gt;underline&lt;/u&gt;</u> bold&lt;/b&gt;</b>"
    text = "<b>bold <u>underline</u> bold</b>"
    entities = pyromodz.types.List(
        [pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.BOLD, offset=0, length=33),
         pyromodz.types.MessageEntity(type=pyromodz.enums.MessageEntityType.UNDERLINE, offset=8, length=16)])

    assert HTML.unparse(text=text, entities=entities) == expected


def test_html_unparse_no_entities():
    expected = "text"
    text = "text"
    entities = []

    assert HTML.unparse(text=text, entities=entities) == expected
