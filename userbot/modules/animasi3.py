from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.feri(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Feri`")
    sleep(3)
    await typew.edit("`17 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Trenggalek, Salam Kenal:)`")

@register(outgoing=True, pattern='^.dante(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Dante`")
    sleep(3)
    await typew.edit("`16 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di pulau seribu, Salam Kenal:)`")



@register(outgoing=True, pattern='^ilyu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")


@register(outgoing=True, pattern='^.pe(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Bapaknya Udin Di Makan Udang`")
    sleep(2)
    await typew.edit("`Cuma Sendiri nih Senggol Dong`")


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Awali perkataan dengan dengan salam`")
    sleep(1)
    await typew.edit("`Assalamualaikum Asuuuu`")


CMD_HELP.update({
    "animasi3":
    "CMD`.pe`\
\nPenjelasan: Cek lah asw.\
\n\nCMD:`.feri`\
\nPenjelasan: Cek lah asw.\
\n\nCMD:`.ilyu`\
\nPenjelasan: Cek lah asw.\
\n\nCMD:`p`\
\nPenjelasan: Cek lah asw.\
\n\nCMD:`.semangat`\
\nPenjelasan: Cek lah asw."
})
