import os
import json
from typing import Optional
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SSH_KEY_FILE = os.path.join(os.path.dirname(__file__), 'ssh_keys.json')


def save_ssh_key(key_name: str, ssh_key: str) -> None:
    try:
        keys = load_ssh_keys()
        keys[key_name] = ssh_key
        with open(SSH_KEY_FILE, 'w', encoding='utf-8') as f:
            json.dump(keys, f, ensure_ascii=False, indent=2)
        logger.info(f'成功保存 SSH 密钥: {key_name}')
    except Exception as e:
        logger.error(f'保存 SSH 密钥失败: {str(e)}')


def load_ssh_keys() -> dict:
    try:
        if os.path.exists(SSH_KEY_FILE):
            with open(SSH_KEY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        logger.error(f'加载 SSH 密钥失败: {str(e)}')
    return {}


def get_ssh_key(key_name: str) -> Optional[str]:
    keys = load_ssh_keys()
    return keys.get(key_name)