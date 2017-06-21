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
import re
import socket
import requests
from collections import OrderedDict
from colorclass import Color
from io import StringIO

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan} Archivo principal importado.{/cyan}'))

import sqlite3
con = sqlite3.connect('optc.db',check_same_thread = False)
c = con.cursor()
pkmn = ""

TOKEN = '' 


usuarios = [line.rstrip('\n') for line in open('users.txt')] 

bot = telebot.TeleBot(TOKEN) 
hora = time.strftime("%Y-%m-%d %H:%M:%S")

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
			if cid < 0:
				mensaje += f"{{autoblue}} ChatID:{{/blue}} [{cid}]"
				mensaje += "\n"
				mensaje += f"{{automagenta}}Mensaje:{{/magenta}} {m.text}\n"
				mensaje += "{autoblack}-------------------------------{/black}\n"
			else:
				mensaje += f"{{autored}}Hora:{{/red}} {hora}\n"
				mensaje += f"{{autocyan}}UserID:{{/cyan}} [{uid}] "
				mensaje += f"{{automagenta}}Mensaje:{{/magenta}} {m.text}\n"
				mensaje += "{autoblack}-------------------------------{/black}\n"
				
			if(m.text.startswith("!") or m.text.startswith("/")):
				f = open('log.txt', 'a')
				f.write(mensaje)
				f.close()
				patata = open('id.txt', 'a')
				patata.write(f'@{uname} [{uid}]\n')
				patata.close()
				print (Color(str(mensaje)))

bot.set_update_listener(listener)


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
			print("Vamos a ver si el select de grupo ha devuelto algún elemento")
			print(f'El resultado del select es: {i[0]}')
			EG =i[0]
	
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
			EU =i[0]
	
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
def command_idOP(m):
	cid = m.chat.id 
	uname = m.from_user.username
	uid = m.from_user.id
	arrayl = []
	if (m.text.capitalize().startswith("Japan")):
		try:
		
			c.execute(f"SELECT idUsuario,NombreUsuario,idJapan FROM Usuarios INNER JOIN UsuGrupo ON Usuarios.idUsuario = UsuGrupo.idUsuarioFK WHERE UsuGrupo.idGrupoFK ='{cid}' ORDER BY NombreUsuario ASC")
		
		
			for i in c:
				NombreUsuario_resultado = f'{i[1]}: '
				idOP_resultado = i[2]
				p = NombreUsuario_resultado + idOP_resultado
				arrayl.append(p)
			
			f = str(arrayl).replace(" '","").replace("'","")
			f = f.replace(",", "\n").replace("[","").replace("]","")
			print(arrayl)
			bot.send_message(cid, f'*{f}*', parse_mode = "Markdown")
			con.commit()
		
		except:
			bot.send_message(cid, "An error ocurred. Report to @Intervencion.")
			
	elif (m.text.capitalize().startswith("Global")):
		try:
		
			c.execute(f"SELECT idUsuario,NombreUsuario,idGlobal FROM Usuarios INNER JOIN UsuGrupo ON Usuarios.idUsuario = UsuGrupo.idUsuarioFK WHERE UsuGrupo.idGrupoFK ='{cid}' ORDER BY NombreUsuario ASC")
		
		
			for i in c:
				NombreUsuario_resultado = f'{i[1]}: '
				idOP_resultado = i[2]
				p = NombreUsuario_resultado + idOP_resultado
				arrayl.append(p)
			
			f = str(arrayl).replace(" '","").replace("'","")
			f = f.replace(",", "\n").replace("[","").replace("]","")
			print(arrayl)
			bot.send_message(cid, f'*{f}*', parse_mode = "Markdown")
			con.commit()
		
		except:
			bot.send_message(cid, "An error ocurred. Report to @Intervencion.")
		else:
			bot.send_message(cid, "ElseError: The format of the command is `/id Region` where `Region` is `Japan` or `Global`.", parse_mode="Markdown")

@bot.message_handler(commands=['add'])
def command_addidOP(m):
	cid = m.chat.id
	uid = m.from_user.id
	mct = m.chat.title
	ufm = m.from_user.first_name
	ulm = m.from_user.last_name
	if (m.from_user.username is None):
		uname = f'{ufm} {ulm}'
	else:
		uname = m.from_user.username
	if(cid>0):
		bot.send_message(cid,"This only works in groups.")
	elif(cid<0):
		print(str(cid))
		print("VAMOS A LEERLO SIN TRY")
		try:
			idOP = m.text.split(' ', 1)[1].replace(" ", "").capitalize()
			#j = idOP.startswith("Japan")
			#g = idOP.startswith("Global")
			if (m.text.capitalize().startswith("Japan")):
				print(str(idOP))
				print("Entro capitalizado. Voy a splitear.")
				idOP = idOP.split("Japan", 1)[1]
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
							nocapital = uname.capitalize()
							EU = existeUser(uid)
							if(EU == 0):
								c.execute(f"INSERT INTO Usuarios (idUsuario,NombreUsuario,idJapan) VALUES ('{uid}','@{nocapital}','{idOP}')")
							print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0")
							c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK,idGrupoFK,Region) VALUES ('{uid}','{cid}','Japan')")
							bot.send_message(cid, f"*{uname}* has been added to the DB with Japanese Pirate ID *{idOP}*.", parse_mode="Markdown")
							con.commit()
						except sqlite3.Error as e:
							print(e)
							bot.send_message(cid, f"*{uname}* has been added to the DB with Japanese Pirate ID *{idOP}*.", parse_mode="Markdown")
					elif(EG == 1):
						print("El grupo sí existe")
						nocapital = uname.capitalize()
						try:
							EU = existeUser(uid)
							if(EU == 0):
								c.execute(f"INSERT INTO Usuarios (idUsuario,NombreUsuario,idJapan) VALUES ('{uid}', '@{nocapital}','{idOP}')")
							print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0 Y AHORA VOY A COMPROBAR EUG")
							EUG = existeUserGru(uid,cid)
							print("Sabemos que EUG vale " + str(EUG))
							if(EUG == 0):
								print("Entro cuando no existe la combinación usuario - grupo")
								c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK,idGrupoFK,Region) VALUES ('{uid}','{cid}','Japan')")
								bot.send_message(cid, f"*{uname}* has been added to the DB with Japanese Pirate ID *{idOP}*.", parse_mode="Markdown")
							if(EUG == 1):
								bot.send_message(cid, "You have already introduced your Japanese Pirate ID in this group, if you want to edit it use `/edit Japan`", parse_mode="Markdown")
							con.commit()
						except sqlite3.Error as e:
							print(e)
							bot.send_message(cid, "You have already introduced your Japanese Pirate ID in this group, if you want to edit it use `/edit Japan`", parse_mode="Markdown")
				else:
					bot.send_message(cid, "ElseError: The format of the command is `/add Region XXXXXXXXX` where `Region` is `Japan` or `Global` and X are numbers.", parse_mode="Markdown")
							


			elif (m.text.Capitalize().startswith("Global"))
				print(str(idOP))
				print("Entro capitalizado. Voy a splitear.")
				idOP = idOP.split("Global", 1)[1]
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
							nocapital = uname.capitalize()
							EU = existeUser(uid)
							if(EU == 0):
								c.execute(f"INSERT INTO Usuarios (idUsuario,NombreUsuario,idGlobal) VALUES ('{uid}','@{nocapital}','{idOP}')")
							print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0")
							c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK,idGrupoFK,Region) VALUES ('{uid}','{cid}','Global')")
							bot.send_message(cid, f"*{uname}* has been added to the DB with Global Pirate ID *{idOP}*.", parse_mode="Markdown")
							con.commit()
						except sqlite3.Error as e:
							print(e)
							bot.send_message(cid, f"*{uname}* has been added to the DB with Global Pirate ID *{idOP}*.", parse_mode="Markdown")
					elif(EG == 1):
						print("El grupo sí existe")
						nocapital = uname.capitalize()
						try:
							EU = existeUser(uid)
							if(EU == 0):
								c.execute(f"INSERT INTO Usuarios (idUsuario,NombreUsuario,idGlobal) VALUES ('{uid}', '@{nocapital}','{idOP}')")
							print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0 Y AHORA VOY A COMPROBAR EUG")
							EUG = existeUserGru(uid,cid)
							print("Sabemos que EUG vale " + str(EUG))
							if(EUG == 0):
								print("Entro cuando no existe la combinación usuario - grupo")
								c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK,idGrupoFK,Region) VALUES ('{uid}','{cid}','Global')")
								bot.send_message(cid, f"*{uname}* has been added to the DB with Global Pirate ID *{idOP}*.", parse_mode="Markdown")
							if(EUG == 1):
								bot.send_message(cid, "You have already introduced your Global Pirate ID in this group, if you want to edit it use `/edit Global`", parse_mode="Markdown")
							con.commit()
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
	ulm = m.from_user.first_name
	if (m.from_user.username is None):
		uname = f"{ufm} {ulm}"
	else:
		uname = m.from_user.username
	if (m.text.capitalize().startswith("Japan")):
		try:
			idOP = m.text.split(' ', 1)[1].replace(" ","")
			pattern = '^\d\d\d\d\d\d\d\d\d$'
			idOP = idOP.split("Japan", 1)[1]
			if re.match(pattern, idOP, flags=0):
				try:
				  c.execute(f"UPDATE Usuarios SET 'idJapan' = '{idOP}','NombreUsuario'='@{uname}' WHERE idUsuario = {uid}")
				  bot.send_message(cid, f"*{uname}* now have with Japanese Pirate ID *{idOP}*.", parse_mode = "Markdown")
				  con.commit()
	
				except sqlite3.Error:
				  bot.send_message(cid, "ExceptError: The format of the command is `/add Region XXXXXXXXX` where `Region` is `Japan` or `Global` and X are numbers.", parse_mode="Markdown")
			else:
				
				bot.send_message(cid, "ElseError: The format of the command is `/add Region XXXXXXXXX` where `Region` is `Japan` or `Global` and X are numbers.", parse_mode="Markdown")
		  
		except:
			bot.send_message(cid, "ExceptError: The format of the command is `/add Region XXXXXXXXX` where `Region` is `Japan` or `Global` and X are numbers.", parse_mode="Markdown")


	if (m.text.capitalize().startswith("Global")):
		try:
			idOP = m.text.split(' ', 1)[1].replace(" ","")
			pattern = '^\d\d\d\d\d\d\d\d\d$'
			idOP = idOP.split("Japan", 1)[1]
			if re.match(pattern, idOP, flags=0):
				try:
				  c.execute(f"UPDATE Usuarios SET 'idGlobal' = '{idOP}','NombreUsuario'='@{uname}' WHERE idUsuario = {uid}")
				  bot.send_message(cid, f"*{uname}* now have with Global  Pirate ID *{idOP}*.", parse_mode = "Markdown")
				  con.commit()
	
				except sqlite3.Error:
				  bot.send_message(cid, "ExceptError: The format of the command is `/add Region XXXXXXXXX` where `Region` is `Japan` or `Global` and X are numbers.", parse_mode="Markdown")
			else:
				
				bot.send_message(cid, "ElseError: The format of the command is `/add Region XXXXXXXXX` where `Region` is `Japan` or `Global` and X are numbers.", parse_mode="Markdown")
		  
		except:
			bot.send_message(cid, "ExceptError: The format of the command is `/add Region XXXXXXXXX` where `Region` is `Japan` or `Global` and X are numbers.", parse_mode="Markdown")


@bot.message_handler(commands=['myid']) 
def command_miidOP(m):
	cid = m.chat.id
	uid = m.from_user.id
	ufm = m.from_user.first_name
	ulm = m.from_user.first_name
	if (m.from_user.username is None):
		uname = f"{ufm} {ulm}"
	else:
		uname = m.from_user.username

	if (m.text.capitalize().startswith("Japan")):
	try:
		c.execute(f"SELECT NombreUsuario,idJapan from Usuarios WHERE idUsuario={uid}")
		
		for i in c:
			NombreUsuario_resultado = f"{i[0]} "
			idOP_resultado = i[1]
			
		bot.send_message(cid, f'*{NombreUsuario_resultado}*: {idOP_resultado}', parse_mode = "Markdown")
		con.commit()
	except:
		bot.send_message(cid, "Your Japanese Pirate ID is not in the DB.", parse_mode = "Markdown")
		
		
	if (m.text.capitalize().startswith("Global")):
	try:
		c.execute(f"SELECT NombreUsuario,idGlobal from Usuarios WHERE idUsuario={uid}")
		
		for i in c:
			NombreUsuario_resultado = f"{i[0]} "
			idOP_resultado = i[1]
			
		bot.send_message(cid, f'*{NombreUsuario_resultado}*: {idOP_resultado}', parse_mode = "Markdown")
		con.commit()
	except:
		bot.send_message(cid, "Your Global Pirate ID is not in the DB.", parse_mode = "Markdown")


bot.skip_pending = True
bot.polling(none_stop=True)