import rsa

# 生成密钥
(pubkey, privkey) = rsa.newkeys(1024)

# 保存密钥
with open('public.pem','w+') as pub:
	pub.write(pubkey.save_pkcs1().decode())
pub.close()

with open('private.pem','w+') as pri:
    pri.write(privkey.save_pkcs1().decode())
pri.close()