# 模板说明

模板是一个 YAML 格式的文件，用于描述 bilibili 视频海报的样式。

## 模板模板节点

### 基础节点属性

除`base`节点外，其他所有的模板节点都有以下属性：

| 属性    | 类型 | 默认值 | 描述                              |
| ------- | ---- | ------ | --------------------------------- |
| visible | bool | False  | 是否可见                          |
| x       | int  | 0      | 在图片中的横坐标                  |
| y       | int  | 0      | 在图片中的纵坐标                  |
| type    | str  | None   | 节点类型，可选值为`image`和`text` |

### 图像节点属性

| 属性   | 类型 | 默认值 | 描述     |
| ------ | ---- | ------ | -------- |
| path   | str  | None   | 图片路径 |
| color  | str  | None   | 图片颜色 |
| width  | int  | None   | 图片宽度 |
| height | int  | None   | 图片高度 |
| radius | int  | None   | 图片圆角 |

当`path`不为空时，图片将从`path`中读取，其余属性将被忽略，但基础节点属性仍然有效。
可以使用自己的图片，将其放置到`nonebot_plugin_bilibili_video/resource/image`文件夹中，然后在模板中使用`path`属性指定图片文件名即可。

### 文本节点属性

| 属性           | 类型 | 默认值  | 描述         |
| -------------- | ---- | ------- | ------------ |
| font           | str  | Arial   | 字体         |
| size           | int  | 12      | 字体大小     |
| color          | str  | #000000 | 字体颜色     |
| font_max_width | int  | None    | 字体最大宽度 |
| font_max_lines | int  | 1       | 字体最大行数 |

字体文件需要放置在`nonebot_plugin_bilibili_video/resource/font`文件夹中，然后在模板中使用`font`属性指定字体文件名即可。

## 节点可用的值

| 节点名      | 类型  | 描述         |
| ----------- | ----- | ------------ |
| base        | image | 背景图       |
| title       | text  | 视频标题     |
| desc        | text  | 视频简介     |
| cover       | image | 视频封面     |
| duration    | text  | 视频时长     |
| pubdate     | text  | 视频发布时间 |
| view        | text  | 视频播放量   |
| danmaku     | text  | 视频弹幕数   |
| like        | text  | 视频点赞数   |
| coin        | text  | 视频硬币数   |
| favorite    | text  | 视频收藏数   |
| share       | text  | 视频分享数   |
| up_name     | text  | UP 主名称    |
| up_face     | image | UP 主头像    |
| up_mid      | text  | UP 主 UID    |
| up_follower | text  | UP 主粉丝数  |
| qrcode      | image | 视频二维码   |

模板样例可参考[默认模板](../nonebot_plugin_bilibili_viode/template/1.yaml)

## 图片绘制流程

按照模板中的节点顺序，从上到下，依次读取节点，如果节点可见，则绘制节点，否则跳过。请注意，base 节点无论放在模板中的什么位置，都会被最先绘制，后绘制的节点如果与前绘制的节点有重叠部分，后绘制的节点将会覆盖这些重叠部分。
