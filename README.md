<p align="center">
    <a href="https://github.com/Kaal-xD/pyromodz">
        <img src="https://telegra.ph/file/de7f160cac1894eb51135.png" alt="Pyromodz" width="128">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br>
    <a href="https://github.com/Kaal-xD/pyromodz">
        Homepage
    </a>
    •
    <a href="https://t.me/pyromodzchat">
        Documentation
    </a>
    •
    <a href="https://t.me/pyromodz">
        Releases
    </a>
    •
    <a href="https://t.me/pyromodz">
        News
    </a>
</p>

## Pyromodz

> A fork version elegant, modern and asynchronous Telegram MTProto API framework of [Pyrogram](https://github.com/pyrogram/pyrogram) library in Python for users and bots with [Pyromod](https://github.com/usernein/pyromod) features.


``` python
from pyromodz import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyromodz!")


app.run()
```

**Pyromodz** is a modern, elegant and asynchronous [MTProto API](https://github.com/Kaal-xD/pyromodz)
framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.


### Key Features

- **Ready**: Install Pyromodz with pip and start building your applications right away.
- **Easy**: Makes the Telegram API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by [TgCrypto](https://github.com/pyrogram/tgcrypto), a high-performance cryptography library written in C.  
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Telegram's API to execute any official client action and more.

### Installing

``` bash
pip3 install pyromodz
```

### Resources

- Join the official channel at https://t.me/pyromodz and stay tuned for news, updates and announcements.


### Special Thanks

- [Pyrogram](https://github.com/pyrogram/pyrogram) - Pyrogram is a original library source from which pyromodz was built.

- [Pyromod](https://github.com/usernein/pyromod) - An add-on to make developing Telegram bots faster and more efficient.


