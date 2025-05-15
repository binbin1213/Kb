# NAS 部署 MeTube，一款功能强大的视频下载工具

**公众号**: NASBox
**发布日期**: 2025-04-29 01:01:29

如有修改或改动，关注文章底部留言！教程对你有用，可以 “**点赞** ” 和 “**打赏** ”支持 ~

  


  


<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km65gT70oZr6feo6FnwqChibOzC6k1CFNKFv65jyQWWaoaxZ63lzHfLXP8zRicFldoMT7sibIrL4O6G5g/640?wx_fmt=png&from=appmsg' />

MeTube：

一款基于 youtube-dl（使用 yt-dlp 分支）的可视化软件，允许从 YouTube 和许多其他网站下载各类视频

<img src='https://mmbiz.qpic.cn/sz_mmbiz_gif/5xFLia3A3km65gT70oZr6feo6FnwqChibOhCYDFdCvs06FNFjPPJNOzmCfXJiaeqwzpjxGib8VfEdkkMQwIRZMCgaQ/640?wx_fmt=gif&from=appmsg' />

支持下载视频的网站（B站和油管都可以）:

https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

### 安装

Docker Compose
    
    
    services:  
    metube:  
    image: alexta69/metube:latest  
    container_name: metube  
    ports:  
       - 8081:8081  
    volumes:  
       - /vol1/1000/docker/metube/downloads:/downloads  
       - /vol1/1000/docker/metube/cookies:/cookies  
    environment:  
       - YTDL_OPTIONS={"cookiefile":"/cookies/cookies.txt"}  
    restart: unless-stopped

参数说明（更多参数设置建议去看文档）

:::  
/downloads：视频下载目录

/cookies（可选）：使用浏览器 Cookie

YTDL_OPTIONS（可选）：要传递给 yt-dlp 的其他选项，采用 JSON 格式

:::

### 浏览器插件

这里需要安装一个浏览器插件获取 Cookie 文件，这样才能下载更高分辨率视频

下载安装浏览器插件（Microsoft Edge & Google Chrome）

https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km65gT70oZr6feo6FnwqChibOHviaNqDdasBq5RVOa3RswY9Hugia251y8R5Ta4Per9P1qgRVevS7SUrg/640?wx_fmt=png&from=appmsg' />

固定在浏览器工具栏

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km65gT70oZr6feo6FnwqChibOwXzo0o8g75yyYXXWreibtCr6Mp4ic3nkAdECjstXkfiajdHNTwx77Fb8A/640?wx_fmt=png&from=appmsg' />

只需要视频网站登录过就行，点击导出 Cookie（包含浏览器所有网站的了）

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km65gT70oZr6feo6FnwqChibOJnGOxXN1BDiceUQ9IyPoz6yuVau6SRyR3rPnrgdewL78E5JPfwMXU1w/640?wx_fmt=png&from=appmsg' />

将 cookies.txt 文件放到 cookies 目录下

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km65gT70oZr6feo6FnwqChibObHOu4GRlO8amo5g6iavkex8DLic9K3JNJk5ia94cyiaUOqGkfVIFUSbyww/640?wx_fmt=png&from=appmsg' />

### 使用

浏览器中输入 `http://NAS的IP:8081` 就能看到界面

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km65gT70oZr6feo6FnwqChibOIv0OvOTmyRAPAGL7w4lAHBLkPvlQM0wKp1L39fI5VpT1iaEMZUHKYUA/640?wx_fmt=png&from=appmsg' />

右上角可以切换深色主题

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km65gT70oZr6feo6FnwqChibORRFlCdjcZUzUNg9LyKwlkr4ruEdIPgF1mQ1tpl19Vuic9UM1EWD0N3g/640?wx_fmt=png&from=appmsg' />

功能还是比较简单的，分为三个模块：链接，下载和完成

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km65gT70oZr6feo6FnwqChibOhhJCFywE44R9lBxXcHM3jDiaOicbI0wMLGEwZUnCkfKQuxoLP8E9p5lQ/640?wx_fmt=png&from=appmsg' />

粘贴要下载的视频链接，点击下载即可（可以自行设置视频质量和格式）

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km65gT70oZr6feo6FnwqChibOvr3CTeiacf5ryXZpQFAWXUpwpk8lfULFUa1ralibuhiciaENRdibjnbMEqQ/640?wx_fmt=png&from=appmsg' />

TIP：

这里具体说说 B 站和油管的下载

B站（1080p），不需要 Cookie ，如果不能识别下载可以参考下面链接格式

https://www.bilibili.com/video/BV1NA4m137Tj

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km65gT70oZr6feo6FnwqChibOEYuAX8ZNDo0yviaZRsvicgXFDvmgNmrf9icSf3UDFzFdUmEsw66ggXElg/640?wx_fmt=png&from=appmsg' />

油管（1080P），需要有 Cookie 和良好的网络，不然会下载错误

https://www.youtube.com/watch?v=8L5cQlXMpeY

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km65gT70oZr6feo6FnwqChibO3RAib1ric88XLShicfPuPPtpmNH0H66bbpA8o0U1Eo0W5ILsuVNk2iaHzw/640?wx_fmt=png&from=appmsg' />

### 总结

不要问我 xxx 网站视频能不能下载，有会员的话分辨率多少这种问题，不介意的可以帮我充个会员我都可以测试！！！目前测试了 B 站，不需要 Cookie 也可以下载 1080P 视频，没有会员的就不要获取 Cookie 了；油管需要 Cookie 和良好网络才能正常下载视频，不然会显示下载错误。

综合推荐：⭐⭐⭐（取决于网站是否支持）

使用体验：⭐⭐⭐（功能比较单一）

部署难易：⭐⭐⭐（中等）︎

  


  


  


︎