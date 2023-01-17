# -*- coding: utf-8 -*-
from pydantic import BaseModel

# bilibili UP主信息类
class UpInfo(BaseModel):
    mid: int  # UP主ID
    name: str  # UP主名
    icon: str  # UP主头像URL


# bilibili 视频统计信息类 (播放量、弹幕数、收藏数、点赞数、硬币数、分享数)
class Stat(BaseModel):
    view: int  # 播放量
    danmaku: int  # 弹幕数
    favorite: int  # 收藏数
    like: int  # 点赞数
    coin: int  # 硬币数
    share: int  # 分享数


# 视频信息类
class VideoInfo(BaseModel):
    title: str  # 视频标题
    pictureUrl: str  # 视频封面URL
    desc: str  # 视频简介
    pubdate: int  # 视频发布时间
    upInfo: UpInfo  # UP主信息
    stat: Stat  # 视频统计信息
    shareUrl: str  # 视频分享链接

    @classmethod
    async def load(cls, video_id: str):
        from .utils import bilibili_video_id_validate
