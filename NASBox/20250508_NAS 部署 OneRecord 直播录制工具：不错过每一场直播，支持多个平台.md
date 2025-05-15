# NAS 部署 OneRecord 直播录制工具：不错过每一场直播，支持多个平台

**公众号**: NASBox
**发布日期**: 2025-05-08 01:29:32

如有修改或改动，关注文章底部留言！教程对你有用，可以 “**点赞** ” 和 “**打赏** ”支持 ~

  


  


<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amv7PvVmtEM61mRG0O2K3RrItiawcymo8LicGTSxicnUlkmRicIG1ic08EvPzw/640?wx_fmt=png&from=appmsg' />

OneRecord：

一款专业的直播录制工具，支持多平台直播录制，无水印下载，高清回放，让您不错过每一个精彩瞬间

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvyRsdZpGNPExyhr4UZe34oV6iaibHoVEy3ENKPCxILOCanj5jc7oaK68Q/640?wx_fmt=png&from=appmsg' />

直播平台：

已支持哔哩哔哩、YouTube、Twitter、抖音、TikTok、Twitch、afreecatv、虎牙、斗鱼、pixiv、bigo、花椒、全民K歌等平台的直播录制功能

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvdHlf5murbMEVPXNwkbwPaXLOnRmVHypJvJY6DxrND6kSic0UZOVIyGA/640?wx_fmt=png&from=appmsg' />

### 安装

Docker Compose
    
    
    services:  
    onerecord:  
    image: registry.cn-hangzhou.aliyuncs.com/onerecord/onerecord:latest  
    container_name: onerecord  
    ports:  
       - 18080:8080  
    volumes:  
       - /vol1/1000/docker/onerecord/config:/data/feiyu-live-server/config  
       - /vol1/1000/docker/onerecord/config/oneRecord:/root/.OneRecord  
       - /vol1/1000/docker/onerecord/logs:/root/.feiyu/logs  
       - /vol1/1000/docker/onerecord/config/aliyunpan:/data/feiyu-live-server/ali  
       - /vol1/1000/docker/onerecord/config/bypy:/root/.bypy  
       - /vol1/1000/docker/onerecord/data:/data/feiyu-live-server/data  
    environment:  
       - JVMPARAM=-Xms512m -Xmx1g  
       - ACTIVEPROFILES=pro  
    restart: always

参数说明（更多参数设置建议去看文档）

:::  
/data/feiyu-live-server/data：存放录制视频

:::

### 准备

温馨提示：为了确保 docker 镜像不被滥用，强制 docker 服务端必须要通过账号密码来访问。

首先需要到网站注册一个账号

https://plus.bestlive.cc

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amv9jXAX31nZybxZIoNyuUibKlKBoYLeeZyK4FWeqiaUTRq5NPZhYtFd0Gg/640?wx_fmt=png&from=appmsg' />

使用邮箱进行注册

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvu2yjwQBicS3xfBXcL8agm9BtBYeWdVoAFEWVRL3CfUUb5xK2vibPMbkQ/640?wx_fmt=png&from=appmsg' />

注册完成就行

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvAuYNPKblAQgACcaBhWgYVW9fmpqrE4tcT5qqdHPNIRJsbe1M7p2m0w/640?wx_fmt=png&from=appmsg' />

### 使用

浏览器中输入 `http://NAS的IP:18080` 就能看到界面

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvak8qjCa0ChPWvmpiaeJMAePqPVHOmwoQqmlYqRDooiabPVkic5KfCLyDA/640?wx_fmt=png&from=appmsg' />输入前面注册的账号和密码<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvR480qStwRcicEjbyZfA4C7vSehX1RC1WHpx8JjPbKz0E8mtg3kFyeoA/640?wx_fmt=png&from=appmsg' />

进入面板

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvbgibf2h6SsGleKJvkCVsbicyiaSUllmAkILOUdCS9Jh5Mfvbia2EDEXPJQ/640?wx_fmt=png&from=appmsg' />

右上角，可以切换深色模式

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvOkMUFORJjJduoK0tMN51vV30O7viatRMToCtK9XkBJWfSniczsHqwtqw/640?wx_fmt=png&from=appmsg' />

配置管理，这里默认就已经设置好的了

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvvPw9UHMjia9mwxWhIWVZ1RM5taq86dYdSlHWPGjDtWkX8mf1uLGxhZA/640?wx_fmt=png&from=appmsg' />

直播管理，添加直播录制

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvQvHuwMEhhySrJic358Z7DegGicD1vyQhYBAeaprmCbWwj1aD9Zu3icEiaQ/640?wx_fmt=png&from=appmsg' />

粘贴直播链接上去就行，其他可以不用调整，点击保存即可

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amv3ovRar0cSthNjwuGCgvMlavvBc68N7BmS3rBkjcBE7LwoTRZeQ3IHQ/640?wx_fmt=png&from=appmsg' />

可以看到添加成功，已经开始录制了

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvmNcu7pCzYDQwC37ZsJdeZKofVr9biblKo7hUajWVVnF3yicwxia6rem5g/640?wx_fmt=png&from=appmsg' />

右侧按钮，可以对当前录制进行设置

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amve083wurtUWdgcJ8MNZeHVGS4tEA37ScwNnTFHbTwWmtqxwGc1JbaNw/640?wx_fmt=png&from=appmsg' />

文件管理，能看到录制的文件

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvwv2LZZGxDDh35yHv732ebnNw1sxVv700AsEHcHRSVP1QFalaD0atxg/640?wx_fmt=png&from=appmsg' />

来到飞牛也是可以看到的

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvCAA2bTTiaibLvQVDt5fGzAkCbqWjxDNgHzg06SZlDSBnTcXJZeD6LFtg/640?wx_fmt=png&from=appmsg' />

点击播放也是没有问题的

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km5QNdS7cHel4xLPzR1C9amvNI6gVBj6UYv1qWRZjAN6LO22VTOFH4JVnhO8gwZa9y2lEarNDEn7icg/640?wx_fmt=png&from=appmsg' />

### 总结

这款录制直播应用还是非常方便的，可以录制国内大多数平台的直播。不过个人 Docker 部署也需要账号这点，我个人还是有点膈应的，虽然目前免费也可以使用，但是总感觉以后应该都要收费。只能说有需要的先用着再说吧，以后真的收费再换其他。

综合推荐：⭐⭐⭐⭐（支持平台多）

使用体验：⭐⭐⭐（配置简单）

部署难易：⭐⭐（简单）︎

  


  


  


︎