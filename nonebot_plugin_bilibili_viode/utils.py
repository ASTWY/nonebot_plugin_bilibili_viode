import re

from httpx import AsyncClient

from .av2bv import bv2av
from .model import *


async def bilibili_video_id_from_url(uri: str) -> str:
    # 正则匹配哔哩哔哩视频链接, 返回视频ID
    # 传入参数：视频链接
    # 返回值：视频ID
    pattern = "(http(s)?:\/\/)?(www\.)?(bilibili\.com|b23\.tv)\/(video\/)?(av[0-9]*|BV[A-Za-z0-9]*|[A-Za-z0-9]*)"
    match = re.match(pattern, uri)
    if match:
        if match.group(4) == "b23.tv":
            async with AsyncClient() as client:
                resp = await client.get(uri)
                if resp.status_code == 302:
                    return await bilibili_video_id_from_url(resp.headers["Location"])
        return match.group(6)
    raise ValueError("Invalid video url")


async def bilibili_video_id_validate(video_id: str) -> str:
    # 正则校验哔哩哔哩视频ID,返回视频aid
    # 传入参数：视频ID
    # 返回值：视频aid （av号）
    regex = "(av[0-9]*)|(BV[A-Za-z0-9]*)"
    match = re.match(regex, video_id)
    if match:
        if video_id.startswith("BV"):
            video_id = await bv2av(video_id)
        return video_id
    raise ValueError("Invalid video id")


async def get_share_sort_url(av_id: str):
    # 获取B站视频的分享短链接
    # 传入参数：AV号
    # 返回值：分享短链接 （https://b23.tv/xxxxxx）
    body = {
        "build": "6060600",
        "buvid": "0",
        "oid": av_id,
        "platform": "android",
        "share_channel": "QQ",
        "share_id": "main.ugc-video-detail.0.0.pv",
        "share_mode": "7",
    }
    async with AsyncClient() as client:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        resp = await client.post(
            url="http://api.biliapi.net/x/share/click", headers=headers, data=body
        )
        if resp.status_code == 200:
            data = resp.json()
            if data["code"] == 0:
                return data["data"]["link"]
    raise ValueError("Get share sort url failed")


async def get_video_info(av_id: str):
    # 获取B站视频的视频基本信息
    # 传入参数：AV号或者BV号
    # 返回值：视频信息类
    if av_id.startswith("BV"):
        av_id = await bv2av(av_id)
    shareUrl = await get_share_sort_url(av_id)
    apiUrl = "http://api.bilibili.com/x/web-interface/view?aid=" + av_id
    async with AsyncClient() as client:
        resp = await client.get(apiUrl)
        if resp.status_code == 200:
            data = resp.json()
            if data["code"] == 0:
                resp = await client.get(
                    "http://api.bilibili.com/x/web-interface/card?mid="
                    + str(data["data"]["owner"]["mid"])
                )
                if resp.status_code == 200:
                    upInfo = resp.json()["data"]["card"]
                return VideoInfo(
                    title=data["data"]["title"],
                    pictureUrl=data["data"]["pic"],
                    desc=data["data"]["desc"],
                    pubdate=data["data"]["pubdate"],
                    upInfo=upInfo,
                    stat=data["data"]["stat"],
                    shareUrl=shareUrl
                    if shareUrl
                    else "http://www.bilibili.com/video/av" + av_id,
                )
    raise ValueError("Get video info failed")


def format_number(number: int) -> str:
    # 格式化播放量
    # 传入参数：播放量
    # 返回值：格式化后的播放量
    if number >= 100000000:
        return str(round(number / 100000000, 1)) + "亿"
    elif number >= 10000:
        return str(round(number / 10000, 1)) + "万"
    else:
        return str(number)
