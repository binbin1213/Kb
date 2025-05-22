#!/bin/bash

# 设置GitHub SSH密钥认证的脚本
echo "开始设置GitHub SSH密钥认证..."

# 检查是否已经存在SSH密钥
if [ ! -f ~/.ssh/id_rsa.pub ]; then
    echo "生成SSH密钥..."
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
fi

# 显示公钥，用于添加到GitHub
echo "请将以下公钥添加到GitHub账户的SSH密钥中："
cat ~/.ssh/id_rsa.pub
echo ""
echo "在GitHub网站上，点击右上角头像 -> Settings -> SSH and GPG keys -> New SSH key"
echo "将上面的公钥复制粘贴到Key字段中，然后点击Add SSH key"

# 等待用户确认
read -p "已添加SSH密钥到GitHub? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    # 测试SSH连接
    echo "测试SSH连接..."
    ssh -T git@github.com
    
    # 更改远程仓库URL为SSH方式
    echo "更改远程仓库URL为SSH方式..."
    REPO_NAME=$(git remote get-url origin | sed 's/.*\/\([^\/]*\)$/\1/' | sed 's/\.git$//')
    GITHUB_USERNAME=$(git remote get-url origin | sed 's/.*github.com\/\([^\/]*\).*/\1/')
    
    git remote set-url origin git@github.com:$GITHUB_USERNAME/$REPO_NAME.git
    
    echo "远程仓库URL已更改为: git@github.com:$GITHUB_USERNAME/$REPO_NAME.git"
    echo "设置完成！现在您可以使用SSH密钥认证推送到GitHub。"
else
    echo "操作取消。请手动完成SSH密钥设置。"
fi 