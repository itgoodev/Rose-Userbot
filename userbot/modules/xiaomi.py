# created by @eve_enryu

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern="^.firmware(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    firmware = "firmware"
    await event.edit("`Memproses...`")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{firmware} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("✖️ `Maaf {ALIVE_NAME} Kamu Sudah Menghapus Bot @XiaomiGeeksBot , Buka Kembali Bot Nya !`")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.fastboot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    fboot = "fastboot"
    await event.edit("`Memproses...`")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{fboot} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("✖️ `Maaf {ALIVE_NAME} Kamu Sudah Menghapus Bot @XiaomiGeeksBot , Buka Kembali Bot Nya !`")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.recovery(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    recovery = "recovery"
    await event.edit("`Memproses...`")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{recovery} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("✖️ `Maaf {ALIVE_NAME} Kamu Sudah Menghapus Bot @XiaomiGeeksBot , Buka Kembali Bot Nya !`")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.pb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pitch = "pb"
    await event.edit("`Memproses...`")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{pitch} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("✖️ `Maaf {ALIVE_NAME} Kamu Sudah Menghapus Bot @XiaomiGeeksBot , Buka Kembali Bot Nya !`")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.of(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ofox = "of"
    await event.edit("`Memproses...`")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{ofox} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("✖️ `Maaf {ALIVE_NAME} Kamu Sudah Menghapus Bot @XiaomiGeeksBot , Buka Kembali Bot Nya !`")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.eu(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    eu = "eu"
    await event.edit("`Memproses...`")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{eu} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("✖️ `Maaf {ALIVE_NAME} Kamu Sudah Menghapus Bot @XiaomiGeeksBot , Buka Kembali Bot Nya !`")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.vendor(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    vendor = "vendor"
    await event.edit("`Memproses...`")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{vendor} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("✖️ `Maaf {ALIVE_NAME} Kamu Sudah Menghapus Bot @XiaomiGeeksBot , Buka Kembali Bot Nya !`")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.specs(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    specs = "specs"
    await event.edit("`Memproses...`")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{specs} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("✖️ `Maaf {ALIVE_NAME} Kamu Sudah Menghapus Bot @XiaomiGeeksBot , Buka Kembali Bot Nya !`")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


CMD_HELP.update(
    {
        "xiaomi": "**✘ Plugin** `xiaomi` :\
        \n\n  •  **Perintah :** `.firmware` [**Nama Kode**]\
        \n  •  **Fungsi : **Dapatkan Firmware terbaru.\
        \n\n  •  **Perintah :** `.pb` [**Nama Kode**]\
        \n  •  **Fungsi : **Dapatkan Pemulihan PitchBlack terbaru.\
        \n\n  •  **Perintah :** `.specs` [**Nama Kode**]\
        \n  •  **Fungsi : **Dapatkan informasi spesifikasi cepat tentang perangkat.\
        \n\n  •  **Perintah :** `.fastboot` [**Nama Kode**]\
        \n  •  **Fungsi : **Dapatkan MIUI fastboot terbaru.\
        \n\n  •  **Perintah :** `.recovery` [**Nama Kode**]\
        \n  •  **Fungsi : **Dapatkan MIUI pemulihan terbaru.\
        \n\n  •  **Perintah :** `.eu` [**Nama Kode**]\
        \n  •  **Fungsi : **Dapatka n rom xi aomi.eu terbaru.\
        \n\n  • ** Perintah: ** `.vendor` [**Nama Kode**]\
        \n  • ** Fungsi: **Mengambil Vendor Terbaru.\
        \n\n  • ** Perintah: ** `.of` [**Nama Kode**]\
        \n  • ** Fungsi: **Dapatkan Pemulihan ORangeFox terbaru.\
        "
    }
)
