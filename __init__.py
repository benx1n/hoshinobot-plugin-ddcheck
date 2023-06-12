import base64
import random
import traceback
from io import BytesIO

import hoshino
from hoshino import Service, priv
from hoshino.typing import CQEvent, MessageSegment
from loguru import logger
from PIL import Image

from .data_source import get_reply, update_vtb_list

sv = Service("ddcheck", manage_priv=priv.SUPERUSER, enable_on_default=True)

__help__plugin_name__ = "ddcheck"
__des__ = "成分姬"
__cmd__ = """
查成分 {用户名/UID}
""".strip()
__short_cmd__ = __cmd__
__example__ = """
查成分 小南莓Official
""".strip()
__usage__ = f"{__des__}\nUsage:\n{__cmd__}\nExample:\n{__example__}"


@sv.on_prefix(("查成分"))
async def ddcheck(bot, ev: CQEvent):
    text = str(ev.message).strip()
    if not text:
        await bot.send(ev, "请在指令后跟随用户昵称或uid哦~")
        return

    try:
        res = await get_reply(text)
        Image.open(BytesIO(res))
        img_base64 = base64.b64encode(res).decode("utf8")
    except:  # noqa: E722
        logger.warning(traceback.format_exc())
        await bot.send(ev, "请检查昵称或uid是否正确哦～")
        return

    if isinstance(res, str):
        await bot.send(ev, "出错了，请稍后再试")
        return

    else:

        await bot.send(ev, str(MessageSegment.image("base64://" + img_base64)))


@sv.scheduled_job("cron", hour="4", minute="30")
async def scheduled_job1():
    bot = hoshino.get_bot()
    msg = await update_vtb_list()
    superid = hoshino.config.SUPERUSERS[0]
    sid = hoshino.get_self_ids()  # 获取bot账号列表
    if len(sid) > 0:  # 若bot账号数量大于0，则随机选择一个号向超级管理员发送消息
        sid = random.choice(sid)
        try:
            await bot.send_private_msg(self_id=sid, user_id=superid, message=msg)
        except Exception as e:
            hoshino.logger.error(f"向超级管理员发送更新消息失败：{type(e)}")
