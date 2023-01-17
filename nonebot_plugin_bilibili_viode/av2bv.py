from httpx import AsyncClient


_api = "https://api.bilibili.com/x/web-interface/view"


async def av2bv(av_id: str) -> str:
    # av2bv
    # 传入参数：AV号
    # 返回值：BV号
    async with AsyncClient() as client:
        resp = await client.get(_api, params={"aid": av_id})
        if resp.status_code == 200:
            data = resp.json()
            if data["code"] == 0:
                return data["data"]["bvid"]
    raise ValueError("Get video info failed")


async def bv2av(bv_id: str) -> str:
    async with AsyncClient() as client:
        resp = await client.get(_api, params={"bvid": bv_id})
        if resp.status_code == 200:
            data = resp.json()
            if data["code"] == 0:
                return str(data["data"]["aid"])
    raise ValueError("Get video info failed")
