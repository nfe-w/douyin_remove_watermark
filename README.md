# douyin_remove_watermark

## 简介

获取抖音视频无水印下载地址、抖音图片无水印下载地址

## 运行环境

- [Python 3](https://www.python.org/)

## 使用教程

#### 0. 启动项目

```shell
sh startup.sh
```

#### 1. 发post请求

```shell
curl "http://127.0.0.1:7775/execute/video" -H "Content-Type: application/json" -X POST -d '{"share_text": "抖音视频分享链接" }'
curl "http://127.0.0.1:7775/execute/image" -H "Content-Type: application/json" -X POST -d '{"share_text": "抖音图集分享链接" }'
```

## 声明

- 本仓库发布的`douyin_remove_watermark`项目中涉及的任何脚本，仅用于测试和学习研究，禁止用于商业用途
- `nfe-w`对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害
- 以任何方式查看此项目的人或直接或间接使用`douyin_remove_watermark`项目的任何脚本的使用者都应仔细阅读此声明
- `douyin_remove_watermark` 保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或`douyin_remove_watermark`项目，则视为已接受此免责声明
- 本项目遵循`MIT LICENSE`协议，如果本声明与`MIT LICENSE`协议有冲突之处，以本声明为准
