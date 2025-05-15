# Docker 部署 Dashdot 仪表板，随时监控 NAS 运行状况

**公众号**: NASBox
**发布日期**: 2025-05-07 02:01:58

如有修改或改动，关注文章底部留言！教程对你有用，可以 “**点赞** ” 和 “**打赏** ”支持 ~

  


  


<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6WdzT1g76bVWEWkI2ia5CH05BogTvia6FsYlaHEfBdJsXib169M7rrsD6tic7FLJltfhGSeYnGv6M8gQ/640?wx_fmt=png&from=appmsg' />

Dashdot：

一款现代服务器仪表板，用于较小的 VPS 和私人服务器。

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6WdzT1g76bVWEWkI2ia5CH03btNtwJK1ggb1TZicicFPKHtgXQfSaQpyrF15XhSeia7iaZMp0ylvHE03w/640?wx_fmt=png&from=appmsg' />

### 安装

Docker Compose
    
    
    services:  
     dashdot:  
      image: mauricenino/dashdot:latest  
      container_name: dashdot  
      ports:  
       - 3001:3001  
      volumes:  
       - /vol1/1000/docker/dashdot:/mnt/host  
      restart: always

### 使用

浏览器中输入 `http://NAS的IP:3001` 就能看到界面

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6WdzT1g76bVWEWkI2ia5CH0t92l5jj46Sz2ySibL0FV6bkf6IwYNZn0gYiaO4H39XbKARmPhBh9PJow/640?wx_fmt=png&from=appmsg' />

初次进入，默认什么都没设置，基本信息都有

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6WdzT1g76bVWEWkI2ia5CH0xqic7Tod5djUDBUSJN6pmmXuRAk46PiaxXbHEr9nv7ANfX2xUUKDdj3g/640?wx_fmt=png&from=appmsg' />

切换深色模式

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6WdzT1g76bVWEWkI2ia5CH0IlREVFib9Vhluncg3FIGNHpF2qlplq2mCM5dPtKAazfoRsjbYKWYN5A/640?wx_fmt=png&from=appmsg' />

切换可以数框框

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6WdzT1g76bVWEWkI2ia5CH0yhicdde9TgbDrZmM5co2qN5QLsf13oTVFGib0CDHjxkpM7NPcm0bnR6Q/640?wx_fmt=png&from=appmsg' />

容量是正确的，不过占用大小不显示

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6WdzT1g76bVWEWkI2ia5CH0mp3hceUsia2loUoHawXOhBGia0U8rfxB1Wenq13OOq0S8FM4NRK2VKqg/640?wx_fmt=png&from=appmsg' />

### 总结

这款仪表板功能还是相当简单的，不需要设置任何东西，部署就行了，可以简单直观查看系统的一些信息。因为我这里是在虚拟机里，所以可能有些数据并不能正常显示。

综合推荐：⭐⭐⭐（看个人需要）

使用体验：⭐⭐⭐（过于简单了，没什么功能）

部署难易：⭐⭐（简单）︎

  


  


  


︎