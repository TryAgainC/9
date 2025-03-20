# -*- coding: utf-8 -*-
import os
import time
from telethon import TelegramClient, events, sync

api_id = [22369252]	#输入api_id，一个账号一项
api_hash = ['bf24c65b4ab93493fde7d55125244432']	#输入api_hash，一个账号一项

session_name = api_id[:]
for num in range(len(api_id)):
	session_name[num] = "id_" + str(session_name[num])
	client = TelegramClient(session_name[num], api_id[num], api_hash[num])
	client.start()
	client.send_message("@nb3344bot", '签到')	#第一项是机器人ID，第二项是发送的文字
	time.sleep(5)	#延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
	client.send_read_acknowledge("@luxiaoxun_bot")	#将机器人回应设为已读
	print("Done! Session name:", session_name[num])
	
os._exit(0)
