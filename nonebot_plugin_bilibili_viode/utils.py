from httpx import AsyncClient

from .model import *


# BV号转AV号
async def bv_to_av(bv_id: str) -> str:
    async with AsyncClient() as client:
        resp = await client.get(
            f"https://api.bilibili.com/x/web-interface/view?bvid={bv_id}"
        )
        if resp.status_code == 200:
            data = resp.json()
            if data["code"] == 0:
                return str(data["data"]["aid"])


# 获取B站视频的短链接
async def get_share_sort_url(av_id: str):
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
    return None


# 获取B站视频的视频基本信息
# 传入参数：AV号或者BV号
# 返回值：视频信息类
async def get_video_info(av_id: str):
    if av_id.startswith("BV"):
        av_id = await bv_to_av(av_id)
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
    return None


# 格式化数值
def format_number(number: int) -> str:
    if number >= 100000000:
        return str(round(number / 100000000, 1)) + "亿"
    elif number >= 10000:
        return str(round(number / 10000, 1)) + "万"
    else:
        return str(number)
