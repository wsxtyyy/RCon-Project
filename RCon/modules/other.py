from vkbottle.bot import BotLabeler, Message
from sys import platform

import TtoS

other_labeler = BotLabeler()
other_labeler.vbml_ignore_case = True


update = '0.5.0.2'
txt = TtoS.Image()

@other_labeler.message(text='update')
async def help_cmd(message: Message):
    try:
        await message.answer(
            message=f"Project: https://vk.com/ping_deep/ \n* Update: {update} \n* Platform: {platform} \n\n {txt.output('sxtyyy', 'made_by')}")

    except Exception as e:
        await message.reply('⚠ / Произошла ошибка, код ошибки: {0}'.format(e))
