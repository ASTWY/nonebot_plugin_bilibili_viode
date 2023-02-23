# nonebot_plugin_bilibili_viode

[![](https://img.shields.io/badge/pypi-1.0.0-green)](https://pypi.org/project/nonebot-plugin-bilibili-viode/)

nonebot_plugin_bilibili_viode 是一个 Nonebot2 的插件，其功能为将用户发送的 B 站视频 ID 转为(伪)分享卡片的形式

## [更新日志](/CHANGELOG.markdown)

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

在你的 nontbot 项目中的 bot.py 文件中添加  
`nonebot.load_plugin("nonebot_plugin_bilibili_viode")`

### Nonebot 配置项

| 配置键名            | 默认值 | 作用                               |
| ------------------- | ------ | ---------------------------------- |
| `bilibili_template` | 1      | 指定使用 template 目录下的那个模板 |

## 许可

MIT
