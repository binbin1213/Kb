# NAS 部署 PDF 工具箱：Stirling-PDF

**公众号**: NASBox
**发布日期**: 2025-05-04 14:38:16

如有修改或改动，关注文章底部留言！教程对你有用，可以 “**点赞** ” 和 “**打赏** ”支持 ~

  


  


<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPCLcXOb4eibFbyLLkoXJ8oW8TG33s696NuBt4hMNTX5nCSYzNb62ohTuw/640?wx_fmt=png&from=appmsg' />

Stirling-PDF：

一个强大的、本地托管的、基于 Web 的 PDF 操作工具，能够对 PDF 文件执行各种操作，包括拆分、合并、转换、重组、添加图像、旋转、压缩等。

<img src='https://mmbiz.qpic.cn/sz_mmbiz_jpg/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPCdIcSBGRIHR36Vq1sUCa83ZELRdE6zBs9OMjQwWk9HGpyRRESviaqOlg/640?wx_fmt=jpeg&from=appmsg' />

应用特性：

  * • 50+ PDF 操作项
  * • 并行文件处理和下载
  * • 支持深色模式
  * • 自定义下载选项
  * • 自定义“通道”，用于在自动队列中运行多个功能
  * • 用于与外部脚本集成的 API
  * • 支持可选的登录和身份验证
  * • 数据库备份和导入
  * • SSO 等企业功能



### 安装

Docker Compose
    
    
    services:  
     stirling-pdf:  
    image: stirlingtools/stirling-pdf:latest  
    container_name: stirling-pdf  
    ports:  
       - 8080:8080  
    volumes:  
       - /vol1/1000/docker/stirling-pdf/data:/usr/share/tessdata  
       - /vol1/1000/docker/stirling-pdf/configs:/configs  
       - /vol1/1000/docker/stirling-pdf/logs:/logs  
    environment:  
       - SYSTEM_DEFAULTLOCALE=zh_CN  
    restart: always

参数说明（更多参数设置建议去看文档）

:::  
/usr/share/tessdata：存放 OCR 扫描文件

/configs：存放配置文件

/logs：存放日志文件

SYSTEM_DEFAULTLOCALE：设置默认语言

:::

### 使用

浏览器中输入 `http://NAS的IP:8080` 就能看到界面

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPCpnFj1VQ76f4h0vVAE9SJbYTbiaFqibUK7cNbOFkmc3kSoDS20mCM6Ekg/640?wx_fmt=png&from=appmsg' />

点击“禁用分析功能”，进入开始使用

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPCBYetPJ5ianLUKVaqOmaNIVydiaA8ebaU2nUkljqKYyJUPTcTck1lhjVw/640?wx_fmt=png&from=appmsg' />

顶部可以切换深色模式

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPCibygLXbajIibylxtBX6gXWasSLg4393vZ94MVPkVDG2MP7eDdZFia4YQA/640?wx_fmt=png&from=appmsg' />

说实话，现在这个界面和以前比起来丑太多了

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPCV9j85D78WAgbyTnDcD7mpecHXl6Sv9twHa71smm7xPP8hLbBRajhLA/640?wx_fmt=png&from=appmsg' />

我个人还是喜欢旧界面，可以点击这里切换

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPC8pzQm98HNicoMVWZhzibOErYuzWLFVTgm1P6QGRKMUT2Y6dW4eoep3Cw/640?wx_fmt=png&from=appmsg' />

旧界面的样式

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPCHlhBQafSXydxYPHnRtS6QZwqDpxWSwNVRZ6G8gSoEJPhkbTVGvAO2A/640?wx_fmt=png&from=appmsg' />

功能还是挺多的，这里我就简单截图

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPCGCiaYFIvdu8AE00cCp3rEiciaOpZDqbicibibQwjA0O4DEdepj4XvsJzibk2w/640?wx_fmt=png&from=appmsg' />

TIP：

这里我就简单测试一下功能，有需要建议自行部署

浏览 PDF

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPCaib56fuqxEiaYqN9bfibAy5hVoiaVQGBeMluNG7DWPxINgduNarmowbf9A/640?wx_fmt=png&from=appmsg' />

将 Markdown 转换为 PDF

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPCFAPHDAqcTPibj1jfnxMKhLVs9DMDofs2vUj8kF41NichNLehaZaB8qcg/640?wx_fmt=png&from=appmsg' />

生成 PDF 的效果

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPC0P490LicTW3CqoruL3BAdL8sztLwVnPiadEY6sSUXGx4mccm57l6W06A/640?wx_fmt=png&from=appmsg' />

签署 PDF

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPC2UDBibtIiarZAciaGxUia1TvBv5quvdq6BCtQGyMnYE80ANN9un6eibVnyg/640?wx_fmt=png&from=appmsg' />

可以自由跳转签名位置

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6O8eGplhV0ibbgNJcUjBaPCJsYqG9kicLO6lv7smApp77ooDsEtricR7hric4RMiaYFPgskiaZVSth5uLg/640?wx_fmt=png&from=appmsg' />

### 总结

总的来说是一个强大的 PDF 工具，支持的功能丰富，同时也支持中文。其实网上也有很多 PDF 编辑工具，不过大多数都是需要收费，而且担心安全问题，经常需要编辑 PDF 的用户可以部署试试看。

综合推荐：⭐⭐⭐（功能丰富且强大）

使用体验：⭐⭐⭐（界面和交互有待优化）

部署难易：⭐⭐（简单）︎

  


  


  


︎