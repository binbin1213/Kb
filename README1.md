# Docker 镜像使用说明

## 前提条件
- 确保你已经安装了 Docker。你可以从 [Docker 官方网站](https://www.docker.com/get-started) 下载并安装。
- 如果你需要使用 GitHub 自动上传功能，需要配置好 GitHub 认证，包括设置好 SSH 密钥或者个人访问令牌（PAT）。

## 镜像拉取
在终端中运行以下命令来从 Docker Hub 拉取镜像：
```bash
docker pull <your-dockerhub-username>/<your-image-name>:<tag>
```
请将 `<your-dockerhub-username>` 替换为你的 Docker Hub 用户名，`<your-image-name>` 替换为你的镜像名称，`<tag>` 替换为镜像标签（通常为 `latest`）。

## 容器运行
### 基本运行
使用以下命令来启动一个新的容器：
```bash
docker run -d \
  -e RSS_URL="https://your-rss-url.com" \
  -v /your/local/downloads:/app/downloads \
  <your-dockerhub-username>/<your-image-name>:<tag>
```
### 参数说明
- `-e RSS_URL`：设置 RSS 订阅的 URL。如果不设置，将使用 Dockerfile 中默认的空值。
- `-v`：将本地目录挂载到容器内的 `/app/downloads` 目录，用于存储下载的文件。

## 环境变量配置
| 环境变量名 | 描述 | 默认值 |
| --- | --- | --- |
| `RSS_URL` | RSS 订阅的 URL | "" |
| `DOWNLOAD_DIR` | 下载文件的存储目录 | `/app/downloads` |

## GitHub 认证配置
如果你想使用 GitHub 自动上传功能，需要确保你的代码仓库已经配置好 GitHub 认证。可以通过以下步骤进行配置：
1. 生成 SSH 密钥（如果还没有）：`ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
2. 将公钥添加到你的 GitHub 账户设置中。
3. 在运行容器时，确保容器能够访问你的 SSH 密钥。可以通过挂载 SSH 密钥目录来实现：
```bash
docker run -d \
  -e RSS_URL="https://your-rss-url.com" \
  -v /your/local/downloads:/app/downloads \
  -v ~/.ssh:/root/.ssh \
  <your-dockerhub-username>/<your-image-name>:<tag>
```

## 注意事项
- 请确保你的 GitHub 仓库有写入权限，否则自动上传功能将失败。
- 定期检查容器的日志，确保 RSS 抓取和 GitHub 上传功能正常工作。