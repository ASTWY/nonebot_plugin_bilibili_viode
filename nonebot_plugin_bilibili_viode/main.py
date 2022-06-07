from typing import Union

from nonebot import on_message
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
from nonebot_plugin_guild_patch import GuildMessageEvent

from . import config
from .img import build_get_share_info, build_video_poster
from .utils import *

share_sort_url = on_message(block=False)


@share_sort_url.handle()
async def _(event: Union[MessageEvent, GuildMessageEvent]):
    if event.raw_message.startswith("av") and event.raw_message[2:].isdigit():
        video_id = event.raw_message[2:]
    elif event.raw_message.startswith("BV"):
        video_id = await bv_to_av(event.raw_message)
    else:
        return
    video_info = await get_video_info(video_id)
    if config.bilibili_poster:
        img = await build_video_poster(video_info)
    else:
        img = await build_get_share_info(video_info)
    if img:
        msg = MessageSegment.image(img) + MessageSegment.text(
            "\n点击前往:" + video_info.shareUrl
        )
        await share_sort_url.finish(msg)
