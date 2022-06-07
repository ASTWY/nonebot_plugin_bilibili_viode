# nonebot_plugin_bilibili_viode

nonebot_plugin_bilibili_viode是一个Nonebot2的插件，其功能为将用户发送的B站视频ID转为(伪)分享卡片的形式  

## 如何安装使用
### 安装
`pip install nonebot_plugin_bilibili_viode`  
或者  
`poetry add nonebot_plugin_bilibili_viode`  
### 升级  
`pip install -U nonebot_plugin_bilibili_viode`  
或者  
`poetry add nonebot_plugin_bilibili_viode@latest`  
### 使用
在你的nontbot项目中的bot.py文件中添加  
`nonebot.load_plugin("nonebot_plugin_bilibili_viode")`
### Nonebot配置项
|配置键名|默认值|作用|  
|-|-|-|  
|`bilibili_poster`|True|是否使用海报分享图片样式|  
## 许可
MIT
