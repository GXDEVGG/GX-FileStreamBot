# This file is a part of TG-FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


class Language(object):
    def __new__ (self, message: Message):
        if getattr(message.from_user, 'language_code', 'Unknown') in self.available:
            return getattr(self, getattr(message.from_user, 'language_code', self.en), self.en)
        else:
            return self.en

    available=['en', 'Test']

    class en(object):
        START_TEXT = """
<i>👋 Olá,</i>{}\n
<i>Eu sou o Bot Gerenciamento Conteúdos</i>\n
<i>Clique em ( Suporte ) para entrar em contato com o desenvolvedor. - GX</i>\n\n"""

        HELP_TEXT = """
<i>- Envie-me qualquer arquivo (ou) Mídia do telegram</i>
<i>- Fornecerei um link externo de download direto!.</i>
<i>- Link de download com velocidade mais rápida</i>
<u>🔸 AVISO!! 🚸</u>\n
<i>Contactar o Programador ( ou ) Comunicar erros</i> <b>: <a href='https://t.me/gilderlanxavier'>[ CLIQUE AQUI ]</a></b>"""

        ABOUT_TEXT = """
<b>Gerenciador de Conteúdos</b>\n
<b>🔸 Versão: 3.0.3.2</b>\n
<b>🔹 Fork de Atualização: By GX - <a href='https://t.me/gilderlanxavier'>[ CLIQUE AQUI ]</a></b>
"""

        stream_msg_text ="""
<i><u>Obaa! Seu link foi gerado:</u></i>\n
<b>📂 Nome do Arquivo:</b> <i>{}</i>\n
<b>📦 Tamanho do Arquivo:</b> <i>{}</i>\n
<b>📥 Download:</b> <i>{}</i>\n
<b>▶️ Assistir:</b> <i>{}</i>"""

    class Test(object):
        START_TEXT = """
<i>👋 Olá,</i>{}\n
<i>Eu sou o Bot Gerenciamentos de Conteúdos</i>\n
<i>Clique em Suporte para entrar em contato com o desenvolvedor. - GX - <a href='https://t.me/gilderlanxavier'>[ CLIQUE AQUI PARA ENTRAR EM CONTATO ]</a></i>\n\n"""

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Suporte', callback_data='help'),
        InlineKeyboardButton('Sobre', callback_data='about'),
        InlineKeyboardButton('Fechar', callback_data='close')
        ],
        [InlineKeyboardButton("📢 Canal de Logs", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Inicio', callback_data='home'),
        InlineKeyboardButton('Sobre', callback_data='about'),
        InlineKeyboardButton('Fechar', callback_data='close'),
        ],
        [InlineKeyboardButton("📢 Canal de Logs", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Inicio', callback_data='home'),
        InlineKeyboardButton('Suporte', callback_data='help'),
        InlineKeyboardButton('Fechar', callback_data='close'),
        ],
        [InlineKeyboardButton("📢 Canal de Logs", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
