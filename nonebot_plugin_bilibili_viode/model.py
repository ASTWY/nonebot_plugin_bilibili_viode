# UP主信息类
class UpInfo:
    def __init__(self, uid: int, name: str, iconUrl: str):
        self.uid = uid
        self.name = name
        self.iconUrl = iconUrl


# 视频信息类
class VideoInfo:
    def __init__(
        self,
        title: str,
        pictureUrl: str,
        desc: str,
        pubdate: int,
        upInfo: UpInfo,
        shareUrl: str,
    ) -> None:
        self.title = title
        self.pic = pictureUrl
        self.desc = desc
        self.pubdate = pubdate
        self.upInfo = upInfo
        self.shareUrl = shareUrl
