from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

# AES加密密钥，需要妥善保管
AES_KEY = b'your_16bytes_key'
cipher = AES.new(AES_KEY, AES.MODE_ECB)
RSS_URL_ENCRYPTED = base64.b64encode(cipher.encrypt(pad(RSS_URL, AES.block_size))).decode('utf-8')
CERT_FILE = "fullchain.cer"
DATA_FILE = "data.json"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
TIMEOUT = 25
RETRIES = 3