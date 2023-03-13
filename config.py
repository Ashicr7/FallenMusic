from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID:28571363)
API_HASH = getenv("API_HASH:0b9abfb7079d5208107c9768ce50bd0a)

BOT_TOKEN = getenv("BOT_TOKEN",5520373776:AAGwPsIO_7p31D4KUcp26bJX83y8LqRH0gY)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID:5489580104))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION"1BVtsOHUBu5IDTiSlAl66wqLtBG1_roqKqB0CiiWZt327TGtoi17DIvfO3QPyrpp1Sq2v6bgY26kGwrjO6cJFn4hXVvHn_jyhzBTrwkcBBQ4sx0ya-bVcG8-yFMJ13TWQF5VCvAfT9-_x2md7siPa8EGQKGa1mAmYolH4bYVT5p2RjSK-WC7-5lLiEaIwy2aFfpHLg6gtj8FOBDiwmkJAOpjsLRdm5EBMI7ea0DwAVxWx1vOuVd2rwUynQ1Y0bnly0YhAcKYolv-fUo8gYNe3Kk_3ZGgCR5UCaNvOehzWieZR55EjGwkjdzR559abH8P4lxK4s5BHzdU2lqJksUXVNRzpImfD52I=
)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
