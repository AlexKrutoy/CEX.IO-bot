import random
from enum import Enum


class StaticEmoji(str, Enum):
    ACCEPT = '<emoji id=5206607081334906820>✔️</emoji>'
    DENY = '<emoji id=5210952531676504517>❌</emoji>'
    WARNING = '<emoji id=5447644880824181073>⚠️</emoji>'
    LOUDSPEAKER = '<emoji id=5424818078833715060>📣</emoji>'
    FLAG = '<emoji id=5222444124698853913>🔖</emoji>'
    SCRAP = '<emoji id=5397782960512444700>📌</emoji>'
    ARROW = '<emoji id=5416117059207572332>➡️</emoji>'
    PLUS = '<emoji id=5397916757333654639>➕</emoji>'
    DOLLAR = '<emoji id=5409048419211682843>💵</emoji>'
    START = '<emoji id=5416081784641168838>🟢</emoji>'
    STOP = '<emoji id=5411225014148014586>🔴</emoji>'


def get_random_reaction():
    reactions = [
        "👍", "👎", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴",
        "😍", "🐳", "❤️‍🔥", "🌚", "🌭", "💯", "🤣", "⚡️", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓",
        "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍️", "🤗", "🫡", "🎅", "🎄", "☃️", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄",
        "😘", "💊", "🙊", "😎", "👾", "🤷‍♂️", "🤷", "🤷‍♀️", "😡"
    ]

    return random.choice(reactions)


accept = [
    '<emoji id=5375175408012516662>🌟</emoji>',
    '<emoji id=5377370922279779996>🌟</emoji>',
    '<emoji id=5375163072866432989>🌟</emoji>',
    '<emoji id=5377410002187205490>🌟</emoji>',
    '<emoji id=5375087150729540263>🌟</emoji>',
    '<emoji id=5377790166922442009>🌟</emoji>',
    '<emoji id=5377502816430471486>🌟</emoji>',
    '<emoji id=5375367444590247261>🌟</emoji>',
    '<emoji id=5375598221772996400>🌟</emoji>',
    '<emoji id=5375499540604401121>🌟</emoji>',
    '<emoji id=5375395301748127020>🌟</emoji>',
    '<emoji id=5375357841043371164>🌟</emoji>',
    '<emoji id=5377359437537229623>🌟</emoji>',
    '<emoji id=5375053203308035935>🌟</emoji>',
    '<emoji id=5375188696641321716>🌟</emoji>',
    '<emoji id=5375227888217897673>🌟</emoji>',
    '<emoji id=5375565416812789037>✅</emoji>',
    '<emoji id=5375352888946077785>✅</emoji>',
    '<emoji id=5377728778954881693>✅</emoji>',
    '<emoji id=5375172186787035266>✅</emoji>',
    '<emoji id=5375055724453837637>✅</emoji>',
    '<emoji id=5377850429608574168>✅</emoji>',
    '<emoji id=5375247275700271687>✅</emoji>',
    '<emoji id=5375504222118754078>✅</emoji>',
    '<emoji id=5377740826338145943>✅</emoji>',
    '<emoji id=5375374724559813456>✅</emoji>',
    '<emoji id=5377763795823249705>✅</emoji>',
    '<emoji id=5375157360559930462>✅</emoji>',
    '<emoji id=5375450006746577351>✅</emoji>',
    '<emoji id=5377391104331103107>✅</emoji>',
    '<emoji id=5375300314251410685>✅</emoji>',
    '<emoji id=5447447969458566198>✅</emoji>',
    '<emoji id=5213446125264055603>✅</emoji>',
    '<emoji id=5213292515758713570>✅</emoji>',
    '<emoji id=5215470137192229422>✅</emoji>',
    '<emoji id=5215492745900077682>✅</emoji>',
    '<emoji id=5213406375341731253>✅</emoji>',
    '<emoji id=5213128847439964513>✅</emoji>',
]

deny = [
    "<emoji id=5215204871422093648>❌</emoji>",
    "<emoji id=5212992409213872592>❌</emoji>",
    "<emoji id=5215483816663066751>❌</emoji>",
    "<emoji id=5213460324425935151>❌</emoji>",
    "<emoji id=5215642288071387368>❌</emoji>",
    "<emoji id=5215680783863261658>❌</emoji>",
]

warnings = [
    "<emoji id=5213205860498549992>⚠️</emoji>",
    "<emoji id=5213181173026533794>⚠️</emoji>",
    "<emoji id=5215677343594457295>⚠️</emoji>",
    "<emoji id=5215305227627931680>⚠️</emoji>",
    "<emoji id=5213336479043955543>⚠️</emoji>",
    "<emoji id=5212988801441344587>⚠️</emoji>",
]

nums = {
    0: '<emoji id=5305542129739642017>🔠</emoji>',
    1: '<emoji id=5305481377427240126>🔠</emoji>',
    2: '<emoji id=5305689266729268251>🔠</emoji>',
    3: '<emoji id=5305416115399177518>🔠</emoji>',
    4: '<emoji id=5305637765776422206>🔠</emoji>',
    5: '<emoji id=5303134895059517245>🔠</emoji>',
    6: '<emoji id=5305397569730394749>🔠</emoji>',
    7: '<emoji id=5302991894123394705>🔠</emoji>',
    8: '<emoji id=5303267996096019267>🔠</emoji>',
    9: '<emoji id=5303436071051213525>🔠</emoji>',
}

loads = [
    "<emoji id=5307723788442410997>🫥</emoji>",
    "<emoji id=5307750348520168450>🫥</emoji>",
    "<emoji id=5307736638984559509>🫥</emoji>",
    "<emoji id=5308033876491247752>🫥</emoji>",
    "<emoji id=5305683825005700455>🫥</emoji>",
    "<emoji id=5326006107011816493>🫥</emoji>",
    "<emoji id=5307981757063110606>🫥</emoji>",
    "<emoji id=5307780589384900520>🫥</emoji>",
    "<emoji id=5308017534140685461>🫥</emoji>",
    "<emoji id=5323463142775202324>🫠</emoji>",
    "<emoji id=5307581225592954663>🫥</emoji>",
    "<emoji id=5309799327093236710>🫥</emoji>",
    "<emoji id=5309893756244206277>🫥</emoji>",
    "<emoji id=5327902038720257153>🫥</emoji>",
    "<emoji id=5325919653615115810>🫥</emoji>",
    "<emoji id=5332773291843133224>🫥</emoji>",
    "<emoji id=5334530569122358729>🫥</emoji>",
    "<emoji id=5334885140147479028>🫥</emoji>",
    "<emoji id=5325834523068342417>🫥</emoji>",
    "<emoji id=5334904192622403796>🫥</emoji>",
    "<emoji id=5325534794480624559>😵</emoji>",
    "<emoji id=5307646968657356266>‍</emoji>",
    "<emoji id=5327840856911125897>💫</emoji>",
    "<emoji id=5334643333488713810>🫥</emoji>",
]


def rload():
    return random.choice(loads)


def rcheck():
    return random.choice(accept)


def rdeny():
    return random.choice(deny)


def rwarning():
    return random.choice(warnings)


def num(n):
    return nums[int(n)]
