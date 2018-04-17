import rsa

# 导入密钥
with open('public.pem','r') as pub:
    pubkey = rsa.PublicKey.load_pkcs1(pub.read().encode())
	
with open('private.pem','r') as pri:
    privkey = rsa.PrivateKey.load_pkcs1(pri.read().encode())

	
# 明文
#message = 'hello'
message = input('Please input your string: ')

# 公钥加密
crypto = rsa.encrypt(message.encode(), pubkey)
with open('encryption.txt', 'wb') as enc:
	enc.write(crypto)

# 私钥签名
signature = rsa.sign(message.encode(), privkey, 'SHA-1')

# 公钥验证
rsa.verify(message.encode(), signature, pubkey)

pub.close()
pri.close()
enc.close()