# NAS 部署 EasyVoice 开源的文本转语音工具，支持 AI 推荐和多角色配音

**公众号**: NASBox
**发布日期**: 2025-05-09 02:11:17

如有修改或改动，关注文章底部留言！教程对你有用，可以 “**点赞** ” 和 “**打赏** ”支持 ~

  


  


<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km4Uo9Iuf0zetHedAN6FeZPZ5G2P0aLpdXL4sQJgAMJuf1czXtzuVkk4zTjHcCvKbiajsEZ73cC1u0Q/640?wx_fmt=png&from=appmsg' />

EasyVoice：

一个开源的文本、小说智能转语音解决方案，旨在帮助用户轻松将文本内容转换为高质量的语音输出。

<img src='https://mmbiz.qpic.cn/sz_mmbiz_jpg/5xFLia3A3km4Uo9Iuf0zetHedAN6FeZPZzFql7Agj8yRmW9ClAmYT4Brr1LamCsdGd1zE6sejrYtK8IQGpMcnDw/640?wx_fmt=jpeg&from=appmsg' />

核心功能：

  * • 文本转语音 📝 ➡️ 🎵  
一键将大段文本转为语音，高效又省时。
  * • 流式传输 🌊  
再多的文本，都可以迅速返回音频直接开始试听！
  * • 多语言支持 🌍  
支持中文、英文等多种语言。
  * • 字幕支持 💬  
自动生成字幕文件，方便视频制作和字幕翻译。
  * • 角色配音 🎭  
提供多种声音选项，完美适配不同角色。
  * • 自定义设置 ⚙️  
可调整语速、音调等参数，打造专属语音风格。
  * • AI 推荐 🧠  
通过 AI 智能推荐最适合的语音配置，省心又贴心。
  * • 试听功能 🎧  
生成前可试听效果，确保每一句都如你所愿！



在线演示站：

https://easyvoice.ioplus.tech/

### 安装

Docker Compose
    
    
    services:  
     easyvoice:  
      image: cosincox/easyvoice:latest  
      container_name: easyvoice  
      ports:  
       - 3000:3000  
      volumes:  
       - /vol1/1000/docker/easyvoice:/app/audio  
      restart: always

参数说明（更多参数设置建议去看文档）

:::  
OPENAI_BASE_URL（可选，环境变量）：OpenAI 兼容 API 地址

OPENAI_API_KEY（可选，环境变量）：OpenAI API Key

MODEL_NAME（可选，环境变量）：使用的模型名称

:::

### 使用

浏览器中输入 `http://NAS的IP:3000` 就能看到界面

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km4Uo9Iuf0zetHedAN6FeZPZEtp8Mj9oL988NQBWWg06Z7gr2oV9QYt5SuIsiaSVjSSOWNdItYcKqvw/640?wx_fmt=png&from=appmsg' />

点击“立即体验”

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km4Uo9Iuf0zetHedAN6FeZPZAnfiac1uDtauVQztSLd4d6N2bYNew71eN55y4nePxQ4sMicLhpiahSkibA/640?wx_fmt=png&from=appmsg' />

进入到控制面板

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km4Uo9Iuf0zetHedAN6FeZPZGVMf7WrppuvpuXfLUywiaJZvMYyWRQSJ0Y2icXesVoSRyyOZt34FZ20A/640?wx_fmt=png&from=appmsg' />

可以按需要调节想要的效果，点击试听就会生成语音了

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km4Uo9Iuf0zetHedAN6FeZPZVRzU17srPpfr3fGbQYMo5ex3Jy4czqc6BbxFbUC3nbCKx1PROImicHA/640?wx_fmt=png&from=appmsg' />

也可以使用 AI 推荐（其实也是用预设的语音，不过是 AI 进行自动选择）

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km4Uo9Iuf0zetHedAN6FeZPZg6nseibLfMdTicCBG4HtMD21rABibkN5NgyTcJytUWsN6hmRZg3QF8oXQ/640?wx_fmt=png&from=appmsg' />

这里粘贴了一段文本作为测试，点击生成语音

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km4Uo9Iuf0zetHedAN6FeZPZuxkXTAn8icDkT0O8Pic7Owl0jabtQKLgpUQvYmvaJDoexsdmwlrfC0zA/640?wx_fmt=png&from=appmsg' />

生成完毕，可以点击播放和下载

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km4Uo9Iuf0zetHedAN6FeZPZ08p2xGqO0FgpZ8SqlNbTC5mP14cYhdeicvjLibt5SZA0YzuSvKXTvnLQ/640?wx_fmt=png&from=appmsg' />

生成语音期间，资源占用情况很小

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km4Uo9Iuf0zetHedAN6FeZPZGraHcGDjiaNyC8zKzZIb2WdTlqgjO82hO0OIicibe4OwOBIc130wRLQXw/640?wx_fmt=png&from=appmsg' />

最后我还用 AI 生成的一段多角色对话文本进行测试，确实是会自动切换不同角色进行对话

<img src='https://mmbiz.qpic.cn/sz_mmbiz_png/5xFLia3A3km4Uo9Iuf0zetHedAN6FeZPZpUL5hibqQaoHpAsQIQb6zNg06RJu5Jq9FWiafdPTsyApPswrp9yGmgbA/640?wx_fmt=png&from=appmsg' />

### 总结

之前也部署过另外一个 TTS 工具，但是资源占用太大了基本吃满性能。目前使用下来这款基本不需要什么性能就可以轻松生成语音了，而且可以使用 AI 自动分配角色语音还是比较智能的。

综合推荐：⭐⭐⭐（有一定实用性）

使用体验：⭐⭐⭐（使用简单，消耗资源低）

部署难易：⭐（非常简单）︎

  


  


  


︎