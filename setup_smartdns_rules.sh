#!/bin/bash

set -e

echo "📥 克隆规则仓库（如果尚未存在）..."
cd /etc/smartdns
if [ ! -d "china_list_for_smartdns" ]; then
    sudo git clone https://github.com/Olixn/china_list_for_smartdns.git
else
    echo "✅ 规则仓库已存在，跳过克隆。"
fi

echo "🧠 确保 smartdns.conf 引用了规则文件..."
CONF_FILE="/etc/smartdns/smartdns.conf"
for RULE in accelerated-domains.china.domain.smartdns.conf \
            gfwlist.domain.smartdns.conf \
            apple.china.domain.smartdns.conf \
            google.china.domain.smartdns.conf; do
    LINE="conf-file /etc/smartdns/china_list_for_smartdns/$RULE"
    grep -qxF "$LINE" "$CONF_FILE" || echo "$LINE" | sudo tee -a "$CONF_FILE"
done

echo "🕓 设置每日凌晨 4 点自动更新规则..."
CRON_LINE="0 4 * * * /etc/smartdns/china_list_for_smartdns/update_rules.sh && systemctl restart smartdns"
( crontab -l 2>/dev/null | grep -v update_rules.sh ; echo "$CRON_LINE" ) | crontab -

echo "🚀 手动执行一次规则更新并重启 SmartDNS..."
sudo /etc/smartdns/china_list_for_smartdns/update_rules.sh
sudo systemctl restart smartdns

echo "✅ 规则集成与自动更新配置完成！"
