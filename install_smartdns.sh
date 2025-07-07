#!/bin/bash

set -e

echo "📦 下载并安装 SmartDNS..."
cd /tmp
wget https://github.com/pymumu/smartdns/releases/download/Release46.1/smartdns.1.2025.03.02-1533.x86_64-linux-all.tar.gz
tar zxvf smartdns.1.2025.03.02-1533.x86_64-linux-all.tar.gz
cd smartdns
sudo ./install -i

echo "🧹 清理旧配置..."
sudo rm -f /etc/smartdns/smartdns.conf
sudo mkdir -p /etc/smartdns

echo "🧠 写入主配置 smartdns.conf..."
cat <<EOF | sudo tee /etc/smartdns/smartdns.conf
# 基础设置
dual-stack-mode yes
speed-check-mode ping-tcp:443
prefetch-domain yes
cache-size 4096

# 监听端口
bind 127.0.0.1:6053
bind-tcp 127.0.0.1:6053

# 国内 DNS
server 114.114.114.114 -group china
server 223.5.5.5 -group china

# 国外 DNS（通过 OpenClash 代理）
server https://dns.google/dns-query -group foreign -http-proxy 192.168.1.101:7893
server https://cloudflare-dns.com/dns-query -group foreign -http-proxy 192.168.1.101:7893
server https://dns.quad9.net/dns-query -group foreign -http-proxy 192.168.1.101:7893

# 引入规则
conf-file /etc/smartdns/china_list_for_smartdns/accelerated-domains.china.domain.smartdns.conf
conf-file /etc/smartdns/china_list_for_smartdns/gfwlist.domain.smartdns.conf
conf-file /etc/smartdns/china_list_for_smartdns/apple.china.domain.smartdns.conf
conf-file /etc/smartdns/china_list_for_smartdns/google.china.domain.smartdns.conf
EOF

echo "📥 克隆规则仓库..."
cd /etc/smartdns
sudo git clone https://github.com/Olixn/china_list_for_smartdns.git

echo "🕓 设置自动更新规则任务..."
(crontab -l 2>/dev/null; echo "0 4 * * * /etc/smartdns/china_list_for_smartdns/update_rules.sh && systemctl restart smartdns") | crontab -

echo "🚀 重启 SmartDNS..."
sudo systemctl daemon-reload
sudo systemctl restart smartdns
sudo systemctl enable smartdns

echo "✅ 安装完成！请在 AdGuard Home 中设置上游 DNS 为：127.0.0.1:6053"
