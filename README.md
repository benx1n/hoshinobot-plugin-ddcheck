# hoshinobot-plugin-ddcheck

Hoshinobot 成分姬插件

查询B站关注列表的VTuber成分，并以图片形式发出

插件移植自[nonebot-plugin-ddcheck](https://github.com/noneplugin/nonebot-plugin-ddcheck)

VTB列表数据来源：[vtbs.moe](https://vtbs.moe/)


### 使用方式

**以下命令需要加[命令前缀](https://v2.nonebot.dev/docs/api/config#Config-command_start) (默认为`/`)，可自行在bot.py中的COMMAND_START设置为空**

```
查成分 + B站用户名/UID
```


### 安装

```
git clone https://github.com/benx1n/hoshinobot-plugin-ddcheck.git

pip install -r requirements.txt

将config_example.json拷贝一份后重命名为config.json

在bot.py中添加'hoshinobot-plugin-ddcheck'
```
初次运行时由于需要下载chromium故可能会等待较长时间，请关注控制台输出的进度条<br><br>

<<<<<<< HEAD
### 已知问题
由于windows下playwright无法兼容SelectorEventLoop，如果您的其他插件中包含有如下代码（一般是用于解决aiohttp的代理问题）
=======

若要显示主播牌子，需要在 `.config.json` 文件中添加任意的B站用户cookie：

需要在 `.env.xxx` 文件中添加任意的B站用户cookie：

>>>>>>> a9bbd8c2fe8349915dbb0a370965c630f81d890f
```
"cookie" = "xxx"
```
初次运行时由于需要下载chromium故可能会等待较长时间，请关注控制台输出的进度条<br><br>

### 已知问题
由于windows下playwright无法兼容SelectorEventLoop，如果您的其他插件中包含有如下代码（一般是用于解决aiohttp的代理问题）
```
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```
详情请见[#1](https://github.com/benx1n/hoshinobot-plugin-ddcheck/issues/1)
已知有冲突的插件：setu_renew
`cookie` 获取方式：

`F12` 打开开发工具，查看 `www.bilibili.com` 请求的响应头，找形如 `SESSDATA=xxx;` 的字段，如：

```
bilibili_cookie="SESSDATA=xxx;"
```

<div align="left">
  <img src="https://s2.loli.net/2022/07/19/AIBmd2Z9V5YwlkF.png" width="500" />
</div>


### 示例

<div align="left">
  <img src="https://s2.loli.net/2022/03/20/Nk3jZJgxforHDsu.png" width="400" />
</div>
