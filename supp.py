import discord
from discord.ext import commands
import random
import asyncio
import random
import os
import io
import re
import time
import youtube_dl
import discord.ext.commands
import requests
import json
import datetime
import supp.py

players = {}
config = None
client = discord.Client()

DEIN_USERNAME = "DEINE_USER_ID"

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto

    token = secreto.seu_token()

verde = 0x00FF00
azul = 0x0000FF
vermelho = 0xFF0000
amarelo = 0xFFFF00
roxo = 0x690FC3
msg_id = None
msg_user = None

global msg_reg
msg_reg = discord.utils.get(client.get_all_channels(), id='461613280251871232')

@client.event
async def on_ready():
    print('Modo servidor de suporte ONLINE')

@client.event
async def on_message(message):


    if message.content.startswith("zTermos&Condições"):
        if not message.channel.id == "461613280251871232":
            return
        else:
            user = message.author
            role = discord.utils.find(lambda r: r.name == 'Membros', message.server.roles)
            await client.add_roles(user, role)
            embedreg = discord.Embed(title="Você agora está no servidor Zueiros Anonimous ❤",
                                  description="Vê se não deixa o servidor morrer hein, você agora é uma parte importante dele, sinta-se orgulhoso(a) !",
                                  color=user.color)
            embedreg.set_author(name="Olá...")
            embedreg.set_footer(text='Para saber meus comandos digite "zHelp" em um canal ESPECÍFICO !')
            await client.send_message(user, embed=embedreg)

    if message.channel.id == "461613280251871232":
        await asyncio.sleep(1)
        await client.delete_message(message)

    if message.content.lower().startswith("z?registro"):
        if not message.author.id == '320339126601777152':
            return
        else:
            embedreg = discord.Embed(title="Bem vindo ao Zueiros Anonimous", url="https://goo.gl/8Ti3eh",
                                  description="Antes de mais nada gostaria que você lesse tudinho ❤")
            embedreg.set_author(name="Mensagem de registramento",
                             url="http://discord.gg/9yw4AQe", icon_url = "https://images-ext-2.discordapp.net/external/A32qoE2z-1WSyFxjByYYSaLevOFpPxoilGvmQToPpvA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/421862224454221824/470446de83376ed6744ab43b2a7bc33d.webp?width=428&height=428")
            embedreg.add_field(name="Como se registrar...",
                            value="Enfim meu consagrado, vou ser direto, esta é uma espécie de registração em nosso servidor, mas é claro, sem poluir nosso servidor com diversas coisas diferentes e que não fazem muito sentido... \nPulando toda a conversa fiada gostaria que utilizasse o respectivo comando caso queira ficar para 'zoar' no servidor.",
                            inline=False)
            embedreg.add_field(name="Obrigado pela compreensão",
                            value="Comando para registro = `zTermos&Condições`", inline=False)
            embedreg.add_field(name="Aviso rápido",
                            value="Ao entrar neste servidor você estará ciente de que deverá ler as regras, caso não as respeite uma punição será utilizada.\n\nProve que leu até o final e reaja a esta mensagem ❤",
                            inline=False)
            embedreg.add_field(name="Meu site:", value="https://goo.gl/8Ti3eh", inline=True)
            embedreg.add_field(name="Meu criador:", value="<@320339126601777152>", inline=True)
            embedreg.add_field(name="Meu prefix:", value="`z`", inline=True)
            embedreg.set_footer(text="Registração não funciona ? fale com meu criador = SHAIDERWOW#6701")
            regmesg = await client.send_message(message.channel, embed=embedreg)
            await client.add_reaction(regmesg, "a:zueiroanonimobotemoji:440504316613230592")


#client.run(token)
