#!/usr/bin/env python
import plyvel

# 打开 Rime 的 LevelDB 数据库
db = plyvel.DB('./rime_ice.userdb', create_if_missing=False)

for key, value in db:
	print(f"Key: {key.decode('utf-8')}, Value: {value}")

db.close()
