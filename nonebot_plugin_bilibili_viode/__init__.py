from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
from nonebot import on_message
from nonebot_plugin_guild_patch import GuildMessageEvent
from typing import Union
from .utils import *
from .img import build_get_share_info

share_sort_url = on_message(block=False)


@share_sort_url.handle()
async def _(event: Union[MessageEvent, GuildMessageEvent]):
    if event.raw_message.startswith("av") and event.raw_message[2:].isdigit():
        video_id = event.raw_message[2:]
    elif event.raw_message.startswith("BV"):
        video_id = await bv_to_av(event.raw_message)
    else:
        return
    viode_info = await get_video_info(video_id)
    if viode_info:
        msg = MessageSegment.image(
            await build_get_share_info(viode_info)
        ) + MessageSegment.text("\n点击前往:" + viode_info.shareUrl)
        await share_sort_url.finish(msg)

__version__ = '0.1.0'
