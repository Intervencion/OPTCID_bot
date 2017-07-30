import sys
import re
import telebot
from telebot import types
import time 
import json
import urllib
import random
import os
import six
import socket
import requests
from collections import OrderedDict
from colorclass import Color
from io import StringIO

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan} OPTCID iniciado.{/cyan}'))


import sqlite3
con = sqlite3.connect('optc.db',check_same_thread = False)
c = con.cursor()
pkmn = ""

TOKEN = ""


usuarios = [line.rstrip('\n') for line in open('users.txt')] 
admins = [1896312]

bot = telebot.TeleBot(TOKEN) 
hora = time.strftime("%Y-%m-%d %H:%M:%S")

try:
	bot.send_message(admins[0], "@OPTCID_bot ha sido encendido")
except Exception as e:
	bot.send_message(admins[0], str(e))

def listener(messages):
	for m in messages:
		cid = m.chat.id
		uid = m.from_user.id
		uname = m.from_user.username
		mct = m.chat.title
		ufm = m.from_user.first_name
		ulm = m.from_user.last_name			
		if m.text:
			mensaje = f"{{autogreen}}User:{{/green}} {ufm}\n"
			if cid < 0:
				mensaje += f"{{autoyellow}}Chat:{{/yellow}} {mct}\n"
				mensaje += f"{{autored}}Hora:{{/red}} {hora}\n"
				mensaje += f"{{autocyan}}UserID:{{/cyan}} [{uid}]"
				mensaje += f"{{autoblue}} ChatID:{{/blue}} [{cid}]"
				mensaje += "\n"
				mensaje += f"{{automagenta}}Mensaje:{{/magenta}} {m.text}\n"
				mensaje += "{autoblack}-------------------------------{/black}\n"
			else:
				mensaje += f"{{autored}}Hora:{{/red}} {hora}\n"
				mensaje += f"{{autocyan}}UserID:{{/cyan}} [{uid}] "
				mensaje += f"{{automagenta}}Mensaje:{{/magenta}} {m.text}\n"
				mensaje += "{autoblack}-------------------------------{/black}\n"
				
			if m.text.startswith("/"):
				f = open('log.txt', 'a')
				f.write(mensaje)
				f.close()
				patata = open('id.txt', 'a')
				patata.write(f'@{uname} [{uid}]\n')
				patata.close()
				print (Color(str(mensaje)))
	#	if m.content_type == 'new_chat_members':
			@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
			def on_user_joins(m):
				cid = m.chat.id
				mct = m.chat.title
				bienvenida = ""
				if(m.new_chat_member.username=="OPTCID_bot"):
					l= 1
				
				else:
					if (m.new_chat_member.username is None):
						nmusername = ""
						nmusername += m.new_chat_member.first_name
						if (m.new_chat_member.last_name is not None):
							nmusername += " "
							nmusername += m.new_chat_member.last_name
							mct = m.chat.title
						else: 
							mct = m.chat.title
					else:
						nmusername = "@" + m.new_chat_member.username
					rules = ""
					if str(cid) == "-1001089561912": #English#
						bienvenida += f"Welcome to {mct} "
						rules += "1) *Speak English.*\n"
						rules += "2) Be nice.\n"
						rules += "3) Don't spoil.\n"
						rules += "4) Don't spam.\n"
						rules += "5) No +18.\n"
						rules += "6) No acc selling."
						italian = "[Italian](https://t.me/joinchat/ABzveENpurD6yuLWuTL18Q)"
						spanish = "[Spanish](https://t.me/joinchat/ABzveENMOZg4ZCXSqfziGA)"
						rules += "Join our {italian} or {spanish} group!"
						bot.send_message(cid, f"{bienvenida}{nmusername}\nPlease follow the rules\n{rules}", parse_mode = "Markdown")	
					elif str(cid) == "-1001129068952": #Spain#
						bienvenida += f"Bienvenidos a {mct} "
						rules += "1) Se amable.\n"
						rules += "3) No spoilers.\n"
						rules += "4) No spam.\n"
						rules += "5) No +18.\n"
						rules += "6) Nada de compra-venta de cuentas."
						bot.send_message(cid, f"{bienvenida}{nmusername}\nRespetad las reglas:\n{rules}", parse_mode = "Markdown")	
					#elif str(cid) == "-1001131002544": #Italy#
						#bienvenida += f"Welcome to {mct} @"
						#rules = "1) speak English.\n"
						#rules += "2) be nice.\n"
						#rules += "3) don't spoil.\n"
						#rules += "4) don't spam.\n"
						#rules += "5) No +18.\n"
						#rules += "6) No acc selling."
						#bot.send_message(cid, f"{bienvenida}{nmusername}\nPlease follow the rules\n{rules}", parse_mode = "Markdown")
					#elif str(cid) == "-1001123740312": #asd#
					#	print("asd")
						#bienvenida += f"Welcome to {mct} "
						#rules += "1) Speak English.\n"
						#rules += "2) Be nice.\n"
						#rules += "3) Don't spoil.\n"
						#rules += "4) Don't spam.\n"
						#rules += "5) No +18.\n"
						#rules += "6) No acc selling."
						#bot.send_message(cid, f"{bienvenida}{nmusername}\nPlease follow the rules\n{rules}", parse_mode = "Markdown")	
					#elif str(cid) == "-182480289": #asdasd#
						#print("asdasd")
						#bienvenida += f"Welcome to {mct} "
						#rules += "1) Speak English.\n"
						#rules += "2) Be nice.\n"
						#rules += "3) Don't spoil.\n"
						#rules += "4) Don't spam.\n"
						#rules += "5) No +18.\n"
						#rules += "6) No acc selling."
						#bot.send_message(cid, f"{bienvenida}{nmusername}\nPlease follow the rules\n{rules}", parse_mode = "Markdown")	
					else:
						print ("entro al else")
						mct = m.chat.title

bot.set_update_listener(listener)


@bot.message_handler(commands=['start'])
def command_start(m):
	cid = m.chat.id
	comandos = "Avaible commands on @OPTCID\_bot:\n"
	comandos += "`/add` - The format of the command is `/add Region XXXXXXXXX` where `Region` is `Japan` or `Global` and `X` are numbers.\n"
	comandos += "`/edit` - The format of the command is `/edit Region XXXXXXXXX` where `Region` is `Japan` or `Global` and `X` are numbers.\n"
	comandos += "`/id` - The format of the command is `/id Region` where `Region` is `Japan` or `Global`.\n"
	comandos += "`/myid` - The format of the command is `/myid Region` where `Region` is `Japan` or `Global`.\n"
	comandos += "`/del` - The format of the command is `/del Region` where `Region` is `Japan` or `Global`."
	bot.send_message(cid, comandos, parse_mode="Markdown")
	
@bot.message_handler(commands=['eg'])
def command_eg(m):
	cid = m.chat.id
	EG = existeGrupo(cid)
	if(EG == 1):
		bot.send_message(cid, "El grupo existe en la BD",
						 parse_mode="Markdown")
	else:
		bot.send_message(cid, "El grupo NO existe en la BD",
						 parse_mode="Markdown")

def existeGrupo(cid):
	c.execute(f"SELECT COUNT(*) FROM GRUPO WHERE idGrupo ='{cid}'")
	try:
		for i in c:
			print("Vamos a ver si el select del Grupo ha devuelto algún elemento")
			print(f"El resultado del select es: {i[0]}")
			EG = i[0]
#		r = c.fetchone()
#		print("Vamos a ver si el select del Grupo ha devuelto algún elemento")
#		print(f"El resultado del select es: {i[0]}")
#		EG = r[0]
	
	except Exception as e:
		print(e)
		print("Estamos aquí porque el select nos ha devuelto un elemento vacío")
		EG = 0
	
	return EG

def existeUser(uid):
	c.execute(f"SELECT COUNT(*) FROM Usuarios WHERE idUsuario ='{uid}'")
	try:
		for i in c:
			print("Vamos a ver si el select de Usuarios ha devuelto algún elemento")
			print(f"El resultado del select es: {i[0]}")
			EU = i[0]
#		r = c.fetchone()
#		print("Vamos a ver si el select de Usuarios ha devuelto algún elemento")
#		print(f"El resultado del select es: {i[0]}")
#		EU = r[0]
	
	except Exception as e:
		print(e)
		print("Estamos aquí porque el select nos ha devuelto un elemento vacío")
		EU = 0
	
	return EU

def existeUserGru(uid,cid):
	c.execute(f"SELECT COUNT(*) FROM UsuGrupo WHERE idUsuarioFK ='{uid}' AND idGrupoFK ='{cid}'")
	try:
		for i in c:
			print("Vamos a ver si el select de UsuGrupo ha devuelto algún elemento")
			print(f"El resultado del select es: {i[0]}")
			EUG =i[0]
	
	except Exception as e:
		print(e)
		print("Estamos aquí porque el select nos ha devuelto un elemento vacío")
		EUG = 0
	print(f"Vamos a devolver el valor de EUG que es {EUG}")
	return EUG

@bot.message_handler(commands=['id'])
def command_id(m):
	cid = m.chat.id 
	uname = m.from_user.username
	uid = m.from_user.id
	arrayl = []
	try:
		oioi = m.text.split(' ', 1)[1].capitalize()
		print(oioi)
		if (oioi.startswith("Japan")):
			try:
				print("entro en el try")
				c.execute(f"SELECT idUsuario,NombreUsuario,idJapan FROM Usuarios INNER JOIN UsuGrupo ON Usuarios.idUsuario = UsuGrupo.idUsuarioFK WHERE UsuGrupo.idGrupoFK ='{cid}' ORDER BY NombreUsuario ASC")
				print("hago el for?")
				for i in c:
					print("1")
					if i[2] is None:
						print("No entran los vacíos.")
					else:
						NombreUsuario_resultado = f'{i[1]}: '
						print("2)" + str(NombreUsuario_resultado))
						idOP_resultado = i[2]
						idOP_resultado = str(idOP_resultado).zfill(9)
					#	if idOP_resultado is None:
					#		idOP_resultado = i[2]
						print("3)" + str(idOP_resultado))
						p = f'*{NombreUsuario_resultado}* `{idOP_resultado}`'
						print("4" + str(p))
						arrayl.append(p)
						print("5")
				f = str(arrayl).replace(" '","").replace("'","")
				f = f.replace(",", "\n").replace("[","").replace("]","")
				if not f:
					f = "The DB is empty. Please add yourself with `/add Region XXXXXXXXX` where `Region` is `Japan` and X are numbers."
					bot.send_message(cid, f'{f}', parse_mode = "Markdown")
					con.commit()
				elif (f == None):
					f = "The DB is empty. Please add yourself with `/add Region XXXXXXXXX` where `Region` is `Japan` and X are numbers."
					bot.send_message(cid, f'{f}', parse_mode = "Markdown")
					con.commit()
				else:
					bot.send_message(cid, f'{f}', parse_mode = "Markdown")
					con.commit()
			
			except:
				bot.send_message(cid, "An error ocurred. Report to @Intervencion.")
				
		elif (oioi.startswith("Global")):
			try:
			
				c.execute(f"SELECT idUsuario,NombreUsuario,idGlobal FROM Usuarios INNER JOIN UsuGrupo ON Usuarios.idUsuario = UsuGrupo.idUsuarioFK WHERE UsuGrupo.idGrupoFK ='{cid}' ORDER BY NombreUsuario ASC")
				print("hago el for?")
				for i in c:
					print("1")
					if i[2] is None:
						print("No entran los vacíos.")
					else:
						NombreUsuario_resultado = f'{i[1]}: '
						print("2)" + str(NombreUsuario_resultado))
						idOP_resultado = i[2]
						idOP_resultado = str(idOP_resultado).zfill(9)
					#	if idOP_resultado is None:
					#		idOP_resultado = i[2]
						print("3)" + str(idOP_resultado))
						p = f'*{NombreUsuario_resultado}* `{idOP_resultado}`'
						print("4" + str(p))
						arrayl.append(p)
						print("5")
				f = str(arrayl).replace(" '","").replace("'","")
				f = f.replace(",", "\n").replace("[","").replace("]","")
				if not f:
					f = "The DB is empty. Please add yourself with `/add Region XXXXXXXXX` where `Region` is `Global` and X are numbers."
					bot.send_message(cid, f'{f}', parse_mode = "Markdown")
					con.commit()
				elif (f == None):
					f = "The DB is empty. Please add yourself with `/add Region XXXXXXXXX` where `Region` is `Global` and X are numbers."
					bot.send_message(cid, f'{f}', parse_mode = "Markdown")
					con.commit()
				else:
					bot.send_message(cid, f'{f}', parse_mode = "Markdown")
					con.commit()
			
			except:
				bot.send_message(cid, "An error ocurred. Report to @Intervencion.")
		else:
			bot.send_message(cid, "ElseError: The format of the command is `/id Region` where `Region` is `Japan` or `Global`.", parse_mode="Markdown")
	except:
		bot.send_message(cid, "ElseError: The format of the command is `/id Region` where `Region` is `Japan` or `Global`.", parse_mode="Markdown")

@bot.message_handler(commands=['add'])
def command_addidOP(m):
	cid = m.chat.id
	uid = m.from_user.id
	mct = m.chat.title
	ufm = m.from_user.first_name
	ulm = m.from_user.last_name
	if (m.from_user.username is None):
		if (ulm is None):
			uname = ufm
		else:
			uname = f'{ufm} {ulm}'
	else:
		uname = m.from_user.username
	if(cid>0):
		bot.send_message(cid,"This only works in groups.")
	else:
		print(str(cid))
		print("VAMOS A LEERLO SIN TRY")
		try:
			idOP = m.text.split(' ', 1)[1].replace(" ", "").replace(".", "").replace(",", "").lower().capitalize()
			print(idOP)
			if (idOP.startswith("Jap") or idOP.startswith("Jpn")):
				print(str(idOP))
				print("Entro capitalizado. Voy a splitear.")
				idOP = idOP.replace("Japan", "Jap")
				idOP = idOP.replace("Jap", "Japan")
				idOP = idOP.replace("Jpn", "Japan")
				idOP = idOP.split("Japan", 1)[1]
				idOP = idOP.replace(" ", "")
				print("He spliteado. Voy a crear el patrón.")
				pattern = '^\d\d\d\d\d\d\d\d\d$'
				print("creado el patrón, voy a comprobar que coincide")
				if re.match(pattern, idOP, flags=0):
					print("He entrado comprovando que el patrón es bueno")
					print("voy a mirar si el grupo ya existe")
					EG = existeGrupo(cid)
					if (EG == 0):
						print("El Grupo no existe, ergo tengo que crearlo")
						print(m.chat.title)
						print(f"El nombre del chat es: {mct}")
						print("Ahora vamos a hacer el insert en el grupo")
						try:
							c.execute(f"INSERT INTO Grupo (idGrupo,NombreGrup) VALUES ('{cid}','{mct}')")
							print(f"El id del grupo {cid}")
							EU = existeUser(uid)
							if(EU == 0):
								c.execute(f"INSERT INTO Usuarios (idUsuario,NombreUsuario,idJapan) VALUES ('{uid}','@{uname}','{idOP}')")								
								c.execute(f"UPDATE Usuarios SET 'idJapan' = '{idOP}','NombreUsuario'='@{uname}' WHERE idUsuario = '{uid}'")
							print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0")
							c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK,idGrupoFK, Region) VALUES ('{uid}','{cid}',Japan)")
							bot.send_message(cid, f"*{uname}* has been added to the DB with Japanese Pirate ID *{idOP}*.", parse_mode="Markdown")
							con.commit()
						except sqlite3.Error as e:
							print(e)
							bot.send_message(cid, f"*{uname}* has been added to the DB with Japanese Pirate ID *{idOP}*.", parse_mode="Markdown")
					elif(EG == 1):
						print("El grupo sí existe")
						try:
							EU = existeUser(uid)
							if(EU == 0):
								c.execute(f"INSERT INTO Usuarios (idUsuario,NombreUsuario,idJapan) VALUES ('{uid}', '@{uname}','{idOP}')")
								#bot.send_message(cid, f"*{uname}* has been added to the DB with Japanese Pirate ID *{idOP}*.", parse_mode="Markdown")
							#else:
								print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0 Y AHORA VOY A COMPROBAR EUG")
								EUG = existeUserGru(uid,cid)
								print(f"Sabemos que EUG vale {EUG}")
								if(EUG == 0):
									print("Entro cuando no existe la combinación usuario - grupo")
									c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK,idGrupoFK,Region) VALUES ('{uid}','{cid}',Japan)")
									bot.send_message(cid, f"*{uname}* has been added to the DB with Japanese Pirate ID *{idOP}*.", parse_mode="Markdown")
								elif(EUG == 1):
									bot.send_message(cid, "You have already introduced your Japanese Pirate ID in this group, if you want to edit it use `/edit Japan`", parse_mode="Markdown")
								else:
									bot.send_message(cid, "Error in EUG.")
								con.commit()
							else:
								bot.send_message(-1001113426399, "patata", parse_mode="Markdown")
						except sqlite3.Error as e:
							print(e)
							bot.send_message(cid, "You have already introduced your Japanese Pirate ID in this group, if you want to edit it use `/edit Japan`", parse_mode="Markdown")
				else:
					bot.send_message(cid, "ElseError: The format of the command is `/add Region XXXXXXXXX` where `Region` is `Japan` or `Global` and X are numbers.", parse_mode="Markdown")
			elif (idOP.startswith("Global")):
				print(str(idOP))
				print("Entro capitalizado. Voy a splitear.")
				idOP = idOP.split("Global", 1)[1]
				idOP = idOP.replace(" ", "")
				print("He spliteado. Voy a crear el patrón.")
				pattern = '^\d\d\d\d\d\d\d\d\d$'
				print("creado el patrón, voy a comprobar que coincide")
				if re.match(pattern, idOP, flags=0):
					print("He entrado comprovando que el patrón es bueno")
					print("voy a mirar si el grupo ya existe")
					EG = existeGrupo(cid)
					if (EG == 0):
						print("El Grupo no existe, ergo tengo que crearlo")
						print(m.chat.title)
						print(f"El nombre del chat es: {mct}")
						print("Ahora vamos a hacer el insert en el grupo")
						try:
							c.execute(f"INSERT INTO Grupo (idGrupo,NombreGrup) VALUES ('{cid}','{mct}')")
							print(f"El id del grupo {cid}")
							bot.send_message(-1001113426399, f"El id del grupo {cid}", parse_mode="Markdown")
							EU = existeUser(uid)
							if(EU == 0):
								c.execute(f"INSERT INTO Usuarios (idUsuario,NombreUsuario,idGlobal) VALUES ('{uid}','@{uname}','{idOP}')")
								bot.send_message(-1001113426399, "EU = 0", parse_mode="Markdown")
							print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0")
							bot.send_message(-1001113426399, "ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0", parse_mode="Markdown")
							c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK,idGrupoFK, Region) VALUES ('{uid}','{cid}','Global')")
							bot.send_message(cid, f"*{uname}* has been added to the DB with Global Pirate ID *{idOP}*.", parse_mode="Markdown")
							con.commit()
						except sqlite3.Error as e:
							print(e)
							bot.send_message(cid, f"*{uname}* has been added to the DB with Global Pirate ID *{idOP}*.", parse_mode="Markdown")
					elif(EG == 1):
						print("El grupo sí existe")
						#bot.send_message(-1001113426399, "El grupo sí existe", parse_mode="Markdown")
						try:
							EU = existeUser(uid)
							if(EU == 0):
								c.execute(f"INSERT INTO Usuarios (idUsuario, NombreUsuario, idGlobal) VALUES ('{uid}', '@{uname}','{idOP}')")
								#bot.send_message(-1001113426399, "EU = 0", parse_mode="Markdown")
								#bot.send_message(cid, f"*{uname}* has been added to the DB with Global Pirate ID *{idOP}*.", parse_mode="Markdown")
							#else:
								print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0 Y AHORA VOY A COMPROBAR EUG")
								#bot.send_message(-1001113426399, "ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0 Y AHORA VOY A COMPROBAR EUG", parse_mode="Markdown")
								EUG = existeUserGru(uid,cid)
								print(f"Sabemos que EUG vale {EUG}")
								if(EUG == 0):
									print("Entro cuando no existe la combinación usuario - grupo")
									c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK,idGrupoFK,Region) VALUES ('{uid}','{cid}','Global')")
								#	bot.send_message(-1001113426399, "Entro cuando no existe la combinación usuario - grupo", parse_mode="Markdown")
									bot.send_message(cid, f"*{uname}* has been added to the DB with Global Pirate ID *{idOP}*.", parse_mode="Markdown")
								elif(EUG == 1):
									bot.send_message(cid, "You have already introduced your Global Pirate ID in this group, if you want to edit it use `/edit Global`", parse_mode="Markdown")
								else:
									bot.send_message(cid, "Error in EUG.")
								con.commit()
							else:
								bot.send_message(-1001113426399, "patata", parse_mode="Markdown")
						except sqlite3.Error as e:
							print(e)
							bot.send_message(cid, "You have already introduced your Global Pirate ID in this group, if you want to edit it use `/edit Global`", parse_mode="Markdown")
				else:
					bot.send_message(cid, "ElseError: The format of the command is `/add Region XXXXXXXXX` where `Region` is `Japan` or `Global` and X are numbers.", parse_mode="Markdown")
		except:
			bot.send_message(cid, "ExceptError: The format of the command is `/add Region XXXXXXXXX` where `Region` is `Japan` or `Global` and X are numbers.", parse_mode="Markdown")


@bot.message_handler(commands=['edit']) 
def command_editidOP(m):
	cid = m.chat.id
	uid = m.from_user.id
	ufm = m.from_user.first_name
	ulm = m.from_user.last_name
	if (m.from_user.username is None):
		if (ulm is None):
			uname = ufm
		else:
			uname = f'{ufm} {ulm}'
	else:
		uname = m.from_user.username
	try:
		idOP = m.text.split(' ', 1)[1].replace(" ", "").replace(".", "").capitalize()
		print(idOP)
		if (idOP.startswith("Japan")):
			try:
				pattern = '^\d\d\d\d\d\d\d\d\d$'
				idOP = idOP.split("Japan", 1)[1]
				if re.match(pattern, idOP, flags=0):
					try:
					  c.execute(f"UPDATE Usuarios SET 'idJapan' = '{idOP}','NombreUsuario'='@{uname}' WHERE idUsuario = '{uid}'")
					  bot.send_message(cid, f"*{uname}* now have Japanese Pirate ID *{idOP}*.", parse_mode = "Markdown")
					  con.commit()
		
					except sqlite3.Error:
					  bot.send_message(cid, "ExceptError: The format of the command is `/edit Region XXXXXXXXX` where `Region` is `Japan` and X are numbers.", parse_mode="Markdown")
				else:
					
					bot.send_message(cid, "ElseError: The format of the command is `/edit Region XXXXXXXXX` where `Region` is `Japan` and X are numbers.", parse_mode="Markdown")
			  
			except:
				bot.send_message(cid, "ExceptError: The format of the command is `/edit Region XXXXXXXXX` where `Region` is `Japan` and X are numbers.", parse_mode="Markdown")


		if (idOP.startswith("Global")):
			try:
				pattern = '^\d\d\d\d\d\d\d\d\d$'
				idOP = idOP.split("Global", 1)[1]
				if re.match(pattern, idOP, flags=0):
					try:
					  c.execute(f"UPDATE Usuarios SET 'idGlobal' = '{idOP}','NombreUsuario'='@{uname}' WHERE idUsuario = '{uid}'")
					  bot.send_message(cid, f"*{uname}* now have Global  Pirate ID *{idOP}*.", parse_mode = "Markdown")
					  con.commit()
		
					except sqlite3.Error:
					  bot.send_message(cid, "ExceptError: The format of the command is `/edit Region XXXXXXXXX` where `Region` is `Global` and X are numbers.", parse_mode="Markdown")
				else:
					
					bot.send_message(cid, "ElseError: The format of the command is `/edit Region XXXXXXXXX` where `Region` is `Global` and X are numbers.", parse_mode="Markdown")
			  
			except:
				bot.send_message(cid, "ExceptError: The format of the command is `/edit Region XXXXXXXXX` where `Region` is `Global` and X are numbers.", parse_mode="Markdown")
	except:
		bot.send_message(cid, "ExceptError: The format of the command is `/edit Region XXXXXXXXX` where `Region` is `Japan` or `Global` and X are numbers.", parse_mode="Markdown")
		

@bot.message_handler(commands=['del']) 
def command_deleteidOP(m):
	cid = m.chat.id
	uid = m.from_user.id
	ufm = m.from_user.first_name
	ulm = m.from_user.last_name
	if (m.from_user.username is None):
		if (ulm is None):
			uname = ufm
		else:
			uname = f'{ufm} {ulm}'
	else:
		uname = m.from_user.username
	try:
		idOP = m.text.split(' ', 1)[1].capitalize()
		print(idOP)
		reply = "test"
		if (str(idOP).startswith("Japan")):
			reply = "Your Japanese Pirate ID is not in the DB."
			try:
				print("1")
				c.execute(f"SELECT idJapan FROM Usuarios WHERE idUsuario ='{uid}'")
				print("2")
				for i in c:
					print("3")
					if i[0] is None:
						print("4")
						reply = "Your Japanese Pirate ID is not in the DB."
					else:
						print("5")
						idOP = i[0]
						c.execute(f"DELETE FROM Usuarios WHERE idJapan = '{idOP}'")
						print("6")
						try:
							c.execute(f"SELECT idUsuario,NombreUsuario,idGlobalFROM Usuarios INNER JOIN UsuGrupo ON Usuarios.idUsuario = UsuGrupo.idUsuarioFK WHERE UsuGrupo.idGrupoFK ='{cid}'")
							print("7")
							for j in c:
								print("8")
								c.execute(f"DELETE FROM UsuGrupo WHERE idUsuarioFK ='{uid}'")
								print("9")
								reply = "Your Japanese Pirate ID have been deleted from the BD."
						except:
							print("11) No entra en el for porque no existe ergo = None")
							c.execute(f"DELETE FROM UsuGrupo WHERE idUsuarioFK ='{uid}'")
							print("12")
							reply = "Your Japanese Pirate ID have been deleted from the BD."
							print("13")
				bot.send_message(cid, reply, parse_mode = "Markdown")
				con.commit()
			except sqlite3.Error:
			  bot.send_message(cid, "ExceptError: The format of the command is `/del Region` where `Region` is `Japan`.", parse_mode="Markdown")

		elif (str(idOP).startswith("Global")):
			reply = "Your Global Pirate ID is not in the DB."
			try:
				print("1")
				c.execute(f"SELECT idGlobal FROM Usuarios WHERE idUsuario ='{uid}'")
				print("2")
				for i in c:
					print("3")
					if i[0] is None:
						print("4")
						reply = "Your Global Pirate ID is not in the DB."
					else:
						print("5")
						idOP = i[0]
						c.execute(f"DELETE FROM Usuarios WHERE idGlobal = '{idOP}'")
						print("6")
						try:
							c.execute(f"SELECT idUsuario,NombreUsuario,idJapan FROM Usuarios INNER JOIN UsuGrupo ON Usuarios.idUsuario = UsuGrupo.idUsuarioFK WHERE UsuGrupo.idGrupoFK ='{cid}'")
							print("7")
							for j in c:
								print("8")
								c.execute(f"DELETE FROM UsuGrupo WHERE idUsuarioFK ='{uid}'")
								print("9")
								reply = "Your Global Pirate ID have been deleted from the BD."
						except:
							print("11) No entra en el for porque no existe ergo = None")
							c.execute(f"DELETE FROM UsuGrupo WHERE idUsuarioFK ='{uid}'")
							print("12")
							reply = "Your Global Pirate ID have been deleted from the BD."
							print("13")
				bot.send_message(cid, reply, parse_mode = "Markdown")
				con.commit()
			except sqlite3.Error:
			  bot.send_message(cid, "ExceptError: The format of the command is `/del Region` where `Region` is `Global`.", parse_mode="Markdown")
		else:
			bot.send_message(cid, "ElseError: The format of the command is `/del Region` where `Region` is `Japan` or `Global`.", parse_mode="Markdown")
	except:
		bot.send_message(cid, "ExceptError: The format of the command is `/del Region` where `Region` is `Japan` or `Global`.", parse_mode="Markdown")


@bot.message_handler(commands=['myid']) 
def command_myidOP(m):
	cid = m.chat.id
	uid = m.from_user.id
	ufm = m.from_user.first_name
	ulm = m.from_user.last_name
	if (m.from_user.username is None):
		if (ulm is None):
			uname = ufm
		else:
			uname = f'{ufm} {ulm}'
	else:
		uname = m.from_user.username
	try:
		idOP = m.text.split(' ', 1)[1].replace(" ", "").capitalize()
		print(idOP)
		if (idOP.startswith("Japan")):
			try:
				c.execute(f"SELECT NombreUsuario,idJapan from Usuarios WHERE idUsuario='{uid}'")
				
				for i in c:
					NombreUsuario_resultado = f"{i[0]} "
					idOP_resultado = i[1]
					
	
				if (idOP_resultado == None):
					bot.send_message(cid, f'Your Japanese Pirate ID is not in the DB.', parse_mode = "Markdown")
					con.commit()
				else:
					idOP_resultado = str(idOP_resultado).zfill(9)
					bot.send_message(cid, f'*{NombreUsuario_resultado}*: `{idOP_resultado}`', parse_mode = "Markdown")
					con.commit()
			except:
				bot.send_message(cid, "Your Japanese Pirate ID is not in the DB.", parse_mode = "Markdown")
		elif (idOP.startswith("Global")):
			try:
				c.execute(f"SELECT NombreUsuario,idGlobal from Usuarios WHERE idUsuario='{uid}'")
				
				for i in c:
					NombreUsuario_resultado = f"{i[0]} "
					idOP_resultado = i[1]
				
				if (idOP_resultado == None):
					bot.send_message(cid, f'Your Global Pirate ID is not in the DB.', parse_mode = "Markdown")
					con.commit()
				else:
					idOP_resultado = str(idOP_resultado).zfill(9)
					bot.send_message(cid, f'*{NombreUsuario_resultado}*: `{idOP_resultado}`', parse_mode = "Markdown")
					con.commit()
			except:
				bot.send_message(cid, "Your Global Pirate ID is not in the DB.", parse_mode = "Markdown")
		else:
			bot.send_message(cid, "ElseError: `/myid` - The format of the command is `/myid Region` where `Region` is `Japan` or `Global`.", parse_mode="Markdown")
	except:
		bot.send_message(cid, "ExceptError: `/myid` - The format of the command is `/myid Region` where `Region` is `Japan` or `Global`.", parse_mode="Markdown")




from config import *

@bot.message_handler(commands=['exec'])
def command_exec(m):
    cid = m.chat.id
    uid = m.from_user.id
    #try:
        #send_udp('exec')
    #except Exception as e:
    #    bot.send_message(1896312, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if m.from_user.id in admins:
        if len(m.text.split()) == 1:
            bot.send_message(
                cid,
                "Uso: /exec _<code>_ - Ejecuta el siguiente bloque de código.",
                parse_mode="Markdown")
            return
        cout = StringIO()
        sys.stdout = cout
        cerr = StringIO()
        sys.stderr = cerr
        code = ' '.join(m.text.split(' ')[1:])
        try:
            exec(code)
        except Exception as e:
            bot.send_message(cid, send_exception(e), parse_mode="Markdown")
        else:
            if cout.getvalue():
                bot.send_message(cid, str(cout.getvalue()))
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        
@bot.message_handler(commands=['restart'])
def command_restart(m):
	if m.from_user.id in admins:
		try:
			os.execl(sys.executable, sys.executable, *sys.argv)
		except:
			bot.send_message(cid, "Mal código tete")
	else:
		bot.send_message(cid, "Comando reservado a SU.")






bot.skip_pending = True
bot.polling(none_stop=True)