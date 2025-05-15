# NAS 部署国内领先的 LLM 企业解决方案：Chat Nio

**公众号**: NASBox
**发布日期**: 2025-05-13 06:58:30

如有修改或改动，关注文章底部留言！教程对你有用，可以 “**点赞** ” 和 “**打赏** ”支持 ~

  


  


<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94zQBlC19xrua2nzpHGq2cluBAPw0XkLqcicOOn3TicB0HZiccRJNycfCew/640?wx_fmt=png&from=appmsg' />

Chat Nio：

下一代 AIGC 一站式商业解决方案，支持 OpenAI，Midjourney，Claude，讯飞星火，Stable Diffusion，DALL·E，ChatGLM，通义千问，腾讯混元，360 智脑，百川 AI，火山方舟，新必应，Gemini，Moonshot 等模型，支持对话分享，自定义预设，云端同步，模型市场，支持弹性计费和订阅计划模式，支持图片解析，支持联网搜索，支持模型缓存，丰富美观的后台管理与仪表盘数据统计。

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94RrMmJRQKVbIpJibou1TLOiaWfMZ0f9ZrT0Q41MQCtUW4mRmUiaIBpeuXQ/640?wx_fmt=png&from=appmsg' />

TIP：

简单来说这个相当于一个分发平台，将 GPT 的 API 都对接到平台上再分发给用户，用户可以通过该平台调用 GPT 和购买 GPT 服务。

功能：

  * • 🤖️ 丰富模型支持: 多模型服务商支持 (OpenAI / Anthropic / Gemini / Midjourney 等十余种格式兼容 & 私有化 LLM 支持)
  * • 🤯 美观 UI 设计: UI 兼容 PC / Pad / 移动三端，遵循 Shadcn UI & Tremor Charts 设计规范，丰富美观的界面设计和后台仪表盘
  * • 🎃 完整 Markdown 支持: 支持 LaTeX 公式 / Mermaid 思维导图 / 表格渲染 / 代码高亮 / 图表绘制 / 进度条等进阶 Markdown 语法支持
  * • 👀 多主题支持: 支持多种主题切换，包含亮色主题的明亮模式和暗色主题的深色模式。 👉 自定义配色
  * • 📚 国际化支持: 支持国际化，支持多语言切换 🇨🇳 🇺🇸 🇯🇵 🇷🇺 👉 欢迎贡献翻译 Pull Request
  * • 🎨 文生图支持: 支持多种文生图模型: OpenAI DALL-E✅ & Midjourney (支持 U/V/R 操作)✅ & Stable Diffusion✅ 等
  * • 📡 强大对话同步: 用户 0 成本对话跨端同步支持，支持对话分享 (支持链接分享 & 保存为图片 & 分享管理), 无需 WebDav / WebRTC 等依赖和复杂学习成本
  * • 🎈 模型市场 & 预设系统: 支持后台可自定义的模型市场, 可提供模型介绍、标签等参数, 站长可根据情况自定义模型简介。同时支持预设系统，包含 自定义预设 和 云端同步 功能。
  * • 📖 丰富文件解析: 开箱即用, 支持所有模型的文件解析 (PDF / Docx / Pptx / Excel / 图片等格式解析), 支持更多云端图片存储方案 (S3 / R2 / MinIO 等), 支持 OCR 图片识别 👉 详情参见项目 Chat Nio Blob Service (支持 Vercel / Docker 一键部署)
  * • 🌏 全模型联网搜索: 基于 SearXNG 开源引擎, 支持 Google / Bing / DuckDuckGo / Yahoo / WikiPedia / Arxiv / Qwant 等丰富搜索引擎搜索, 支持安全搜索模式, 内容截断, 图片代理, 测试搜索可用性等功能。
  * • 💕 渐进式 Web 应用 (PWA): 支持 PWA 应用 & 支持桌面端 (桌面端基于 Tauri)
  * • 🤩 齐全后台管理: 支持美观丰富的仪表盘, 公告 & 通知管理, 用户管理, 订阅管理, 礼品码 & 兑换码管理, 价格设定, 订阅设定, 自定义模型市场, 自定义站点名称 & Logo, SMTP 发件设置等功能
  * • 🤑 多种计费方式: 支持 💴 订阅制 和 💴 弹性计费 两种计费方式, 弹性计费支持 次数计费 / Token 计费 / 不计费 / 可匿名调用 和 最小请求点数 检测等强大功能
  * • 🎉 创新模型缓存: 支持开启模型缓存：即同一个请求入参 Hash 下, 如果之前已请求过, 将直接返回缓存结果 (击中缓存将不计费), 减少请求次数。可自行自定义是否缓存的模型、缓存时间、多种缓存结果数等高级缓存设置
  * • 🥪 附加功能 (停止支持): 🍎 AI 项目生成器功能 / 📂 批量文章生成功能 / 🥪 AI 卡片功能 (已废弃)
  * • 😎 优秀渠道管理: 自写优秀渠道算法, 支持⚡ 多渠道管理, 支持🥳优先级设置渠道的调用顺序, 支持🥳权重设置同一优先级下的渠道均衡负载分配概率, 支持🥳用户分组, 🥳失败自动重试, 🥳模型重定向, 🥳内置上游隐藏, 🥳渠道状态管理等强大企业级功能
  * • ⭐ OpenAI API 分发 & 中转系统: 支持以 OpenAI API 标准格式调用各种大模型, 集成强大的渠道管理功能, 仅需部署一个站点即可实现同时发展 B/C 端业务💖
  * • 👌 快速同步上游: 渠道设置、模型市场、价格设定等设置都可快速同步上游站点，以此基础修改自己的站点配置，快速搭建自己的站点，省时省力，一键同步，快速上线
  * • 👋 SEO 优化: 支持 SEO 优化，支持自定义站点名称、站点 Logo 等 SEO 优化设设置使搜索引擎更快的爬取，你的站点与众不同👋
  * • 🎫 多种兑换码体系: 支持多种兑换码体系，支持礼品码和兑换码，支持批量生成，礼品码适合宣传分发，兑换码适合发卡销售，礼品码一个类型的多个码一个用户仅能兑换一个码，在宣传中一定程度上减少一个用户兑换多次的情况😀
  * • 🥰 商用友好协议: 采用 Apache-2.0 开源协议, 商用二开 & 分发友好 (也请遵守 Apache-2.0 协议的规定, 请勿用于违法用途)



支持模型：

  * • OpenAI & Azure OpenAI (✅ Vision ✅ Function Calling)
  * • Anthropic Claude (✅ Vision ✅ Function Calling)
  * • Google Gemini & PaLM2 (✅ Vision)
  * • Midjourney (✅ Mode Toggling ✅ U/V/R Actions)
  * • 讯飞星火 SparkDesk (✅ Vision ✅ Function Calling)
  * • 智谱清言 ChatGLM (✅ Vision)
  * • 通义千问 Tongyi Qwen
  * • 腾讯混元 Tencent Hunyuan
  * • 百川大模型 Baichuan AI
  * • 月之暗面 Moonshot AI (👉 OpenAI)
  * • 深度求索 DeepSeek AI (👉 OpenAI)
  * • 字节云雀 ByteDance Skylark (✅ Function Calling)
  * • Groq Cloud AI
  * • OpenRouter (👉 OpenAI)
  * • 360 GPT
  * • LocalAI / Ollama (👉 OpenAI)



关联教程：

[MariaDB 数据库](https://mp.weixin.qq.com/s?__biz=MzI2MjkzMDk3OA==&mid=2247527905&idx=1&sn=275c4df1dcf07e39eca1064204073b19&scene=21#wechat_redirect)

[Redis 远程字典服务](https://mp.weixin.qq.com/s?__biz=MzI2MjkzMDk3OA==&mid=2247529767&idx=1&sn=39e6f72969b5df1f260de3c33b5a7cb8&scene=21#wechat_redirect)

### 安装

Docker Compose
    
    
    services:  
    chatnio:  
    image: programzmh/chatnio:latest  
    container_name: chatnio  
    ports:  
       - "8094:8094"  
    volumes:  
       - /vol1/1000/docker/chatnio/config:/config  
       - /vol1/1000/docker/chatnio/logs:/logs  
       - /vol1/1000/docker/chatnio/storage:/storage  
    environment:  
       - MYSQL_HOST=192.168.31.90  
       - MYSQL_PORT=3306  
       - MYSQL_DB=chatnio  
       - MYSQL_USER=root  
       - MYSQL_PASSWORD=MYSQL_ROOT_PASSWORD  
       - REDIS_HOST=192.168.31.90  
       - REDIS_PORT=6379  
       - SECRET=s5jDa@P3%N8Xsur!m3T6^  
       - SERVE_STATIC=true  
    restart: always

参数说明（更多参数设置建议去看文档）

:::  
/config：存放配置文件

/logs：存放日志文件

/storage：存放附加功能的生成文件

MYSQL_HOST：MySQL 数据库的主机地址

MYSQL_PORT：MySQL 数据库的端口号

MYSQL_DB：连接 MySQL 数据库的名称

MYSQL_USER：连接 MySQL 数据库使用的用户名

MYSQL_PASSWORD：连接 MySQL 数据库使用的密码

REDIS_HOST：Redis 的主机地址

REDIS_PORT：Redis 服务器的端口号

SECRET：JWT 密钥，自行生成随机字符串修改

SERVE_STATIC：是否启用静态文件服务

:::

该篇教程需要用到数据库，不会安装部署的可以参考下面教程

[MariaDB 数据库](https://mp.weixin.qq.com/s?__biz=MzI2MjkzMDk3OA==&mid=2247527905&idx=1&sn=275c4df1dcf07e39eca1064204073b19&scene=21#wechat_redirect)

创建 chatnio 数据库
    
    
    create database chatnio;

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94TuLRDFOb6aEPSyjoT50caKGUhxteP3rWZH3iaOmJFSYGLbyB45FNKyQ/640?wx_fmt=png&from=appmsg' />

### 使用

浏览器中输入 `http://NAS的IP:8094` 就能看到界面

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94vaSfib2lia3whlgicqiaTWJawdUVmPGcw2OwNHBo6o92icaLqkgmJ00jMnA/640?wx_fmt=png&from=appmsg' />

进入界面后，先点击“登录”

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94ibKK9DnnbOmND5ZmFiaibnhZYHpTkiaiczLcN8BcJX0gNxZSN8Yicibl6gGDw/640?wx_fmt=png&from=appmsg' />

管理员账号：root

密码：chatnio123456

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW942xAW9muslwrerGBlZAMh1HiaBZia5HJLraRTy0Pb8aaWEuJic06q1iaWEg/640?wx_fmt=png&from=appmsg' />

#### 基础设置

点击“后台管理”，先设置一下密码那些

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94R1dIzvZK9fG7atmRicLJSaDic8viaDiaWX6mTj9C7m8IXJuSfNtRcOBXSA/640?wx_fmt=png&from=appmsg' />

用户管理修改一下账号的密码，避免忘记了

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94wLDZSibZiaYv1X55RtYIxibqfDMFmibtib3iaB8s05657iaE4I9pO06pKSMbg/640?wx_fmt=png&from=appmsg' />

渠道管理，相当于对接提供 ChatGPT 服务的平台

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94NeeIWlWpFgLZziaZ9PyP8ncjaoH1bKeGgPUtkUN7h452GbVFK41X8Eg/640?wx_fmt=png&from=appmsg' />

TIP：

这里我对接了之前介绍过的第三方平台：https://aigptx.top，还有 OneAPI 也是一样操作

[NextChat 私人 ChatGPT 网页应用](https://mp.weixin.qq.com/s?__biz=MzI2MjkzMDk3OA==&mid=2247529652&idx=1&sn=b1cd7a0b8c28f451e8c9712515498c4b&scene=21#wechat_redirect)

[One API 接口管理和分发系统](https://mp.weixin.qq.com/s?__biz=MzI2MjkzMDk3OA==&mid=2247523380&idx=1&sn=9fcfea06e130c8cac31af9e4d6761c90&scene=21#wechat_redirect)

填写地址和密钥即可

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94ehPblKqPn1CoPyOicgT6lm0ZgianSW7yZFymPpZbq8sjVykwo8NG4Qsw/640?wx_fmt=png&from=appmsg' />

数据都自动填写好了，其他设置默认即可，点击保存

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94TEjcQY2K0SyNSKAtmQxn3RBsDV7HHxv0LeNIRF1QPsRVia3BTaHRgSA/640?wx_fmt=png&from=appmsg' />

这样就完成渠道对接了

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94g9U0wJnfkdrKu7ia2o6qLgzcerK0Z3uHLdlA4hpmn3W8VxtnhXScw3A/640?wx_fmt=png&from=appmsg' />

模型市场，可以单独选择需要调用的模型（个人使用不建议导入全部），拉到最底部点击提交即可

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94lF1hGezicoKFcDIE8OuBEM0yWP9R9eSsDaic9MuraqgdvyLSiaPef1OXg/640?wx_fmt=png&from=appmsg' />

回到会话界面，就能看到有模型可以选择了

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94ktlfZD5KRHSWUx89VaZIlK2X8OA56MGY5fjj8NaZqytxRScdPyFnkA/640?wx_fmt=png&from=appmsg' />

返回聊天对话界面，测试一下是否可以正常调用

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94ibzGlBhhhTByHTvznwAvJUdgTibPmCR5XNX4bssaib2HopkdJe3nos7Wg/640?wx_fmt=png&from=appmsg' />

#### 日常使用

上面如果设置好 API，这里就可以正常被调用

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94EzHFHia2FwMFbV83gm8Ijnia0jxcc08QG0ibZCShduuYLLicXMeZ1BcxRg/640?wx_fmt=png&from=appmsg' />

快捷栏功能：联网搜索，上传文件，文本编辑，模型市场，偏好设置

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94vmgxGXGmXPXYXiaPibbRqWibRUxc8ibFWcbicWzx3ia1MBjtfMmpAXz8D4hQ/640?wx_fmt=png&from=appmsg' />

联网搜索，默认后台已经配置好的（不过好像有点问题），也可以自行部署

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94P1eZkFkkiaG6LdatianHiaIBDtLnGoflfWO4to6y5PpL5CQvKWP0bWpicA/640?wx_fmt=png&from=appmsg' />

上传文件，可以直接使用（需要联网的）

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW943tTSVGNgMIV141AzxVpQlkes1f1h3sniczFy85KZkOntvpJJNWaftaA/640?wx_fmt=png&from=appmsg' />

上传文档以后，可以看到效果还是有的

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94h8cU7XiabpV2qK1EibxiaUDulSnIg464FOpXhKrj8qicgx2aWeGxZdbEMQ/640?wx_fmt=png&from=appmsg' />

有需要本地文件解析服务，也可以在后台替换为自己部署的服务

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94UGIjJO4O6aahaHFVFnfSicibVMHF30JYA51cTlia8LmzZ7q9nDXlSqeJg/640?wx_fmt=png&from=appmsg' />

文本编辑，发比较多内容的时候比较实用

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94TPRYKnSWFyykeTCTVetKPKjKPymQWWVYGoenibYiaBZxJEGIVmcoPyxw/640?wx_fmt=png&from=appmsg' />

预设设置，相当于角色扮演

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW949jUL5NjZEGEyeiaRw20icoomLaYqw9CEg58KTqmIKFjQDdQ3kBIvpmfQ/640?wx_fmt=png&from=appmsg' />

模型列表（模型市场），可以快速切换模型和相关GPT的介绍

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW940l1t4pyLdeRiakXAIxvtmB5WXyC1icHKtVOHIxPh8PSLib0tldVQWD7xA/640?wx_fmt=png&from=appmsg' />

偏好设置，根据需要设置，一般默认即可

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94EC10brSicXSHZ0GeFsKia1mN5TFFZH8USgL1onK5F13XTSvcdOyjxdsA/640?wx_fmt=png&from=appmsg' />

#### 后台管理

这里就简单截图，不详细介绍了

仪表盘

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94AuRC59lqUkMcOiaJTGlELY5clRvVCzNfXh9mZerM7yyzBrbTkdVGWeQ/640?wx_fmt=png&from=appmsg' />

用户管理

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94IRTVhcZu3AUlTGZYaT0Up3zkEkhyYxuJUiasnr8QRzOo3RS56ZKe6cg/640?wx_fmt=png&from=appmsg' />

模型市场

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94HmoeJhhV7xmib7joOHC0ClZoUq5mQJcG1Bcp8PicuciaH95iaL2ayIllQQ/640?wx_fmt=png&from=appmsg' />

通知管理

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94l4tmWickmMqcITc1pZIsclAtV1sOjIlOFyLsyg9Ff5Mhr6RNqNw1CLA/640?wx_fmt=png&from=appmsg' />

渠道设置

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94Sw2z2P7SdLm4HLWxxrtJkKOhwNFGGtXS7rj4OE6xP1pbRgWUTfyARQ/640?wx_fmt=png&from=appmsg' />

价格设定

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94YMN1HiawHXI5FYmQMFM0IGZwk1wbLooD3JL6u3yL3nm2OelW3CZA5Ug/640?wx_fmt=png&from=appmsg' />

订阅管理

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW945DibhFlManPbYqaofvmdPGO1t7JrGOf5l2GuvZAuTqvncFQjdwfzMWA/640?wx_fmt=png&from=appmsg' />

系统设置

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94Yibd4dPF4Rp8FQbpsoEB7RqreZ54kZBOh9jFeQzQhR5f3ZVHn0xibLYg/640?wx_fmt=png&from=appmsg' />

服务日志

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km6glia50jgBFkIzmzYJkAW94ECUFogEG95OaoJBxDquXqjoL9Vic8ricRRYvOkLibCf4SQomlIeVpEY5A/640?wx_fmt=png&from=appmsg' />

### 总结

为对于有用的人来说很有用，对于没需求的人我只能说你是来捣乱的吧。个人用起来感觉挺不错的，后台管理也很容易上手，功能各方面都挺不错的。

综合推荐：⭐⭐⭐⭐（非常推荐）

使用体验：⭐⭐⭐⭐（美观好用）

部署难易：⭐⭐（简单）︎

  


  


  


︎