import rsa

# 导入密钥
with open('public.pem','r') as pub:
    pubkey = rsa.PublicKey.load_pkcs1(pub.read().encode())
	
with open('private.pem','r') as pri:
    privkey = rsa.PrivateKey.load_pkcs1(pri.read().encode())

with open('encryption.txt', 'rb') as enc:
	crypto = enc.read()

# 私钥解密
message = rsa.decrypt(crypto, privkey).decode()
print(message)

# 私钥签名
signature = rsa.sign(message.encode(), privkey, 'SHA-1')

# 公钥验证
rsa.verify(message.encode(), signature, pubkey)

pri.close()
pub.close()
enc.close()