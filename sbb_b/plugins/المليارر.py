from sbb_b import sbb_b
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
import asyncio
from telethon import events
c = requests.session()
bot_username = '@xnsex21bot'
tepthon = ['yes']


@sbb_b.ar_cmd(admin_cmd(pattern="(تحمع ع |تجمع)"))
async def _(event):
    if tepthon[0] == "yes":
        await event.edit("**𓆰 حـسنـًا .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @EEOBot**")
        channel_entity = await sbb_b.get_entity(bot_username)
        await sbb_b.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sbb_b.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sbb_b.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if tepthon[0] == 'no':
                break
            await asyncio.sleep(5)

            list = await sbb_b(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('**𓆰 لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مـخـتـلفة**') != -1:
                await sbb_b.send_message(event.chat_id, f"**𓆰 لا يـوجـد قنـوات بالبـوت حـاليًا ...**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sbb_b(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sbb_b(ImportChatInviteRequest(bott))
                msg2 = await sbb_b.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await sbb_b.send_message("**𓆰 تم بنجـاح الاشتـراك في {chs} قنـاة .❗**")
            except:
                await sbb_b.send_message(event.chat_id, f"**𓆰 القنـاة رقـم {chs} خطـأ .. يمكـن تبنـدت**")
                break
        await sbb_b.send_message(event.chat_id, "**𓆰 تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


