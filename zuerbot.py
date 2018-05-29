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



@client.event
async def on_ready():
    print('BOT ONLINE - Testando')
    print(client.user.name)
    print(client.user.id)
    print('https://discord.gg/CmszJUV')

async def up_time():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    global seconds
    seconds = 0
    while not client.is_closed:
        await asyncio.sleep(1)
        seconds += 1
        if minutes == 60:
            minutes = 0
            hour += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
client.loop.create_task(up_time())



@client.event
async def on_message(message):

 #   if message.content.lower().startswith('zzueiro-logs'):
  #      server = message.server
   #     await client.create_channel(server, 'zueiro-logs', type=discord.ChannelType.text)

    if message.content.startswith('zpresence') and message.author.id == "320339126601777152":
        game = message.content[9:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Cóe criador, mudei meu status pra: " + game + "")

    if message.content.lower().startswith("z!eval"):
         if not message.author.id == '320339126601777152':
            return await client.send_message(message.channel, '**Permissão insuficiente**')
         try:
            embedeval1 = discord.Embed(title='\n', description='\n')
            embedeval1.add_field(name='**:inbox_tray: Entrada**', value='```' + message.content[7:] + '```')
            embedeval1.add_field(name='**:outbox_tray: Saída**', value='```' + str(eval(message.content[7:])) + '```')
            await client.send_message(message.channel, embed=embedeval1)

         except Exception as e:
            embedeval = discord.Embed(title='\n', description='\n')
            embedeval.add_field(name='**:inbox_tray: Entrada**', value='```' + message.content[7:] + '```')
            embedeval.add_field(name='**:outbox_tray: Saída**', value='```' + repr(e) + '```')
            await client.send_message(message.channel, embed=embedeval)

    if message.content.lower().startswith("zconvite"):
        invitelinknew = await client.create_invite(destination = message.channel, unique = True)
        embedMsginv=discord.Embed(color=message.author.color)
        embedMsginv.add_field(name="Convite para o servidor {}".format(message.server.name), value=invitelinknew)
        embedMsginv.set_footer(text="#Convide seus amigos")
        await client.send_message(message.channel, embed=embedMsginv)

    if message.content.lower().startswith('zban'):
        if not message.author.server_permissions.ban_members:
            user = message.mentions[0]
            author = message.author
            embkickx = discord.Embed(color=amarelo)
            embkickx.add_field(name="Alá `{}`, o `{}` tentou te banir sem ser ADM".format(user, author), value="<a:zueiroanonimobotemoji:440504316613230592>")
            embkickx.set_image(url='https://media.discordapp.net/attachments/440679680530710560/442450061004111874/unknown.png?width=459&height=248')
            embkickx.set_footer(text='Vacilão morre cedo')
            return await client.send_message(message.channel, embed=embkickx)
        try:
            author = message.author
            user = message.mentions[0]
            embkick2x = discord.Embed(color=author.color)
            embkick2x.add_field(name="<a:zueiroanonimobotemoji:440504316613230592> **EXPULSÃO**",
                              value="**Usuário banido:** {} \n"
                                    "**Comando realizado por:** {} \n"
                                    "".format(user, author)
                              )
            embkick2x.set_thumbnail(url=user.avatar_url)
            embkick2x.set_footer(text="ID = {}".format(user.id))
            await client.ban(member=user)
            return await client.send_message(message.channel,embed=embkick2x)
        except discord.errors.Forbidden:
            author = message.author
            embkick3x = discord.Embed(color=amarelo)
            embkick3x.add_field(name="Eu banir alguém de cargo mais alto que o meu ? kkk tu sonha demais {}".format(author), value="<a:zueiroanonimobotemoji:440504316613230592>")
            embkick3x.set_image(url='https://pbs.twimg.com/media/C4aWOX8XAAI9MX7.jpg')
            embkick3x.set_footer(text='PS: Assim tu me fode mano')
            return await client.send_message(message.channel, embed=embkick3x)
        except:
            return await client.send_message(message.channel, "Você deve especificar um usuário para banir, baby")

    if message.content.lower().startswith('zkick'):
        if not message.author.server_permissions.kick_members:
            user = message.mentions[0]
            author = message.author
            embkick = discord.Embed(color=amarelo)
            embkick.add_field(name="Alá `{}`, o `{}` tentou te kikar sem ser ADM".format(user, author), value="<a:zueiroanonimobotemoji:440504316613230592>")
            embkick.set_image(url='https://media.discordapp.net/attachments/440679680530710560/442450061004111874/unknown.png?width=459&height=248')
            embkick.set_footer(text='Vacilão morre cedo')
            return await client.send_message(message.channel, embed=embkick)
        try:
            author = message.author
            user = message.mentions[0]
            embkick2 = discord.Embed(color=author.color)
            embkick2.add_field(name="<a:zueiroanonimobotemoji:440504316613230592> **EXPULSÃO**",
                              value="**Usuário expulso:** {} \n"
                                    "**Comando realizado por:** {} \n"
                                    "".format(user, author)
                              )
            embkick2.set_thumbnail(url=user.avatar_url)
            embkick2.set_footer(text="ID = {}".format(user.id))
            await client.kick(member=user)
            return await client.send_message(message.channel,embed=embkick2)
        except discord.errors.Forbidden:
            author = message.author
            embkick3 = discord.Embed(color=amarelo)
            embkick3.add_field(name="Eu expulsar alguém de cargo mais alto que o meu ? kkk tu sonha demais {}".format(author), value="<a:zueiroanonimobotemoji:440504316613230592>")
            embkick3.set_image(url='https://pbs.twimg.com/media/C4aWOX8XAAI9MX7.jpg')
            embkick3.set_footer(text='PS: Assim tu me fode mano')
            return await client.send_message(message.channel, embed=embkick3)
        except:
            return await client.send_message(message.channel, "Você deve especificar um usuário para expulsar, baby")

    if message.content.lower().startswith('zsugestao'):
        try:
            inviteforsup = await client.create_invite(destination=message.channel, unique=True)
            canalsuges = discord.utils.get(client.get_all_channels(), id='437736462843248651')
            shaiderwow = discord.utils.get(client.get_all_members(), id='320339126601777152')
            sugestao1 = message.content[9:]
            user = message.author
            embsuges = discord.Embed(
                title='Nova sugestão de {}'.format(
                    user.name),
                color=user.color,
                descriptino=None
            )
            embsuges.set_thumbnail(url=user.avatar_url)
            embsuges.add_field(name='<:zueiroanonimosafadinho:438472983942660097>  Sugestão proposta:', value=sugestao1)
            embsuges.add_field(name="<a:zueiroanonimobotemoji:440504316613230592> Informações do usuário que enviou a sugestão <a:zueiroanonimobotemoji:440504316613230592>",
                            value="**Nome**: {} \n"
                            "**Apelido no seu server**: {} \n"
                            "**Seu ID**: {} \n"
                            "**Tag**: {} \n"
                            "**Enviada através do server**: {}".format(user.name, user.nick, user.id, user.discriminator, message.server.name)
                              )

            embsuges.set_footer(text="Este é um comando para sugestões sobre o BOT! nada mais")
            await client.send_message(shaiderwow, embed=embsuges)
            await client.send_message(shaiderwow, inviteforsup)
            await client.send_message(message.channel, 'Sua sugestão foi enviada para o servidor de suporte :3')
            await client.send_message(canalsuges, embed=embsuges)
        except:
            await client.send_message(message.channel, 'Desculpe, não entendi')

    if message.content.lower().startswith('zcsgo'):
        user = message.author
        try:
            csgo1 = message.content[6:]
            csgoname = requests.get(
                'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamids=' + csgo1 + '&format=json')
            csgo2 = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamid=' + csgo1 + '&l=br')
            csgoloads1 = json.loads(csgo2.text)
            csgoloads2 = json.loads(csgoname.text)
            namecsgo = csgoloads2['response']['players'][0]['personaname']
            killscsgo = csgoloads1['playerstats']['stats'][0]['value']#['total_kills']
            deathcsgo = csgoloads1['playerstats']['stats'][1]['value']#['total_deaths']
            plantacsgo = csgoloads1['playerstats']['stats'][3]['value']#['total_planted_bombs']
            defusecsgo = csgoloads1['playerstats']['stats'][4]['value']#['total_defused_bombs']
            tempocsgo = csgoloads1['playerstats']['stats'][2]['value']#['total_time_played']
            winscsgo = csgoloads1['playerstats']['stats'][5]['value']#['total_wins']
            moneycsgo = csgoloads1['playerstats']['stats'][7]['value']#['total_money_earned']
            thumbcsgo = 'https://orig00.deviantart.net/82ff/f/2015/340/b/b/counter_strike_global_offensive_png_icon_by_vezty-d87f3ww.png'


            embedcsgo = discord.Embed(color=user.color)
            embedcsgo.add_field(name='<:personcs:439190430924668939> Informações da conta <:personcs:439190430924668939>',
                                value="<:globalcsgo:439190468337598474> **Nick Atual:** {} <:globalcsgo:439190468337598474>\n"
                                      "<:miracsgo:439190488780898315> **Total de Kills:** {}           <:armacsgo:439190272413532160> **Total de mortes:** {} \n"
                                      "<:trcsgo:439190365980065792> **Bombas plantadas:** {}           <:ctcsgo:439190338364768256> **Bombas defusadas:** {} \n"
                                      "<:a_csgo:439190388830371852> **Total de vitórias:** {} \n"
                                      "<:b_csgo:439190449710956544> **Money ganho em partidas:** ${} \n"
                                      "<:x_csgo:439190408686469120> **Total de tempo jogado:** `Estamos com problemas nesta parte ainda` \n"
                                      "".format(namecsgo, killscsgo, deathcsgo, plantacsgo, defusecsgo, winscsgo, moneycsgo)
                                )
            embedcsgo.set_thumbnail(url=thumbcsgo)
            embedcsgo.set_footer(text="Seus Frags ultrapassam a barreira do -4")
            await client.send_message(message.channel, embed=embedcsgo)
        except:
            await client.send_message(message.channel, "# Só consigo procurar por ID's de conta Steam ;-; ")

    if message.content.lower().startswith('zsteam'):
        user = message.author
        try:
            testcmnd = '76561198168296588'
            steam1 = message.content[7:]
            steam4 = requests.get('http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamid=' + steam1 + '&format=json')
            steam2 = requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamids=' + steam1 + '&format=json')
            steam3 = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamid=' + steam1 + '&format=json')
            steamload1 = json.loads(steam2.text)
            steamload2 = json.loads(steam3.text)
            steamload3 = json.loads(steam4.text)
            nomeste = steamload1['response']['players'][0]['personaname']
            jogosste = steamload2['response']['game_count']
            temposte = steamload1['response']['players'][0]['timecreated']
            ulonlineste = steamload1['response']['players'][0]['lastlogoff']
        #    jogandoste = steamload1['response']['players'][0]['gameextrainfo'] não da de ativar o comando sem estar jogando
            idste = steamload1['response']['players'][0]['steamid']
            linkste = steamload1['response']['players'][0]['profileurl']
            avatarste = steamload1['response']['players'][0]['avatarfull']
            recent1ste = steamload3['response']['games'][0]['name']
        #    recent2ste = steamload3['response']['games'][1]['name']
         #   recent3ste = steamload3['response']['games'][2]['name']
          #  recent4ste = steamload3['response']['games'][3]['name']

            embedsteam = discord.Embed(color=user.color)
            embedsteam.add_field(
                name='<a:zueiroanonimobotemoji:440504316613230592> Aqui está a conta Steam que pediu, {}'.format(user.name),
                value="**Nick:** {} \n"
                      "**Total de jogos:** {} \n"
                      "**Conta criada em:** {} \n"
                      "**Ultimo login:** {} \n"
                      "**Ultimo jogo jogado:** {} \n"
                      "**Link do perfil:** \n {} \n"
                      "".format(nomeste, jogosste, time.strftime("%d/%m/%Y às %H:%M", time.localtime(temposte)), time.strftime("%d/%m/%Y às %H:%M", time.localtime(ulonlineste)), recent1ste, linkste)
            )
            embedsteam.set_thumbnail(url=avatarste)
            embedsteam.set_footer(text='#ZueiroAnonimoJogaNaSteam')
            await client.send_message(message.channel, embed=embedsteam)
        except:
            steam1priv = message.content[7:]
            steam2priv = requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamids=' + steam1 + '&format=json')
            steamload1priv = json.loads(steam2priv.text)
            nomestepriv = steamload1priv['response']['players'][0]['personaname']
        #    idstepriv = steamload1priv['response']['players'][0]['steamid']
            linkstepriv = steamload1priv['response']['players'][0]['profileurl']
            avatarstepriv = steamload1priv['response']['players'][0]['avatarfull']

            embedsteampriv = discord.Embed(color=user.color)
            embedsteampriv.add_field(
                name=' Aqui está a conta Steam que pediu, {}'.format(user.name),
                value="**Nick:** {} \n"
                      "**Link do perfil:** \n {} \n"
                      "`Este perfil possui áreas privadas, não consigo mostrar mais informações`"
                      "".format(nomestepriv, linkstepriv)
            )
            embedsteampriv.set_thumbnail(url=avatarstepriv)
            embedsteampriv.set_footer(text='#ZueiroAnonimoJogaNaSteam')
            await client.send_message(message.channel, embed=embedsteampriv)

    if message.content.lower().startswith('zfilme'):
        user = message.author
        try:
            movie1 = message.content[7:]
            movie2 = requests.get('https://api.themoviedb.org/3/search/movie?api_key=d9f2dc02f23bb44860dbb5fa196865d5&language=pt-br&query=' + movie1 + '/')
            movie = json.loads(movie2.text)
            nomemovie = (movie['results'][0]['title'])
            nomeorigmovie = (movie['results'][0]['original_title'])
            sinopsemovie = (movie['results'][0]['overview'])
            datamovie = (movie['results'][0]['release_date'])
            languagemovie = (movie['results'][0]['original_language'])
            imdbmovie = (movie['results'][0]['vote_average'])
            postermovie = (movie['results'][0]['poster_path'])



            embedfilm = discord.Embed(color=user.color)
            embedfilm.add_field(name='<a:zueiroanonimobotemoji:440504316613230592> Aqui está o filme 10 barra 10 que pediu, {}'.format(user.name),
                               value="🎬 **Filme:** {} \n"
                                     "** Nome Original:** {} 🎬\n"
                                     "📆 **Data de lançamento:** {} \n"
                                     "👅 **Linguagem original:** {} \n"
                                     "🔢 **Nota:** {} \n"
                                     "🌍 **Sinopse:** {} \n" 
                                     "".format(nomemovie, nomeorigmovie, datamovie, languagemovie, imdbmovie, sinopsemovie)
                               )
            embedfilm.set_thumbnail(url='https://image.tmdb.org/t/p/w600_and_h900_bestv2' + postermovie)
            embedfilm.set_footer(text="#ZueiroAninomoVirouCinéfolo")
            await client.send_message(message.channel, embed=embedfilm)
        except:
            await client.send_message(message.channel, "Putz grila Nilce, não consegui encontrar o filme!  :C")

    if message.content.lower().startswith('zserie'):
        user = message.author
        try:
            serie1 = message.content[7:]
            serie2 = requests.get('https://api.themoviedb.org/3/search/tv?api_key=d9f2dc02f23bb44860dbb5fa196865d5&language=pt-br&query=' + serie1 + '/')
            serie = json.loads(serie2.text)
            nomeserie = (serie['results'][0]['name'])
            nomeorigserie = (serie['results'][0]['original_name'])
            sinopseserie = (serie['results'][0]['overview'])
            dataserie = (serie['results'][0]['first_air_date'])
            languageserie = (serie['results'][0]['original_language'])
            imdbserie = (serie['results'][0]['vote_average'])
            posterserie = (serie['results'][0]['poster_path'])



            embedserie = discord.Embed(color=user.color)
            embedserie.add_field(name='<a:zueiroanonimobotemoji:440504316613230592> Aqui está a série 10 barra 10 que pediu, {}'.format(user.name),
                               value="🎬 **Série:** {} \n"
                                     "** Nome Original:** {} 🎬\n"
                                     "📆 **Data do 1° episódio:** {} \n"
                                     "👅 **Linguagem original:** {} \n"
                                     "🔢 **Nota:** {} \n"
                                     "🌍 **Sinopse:** {} \n" 
                                     "".format(nomeserie, nomeorigserie, dataserie, languageserie, imdbserie, sinopseserie)
                               )
            embedserie.set_thumbnail(url='https://image.tmdb.org/t/p/w600_and_h900_bestv2' + posterserie)
            embedserie.set_footer(text="#ZueiroAninomoMaratonaSéries")
            await client.send_message(message.channel, embed=embedserie)
        except:
            await client.send_message(message.channel, "Putz grila Nilce, não consegui encontrar a série!  :C")

    if message.content.lower().startswith('zzztoc4r'):
        #role = discord.utils.get(message.server.roles, name='DJ')
        #if not role in message.author.roles:
        #    return await client.send_message(message.channel, "💽``É necessário o cargo DJ para executar este comando!``")
        link = message.content[9:]
        voice = client.voice_client_in(message.server)
        player = await voice.create_ytdl_player("ytsearch:{}".format(link))
        player.start()
        await client.send_message(message.channel, "💽``Tocando agora: {}``".format(player.title))

    if message.content.startswith('ztist'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('zsleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

##############################BOT MUSIC##################################
    if message.content.startswith('zzzentr4r'):
      try:
        canal = message.author.voice.voice_channel
        await client.join_voice_channel(canal)
      except discord.errors.InvalidArgument:
             await client.send_message(message.channel, "Tu acha que eu vou advinhar em qual canal de voz entrar ? entra nele primeiro, depois me chama!")

    if message.content.startswith('zzzs4ir'):
      try:
        canaldevoz = client.voice_client_in(message.server)
        await canaldevoz.disconnect()
      except AttributeError:
          await client.send_message(message.channel,"Tu ta me vendo eu algum canal de voz ???? ENTÃO NÃO ME PEDE PRA SAIR!")
    #if message.content.startswith('zplay '):
     #   yt_url = message.content[6:]
      #  channel = message.author.voice.voice_channel
       # voice = await client.join_voice_channel(channel)
        #await voice.create_ytdl_player(yt_url)
    if message.content.startswith('zzzpl4y'):
            link = message.content[8:]
            canal = message.author.voice.voice_channel
            voice = await client.join_voice_channel(canal)
            player = await voice.create_ytdl_player(link)
            player.start()
            embedmusic = discord.Embed(
                title=":headphones: Tocando agora : {0}".format(player.title),
                colour=azul,
                descripition='\n'
            )
            embedmusic.set_thumbnail(url='https://i.pinimg.com/originals/a7/28/a7/a728a76e57ef17416040dd45a6548845.png%27')
            embedmusic.add_field(name='Duração', value='{} segundos'.format(player.duration))
            embedmusic.add_field(name="Música requisitada por", value='{}'.format(message.author.name))
            await client.send_message(message.channel, embed=embedmusic)

    ###################################INFO-LABNEGRO##################################
    if message.content.lower().startswith('zbotslabnegro'):
        user = message.author
        emblabneg1 = discord.Embed(
            title='{}, aqui estão algumas info de nossos BOTS em Python'.format(message.author.name),
            color=user.color,
            description='✅ = Informações completas\n❌ = Informações incompletas\n \n'
                        '✅**Nome do bot:** Deku#5579, '
                '**Id do bot:** 426889239318364170, '
                '**Dono do bot:** Diego#8505, '
                '**Id do dono:** 348920758623272960, '
                '**Link pra invite:** https://goo.gl/u28a1h, '
                '**LP:** Python, '
                '**Prefixo:** `-` \n'
                '✅**Nome do bot:** Earphone Jack#1589, '
                '**Id do bot:** 432140087019438080, '
                '**Dono do bot:** Diego#8505, '
                '**Id do dono:** 348920758623272960, '
                '**Link pra invite:** http://swifttopia.com/6870268/botepjack, '
                '**LP:** Python, '
                '**Prefixo:** `&` \n'
                '✅**Nome do bot:** Pythozinho#0053, '
                '**Id do bot:** 420703371918442499, '
                '**Dono do bot:** Vagner#1735, '
                '**Id do dono:** 232309115865661440, '
                '**Link pra invite:** https://goo.gl/q9hKzS , '
                '**LP:** Python, '
                '**Prefixo:** `?` \n'
                '✅**Nome do bot:** LoriS#9246, '
                '**Id do bot:** 426850189836419092, '
                '**Dono do bot:** Ph4#3931, '
                '**Id do dono:** 369962464613367811, '
                '**Link pra invite:** bit.ly/LoriSBOT, '
                '**LP:** Python, '
                '**Prefixo:** `L!` \n'
                '✅**Nome do bot:** Zueiro Anonimo#9641, '
                '**Id do bot:** 421862224454221824, '
                '**Dono do bot:** SHAIDERWOW#6701, '
                '**Id do dono:** 320339126601777152, '
                '**Link pra invite:** http://swifttopia.com/6870268/zueiroanonimo, '
                '**LP:** Python, '
                '**Prefixo:** `z` \n'
        )
        emblabneg2 = discord.Embed(
            title=None,
            color=user.color,
            description='✅**Nome do bot:** Beagle!#3110, '
                '**Id do bot:** 431517427147472936, '
                '**Dono do bot:** oCyberBR#5963 , '
                '**Id do dono:** 409318688895008768, '
                '**Link pra invite:** http://swifttopia.com/6870268/botbeagle, '
                '**LP:** Python, '
                '**Prefixo:** `b?` \n' 
                '✅**Nome do bot:** Joder#7480, '
                '**Id do bot:** 416669469050404865, '
                '**Dono do bot:** Kaigo#5682, '
                '**Id do dono:** 380441229416071170, '
                '**Link pra invite:** https://bit.ly/Joder, '
                '**LP:** Python, '
                '**Prefixo:** `jd_` \n' 
                '❌**Nome do bot:** Sesshomaru#9401, '
                '**Id do bot:** 425670256741187604, '
                '**Dono do bot:** Vagner#1735, '
                '**Id do dono:** 232309115865661440, '
                '**Link pra invite:** ?????, '
                '**LP:** Python, '
                '**Prefixo:** `s!` \n' 
                '✅**Nome do bot:** Hullo!!#2613, '
                '**Id do bot:** 431800868585865219, '
                '**Dono do bot:** Ph4#3931, '
                '**Id do dono:** 369962464613367811, '
                '**Link pra invite:** bit.ly/HulloBOT, '
                '**LP:** Python, '
                '**Prefixo:** `!!` \n' 
                '✅**Nome do bot:** Wanted#6346, '
                '**Id do bot:** 429376853162197002, '
                '**Dono do bot:** IamEduardo#6790, '
                '**Id do dono:** 319253966586118146, '
                '**Link pra invite:** http://swifttopia.com/6870268/botwanted, '
                '**LP:** Python, '
                '**Prefixo:** `w!` \n'
        )
        emblabneg3 = discord.Embed(
            title=None,
            color=user.color,
            description='✅**Nome do bot:** Zero#0561, '
                '**Id do bot:** 410173139084115968, '
                '**Dono do bot:** ◤LUCAS◥#5146, '
                '**Id do dono:** 302148993688010752, '
                '**Link pra invite:** https://goo.gl/9nECqp, '
                '**LP:** Python, '
                '**Prefixo:** `.` \n' 
                '✅**Nome do bot:** Shelect#7633, '
                '**Id do bot:** 414639245932756992, '
                '**Dono do bot:** yNerdSz.py 🔥#2937, '
                '**Id do dono:** 326513443693920266, '
                '**Link pra invite:** http://swifttopia.com/6870268/botshelect, '
                '**LP:** Python, '
                '**Prefixo:** `sh!` \n' 
                '❌**Nome do bot:** GeniusesBot#4849, '
                '**Id do bot:** 429022581614444553, '
                '**Dono do bot:** Dono#1090, '
                '**Id do dono:** ?????, '
                '**Link pra invite:** http://swifttopia.com/6870268/botgenuis, '
                '**LP:** Python, '
                '**Prefixo:** `?` \n' 
                '✅**Nome do bot:** Rafaela#2740, '
                '**Id do bot:** 428321055539462145, '
                '**Dono do bot:** yFunnyBr Lira#3629, '
                '**Id do dono:** 264101569333559297, '
                '**Link pra invite:** http://swifttopia.com/6870268/botrafaela, '
                '**LP:** Python, '
                '**Prefixo:** `.` \n'
        )
        emblabneg3.set_footer(text="Todas as informações foram pegas em: https://h4rt3ck.wixsite.com/apocryphos/forum/programacao/_bots")
        await client.send_message(message.channel, embed=emblabneg1)
        await client.send_message(message.channel, embed=emblabneg2)
        await client.send_message(message.channel, embed=emblabneg3)
    ##################################################################################
    ###################################BOTS DO LAB###########################################
    #LoriS
    if message.content.lower().startswith('<@426850189836419092>'):
        user = message.author
        embtestmarc = discord.Embed(
            title='<:python:419662789997756419> Reação da LoriS ao ver sua marcação, {}'.format(message.author.name),
            color=user.color,
            descriptino="VACILÃO MORRE CEDO",
        )
        embtestmarc.set_image(
            url='https://img00.deviantart.net/358f/i/2014/108/0/7/erza_scarlet_s_cake_problem_by_picklesandpigtails-d7f19lf.jpg')
        testmarc1 = await client.send_message(message.channel, embed=embtestmarc)
    #ZERO
    if message.content.lower().startswith('<@410173139084115968>'):
        user = message.author
        embtestmarc1 = discord.Embed(
            title='<:python:419662789997756419> Reação do Zero ao ver sua marcação, {}'.format(message.author.name),
            color=user.color,
            descriptino="VACILÃO MORRE CEDO",
        )
        embtestmarc1.set_image(
            url='https://media.discordapp.net/attachments/425866379921719297/428576974005338117/Izuku_Midoriya.png?width=589&height=431')
        testmarc11 = await client.send_message(message.channel, embed=embtestmarc1)

    if message.content.lower().startswith('<@426745809833295872>'):
        user = message.author
        embtestmarc2 = discord.Embed(
            title='<:python:419662789997756419> Reação da üc207Pr4f5t9 ao ver sua marcação, {}'.format(message.author.name),
            color=user.color,
            descriptino="VACILÃO MORRE CEDO",
        )
        embtestmarc2.set_image(
            url='https://i.pinimg.com/originals/d0/e0/1c/d0e01cae1613414eff5e5091ac09b934.jpg')
        testmarc1 = await client.send_message(message.channel, embed=embtestmarc2)
    ############################################################################################

    if message.content.lower().startswith('z.py'):
        usermsgcod = message.content[4:]
        try:
            await client.send_message(message.channel,'<:python:426890674256740384> {} enviou o segunte código:\n```python\n{} \n```'.format(message.author.mention, usermsgcod))
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Esqueceu de por o código, bb.')

    if message.content.lower().startswith('zhelp'):
        user = message.author
        embhelp2 = discord.Embed(title='<a:zueiroanonimobotemoji:440504316613230592> Olá, {}. <a:zueiroanonimobotemoji:440504316613230592>'.format(message.author.name), color=user.color,
                              description='No momento ainda não estou pronto,porém,posso lhe servir em algumas coisas.\n'
                                          'Vou deixar os meus comandos abaixo para ajudar.\n'
                                          '**zHelp : **Exibe esta mensagem.\n'
                                          '**zGif : **Envia um gif aleatório.\n'
                                          '**zVotar** `<mensagem>` **:** Faz uma votação por reactions.\n'
                                          '**zAvatar : **Mostra o avatar do usuário mencionado ou do seu.\n'
                                          '**zServerinfo : **Mostra as informações do servidor.\n'
                                          '**zBotinfo : **Mostra algumas informações sobre mim.\n'
                                          '**zUserinfo : **Mostra as informações do usuário mencionado ou as suas.\n'
                                          '**zGpsteam : **Mostra o meu grupo da Steam.\n'
                                          '**zSteam** `<ID da conta>`**:** Eu lhe mostro informações sobre a conta Steam. \n'
                                          '**zCsgo** `<ID da Steam>`**:** Eu lhe mostro as informações sobre a conta de CS:GO\n'
                                          '**zFlipcoin : **Me faz reagir com cara(😀) ou coroa(👑).\n'
                                          '**zFilme** `<nome do filme>`**:** Eu te mostro informações do filme escolhido.\n'
                                          '**zSerie** `<nome da serie>`**:** Eu te mostro informações da serie escolhida.\n'
                                          '**zGames : **Te dá o cargo do jogo caso você reaja com o emoji relativo ao mesmo.\n'
                                          '**zPing : **Exibe meu tempo de resposta.\n'
                                          '**zSugestao** `<mensagem>`**:** Envia sua sugestão diretamente pro meu dono.\n'
                                          '**zConvite:** Gera um link para convidar outros à este servidor. \n'
                                          '**z.Py** `<código>`**:** Coloca a fonte python do discord no seu código.\n'
                                          '<a:zueiroanonimobotemoji:440504316613230592>**Comandos que requerem permissões de administrador.**<a:zueiroanonimobotemoji:440504316613230592>\n'
                                          '**zAviso** `<menção>` `<mensagem>` **:** Envia uma mensagem ao usuário mencionado através de mim.\n'
                                          '**zBan** `<menção>` **:** Bane o usuário mencionado do servidor. \n'
                                          '**zKick** `<menção>` **:** Kika o usuário mencionado do servidor. \n'
                                          '<a:zueiroanonimobotemoji:440504316613230592>**ME ADICIONE AO SEU SERVIDOR**<a:zueiroanonimobotemoji:440504316613230592>\n'
                                          'Me adicione ao seu servidor usando este link:\n'
                                          '[Link direto](' + "https://goo.gl/kDKqhF" +')\n'
                                          'Servidor oficial (para suporte e afins):\n'
                                          '[Link direto](' + "http://discord.me/zueirosanonimous" + ')\n')
        await client.send_message(message.channel, embed=embhelp2)

    if message.content.lower().startswith('zzhelpantigasso'):
        user = message.author
        embhelp = discord.Embed(
            title='<:python:419660191244484609> Olá, {}'.format(message.author.name),
            color=user.color,
            descriptino='No momento ainda não estou pronto, porem posso lhe servir em algumas coisas...\nVou deixar algumas infos abaixo para lhe ajudar',
        )
        embhelp.add_field(name='<:python:419660191244484609> <:python:419660191244484609> <:python:419660191244484609> <:python:419660191244484609> <:python:419660191244484609> <:python:419660191244484609> <:python:419660191244484609> ' ,value='No momento ainda não estou pronto, porem posso lhe servir em algumas coisas...\nVou deixar algumas infos abaixo para lhe ajudar')
        embhelp.add_field(name='Meu servidor oficial',value='http://discord.me/zueirosanonimous')
        embhelp.add_field(name='Me adicione em seu servidor',value='http://swifttopia.com/6870268/zueiroanonimo')
        await client.send_message(message.channel, embed=embhelp)
        user = message.author
        embhelp1 = discord.Embed(
            title='<:python:419660191244484609> COMANDOS',
            color=user.color,
            descriptino=None,
        )
        embhelp1.add_field(name='zHelp', value='Aparece esta mensagem, com todos os comandos do BOT')
        embhelp1.add_field(name='zGif', value='Mostra um Gif aleatório engraçado aleatório')
        embhelp1.add_field(name='zVotar + (mensagem)', value='Faz uma votação de ✅ ou ❌ na sua mensagem')
        embhelp1.add_field(name='zAvatar + (usuário)', value='Mostra o avatar do usuário mencionado, junto com reações')
        embhelp1.add_field(name='zServerinfo', value='Mostra informações do servidor em que o BOT está')
        embhelp1.add_field(name='zBotinfo', value='Mostra minhas informações, ou seja, as informações do Zueiro Anonimo')
        embhelp1.add_field(name='zUserinfo + (usuário)', value='Mostra suas informações, caso mencione alguém, mostrará a do usuário mencionado')
        embhelp1.add_field(name='zSteam', value='Mostra meu grupo da Steam')
        embhelp1.add_field(name='zFlipcoin', value='Famoso "cara ou coroa", o BOT reagirá se for cara(😀) ou coroa(👑)')
        embhelp1.add_field(name='zGames', value='Aparece uma lista de jogos e se você clicar em um dos emotes você ganha o cargo dele, entretando só ganhará o cargo se o servidor tiver os seguintes cargos: `CS:GO, League of Legends, Gartic, VRCHAT, Brawlhalla, GTA V, PUBG, Roblox` (Obs. os cargos (roles) devem estar escritos igual ao que está acima)')
        embhelp1.add_field(name='zPing', value='Quantos segundos o BOT demora pra responder ? Teste de velocidade da internet do BOT')
        embhelp1.add_field(name='z.Py + (código)', value='Envia o código do formato Python formatado devolta')
        await client.send_message(message.channel, embed=embhelp1)
        embhelp2 = discord.Embed(
            title='<:python:419660191244484609> COMANDOS PARA ADMs',
            color=amarelo,
            descriptino=None,
        )
        embhelp2.add_field(name='zAviso (usuário) (mensagem)', value='Manda uma mensagem para o usuário mencionado através do BOT')
        await client.send_message(message.channel, embed=embhelp2)
        embhelp99 = discord.Embed(
            title='<:python:419660191244484609> BREVE MAIS...',
            color=azul,
            descriptino=None,
        )
        embhelp99.add_field(name='Só pra enfatizar...', value='Este bot ainda está em desenvolvimento')
        await client.send_message(message.channel, embed=embhelp99)

    if message.content.lower().startswith('<@421862224454221824>'):
        user = message.author
        embpapaco = discord.Embed(
            title='<a:zueiroanonimobotemoji:440504316613230592> Falou comigo, {}? <a:zueiroanonimobotemoji:440504316613230592>'.format(message.author.name),
            color=user.color,
            descriptino="VACILÃO MORRE CEDO",
        )
        embpapaco.set_image(
            url='https://images-ext-2.discordapp.net/external/UuIdfaTGI15OWrW9tZnlXD-rjkhVSzsuQXhUh7463Pg/https/i.imgur.com/T8auOavh.jpg?width=764&height=430')
        embpapaco.set_footer(text="Para ver meus comandos utilize zHelp")
        papaco = await client.send_message(message.channel, embed=embpapaco)
        #   🇧 🇺  🇳  🇩  🇦  ➖   🇲  🇴  🇱  🇪
        await client.add_reaction(papaco, '🇧')
        await client.add_reaction(papaco, '🇺')
        await client.add_reaction(papaco, '🇳')
        await client.add_reaction(papaco, '🇩')
        await client.add_reaction(papaco, '🇦')
        await client.add_reaction(papaco, '➖')
        await client.add_reaction(papaco, '🇲')
        await client.add_reaction(papaco, '🇴')
        await client.add_reaction(papaco, '🇱')
        await client.add_reaction(papaco, '🇪')
        await client.wait_for_message(author=message.author, content="Não gracinha")
        await client.send_message(message.channel, 'Ainda bem... até um outro dia')

    if message.content.lower().startswith('zaviso'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel,'Somente para ADMs do server, desculpa bb <a:zueiroanonimobotemoji:440504316613230592>')
        try:
            author = message.author
            user = message.mentions[0]
            msgg = message.content[6:]
            await client.send_message(user, "**{} lhe mandou um aviso com a seguinte mensagem:** \n {}".format(author, msgg))
        except:
            await client.send_message(message.channel, 'Escreva algo para eu enviar no privado deste usuário.')

    if message.content.lower().startswith('zping'):
        timep = time.time()
        emb = discord.Embed(title='Aguarde...', color=0x565656)
        pingm0 = await client.send_message(message.channel, embed=emb)
        ping = time.time() - timep
        pingm1 = discord.Embed(title='Pong!', description='<a:zueiroanonimobotemoji:440504316613230592> Ping - %.01f segundos' % ping, color=0x15ff00)
        await client.edit_message(pingm0, embed=pingm1)

    if message.content.lower().startswith('zdiga'):
        if message.author.id == '320339126601777152':
            await client.send_message(message.channel, message.content[5:])
            await client.delete_message(message)

    if message.content.lower().startswith('zbotinfo'):
        embedbotin = discord.Embed(
            title=" <:python:419660191244484609> Olá, sou o Zueiro Anonimo <:python:419660191244484609> ",
            descriptino="Oinn",
        )
        embedbotin.set_thumbnail(url=client.user.avatar_url)
        embedbotin.add_field(name='<a:zueiroanonimobotemoji:440504316613230592> Discord BOT Básico', value='Um botizinho com o programa HUEBR injetado na veia')
        embedbotin.add_field(name='<a:nyancat:450290566802964480> Meu site:', value='https://goo.gl/8Ti3eh')
        embedbotin.add_field(name='<a:nyancat:450290566802964480> Estou online faz:', value='`{} hrs {} min e {} segs`'.format(hour, minutes, seconds))
        embedbotin.add_field(name='<a:nyancat:450290566802964480> Ultima atualização:', value='`29/05/2018`')
        embedbotin.add_field(name='<a:nyancat:450290566802964480> Criado em:', value='`24/03/2018`')
        embedbotin.add_field(name='<a:nyancat:450290566802964480> Estou online em',
                             value='` ' + (str(len(client.servers))) + ' `  Serve(s) <:python:419660191244484609> ')
        embedbotin.add_field(name='<a:nyancat:450290566802964480> Em contato com', value='`' + str(len(set(client.get_all_members()))) + ' usuarios`')
        embedbotin.set_footer(text="Criado por SHAIDERWOW#6701 - Copyright © 2018 - Quer saber mais ? digite zHelp", icon_url="https://images-ext-1.discordapp.net/external/OMP4WooSTGR7TMyMtuRSyDPApIIB3f2POTZV6PPLBgM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/320339126601777152/6044af07c657f2d82a2b5bcfbed01d3d.webp")
        await client.send_message(message.channel, embed=embedbotin)

    if message.content.lower().startswith('zuserinfo'):
        try:
            member = message.mentions[0]
            statusgamememb = str(member.game)
            statusnickmemb = str(member.nick)
            statusonmemb = str(member.status)
            tempoxx1x = member.joined_at
            rolesmemb = ([role.name for role in member.roles if role.name != "@everyone"])
            embedusu = discord.Embed(
                title='<a:zueiroanonimobotemoji:440504316613230592> Informações de: {} <a:zueiroanonimobotemoji:440504316613230592>'.format(
                    member.name),
                color=member.color,
                descriptino=None,
            )
            embedusu.set_thumbnail(url=member.avatar_url)
            embedusu.add_field(name="<a:nyancat:450290566802964480> Seu nome", value="{}`#{}`".format(member.name, member.discriminator))
            embedusu.add_field(name='<a:nyancat:450290566802964480> Seu apelido aqui:', value=statusnickmemb.replace('None', 'Não tem'))
            embedusu.add_field(name="<a:nyancat:450290566802964480> Seu ID", value="`{}`".format(member.id))
            embedusu.add_field(name="<a:nyancat:450290566802964480> Status", value=statusonmemb.replace("online","<:online:438399398808911882>").replace("offline","<:offline:438399398762905600>").replace("dnd","<:dnd:438399396548313091>").replace("idle","<:idle:438399398796460032>").replace("stream","<:stream:438399396963418131>"))
            embedusu.add_field(name='<a:nyancat:450290566802964480> Jogando:', value=statusgamememb.replace('None', 'Nada ;-;'))
            embedusu.add_field(name="<a:nyancat:450290566802964480> Criado em:", value=member.created_at.strftime("%d/%m/%Y às %H:%M"))
            embedusu.add_field(name="<a:nyancat:450290566802964480> Maior Cargo: ", value="`{}`".format(member.top_role))
            embedusu.add_field(name='<a:nyancat:450290566802964480> Cargos:', value="```{}```".format(rolesmemb))
            await client.send_message(message.channel, embed=embedusu)
        except:
            user = message.author
            statusgameuse = str(message.author.game)
            statusnickuse = str(message.author.nick)
            statusonuse = str(message.author.status)
            rolesuse = ([role.name for role in user.roles if role.name != "@everyone"])
            tempoxx2x = user.joined_at
            embedusu1 = discord.Embed(
                title='<a:zueiroanonimobotemoji:440504316613230592> Informações de: {} <a:zueiroanonimobotemoji:440504316613230592>'.format(
                    user.name),
                color=user.color,
                descriptino=None,
            )
            embedusu1.set_thumbnail(url=user.avatar_url)
            embedusu1.add_field(name="<a:nyancat:450290566802964480> Seu Nome", value="{}`#{}`".format(user.name, user.discriminator))
            embedusu1.add_field(name='<a:nyancat:450290566802964480> Seu apelido aqui:', value=statusnickuse.replace('None', 'Não tem'))
            embedusu1.add_field(name="<a:nyancat:450290566802964480> Seu ID", value="`{}`".format(user.id))
            embedusu1.add_field(name="<a:nyancat:450290566802964480> Status", value=statusonuse.replace("online","<:online:438399398808911882>").replace("offline","<:offline:438399398762905600>").replace("dnd","<:dnd:438399396548313091>").replace("idle","<:idle:438399398796460032>").replace("stream","<:stream:438399396963418131>"))
            embedusu1.add_field(name='<a:nyancat:450290566802964480> Jogando:', value=statusgameuse.replace('None', 'Nada ;-;'))
            embedusu1.add_field(name="<a:nyancat:450290566802964480> Criado em:", value=user.created_at.strftime("%d/%m/%Y às %H:%M"))
            embedusu1.add_field(name="<a:nyancat:450290566802964480> Maior Cargo:", value="`{}`".format(user.top_role))
            embedusu1.add_field(name='<a:nyancat:450290566802964480> Cargos:', value="```{}```".format(rolesuse))

            await client.send_message(message.channel, embed=embedusu1)

    elif message.content.lower().startswith('zavatar'):
        try:
            member = message.mentions[0]
            embed = discord.Embed(
                title='<a:zueiroanonimobotemoji:440504316613230592> Avatar de: {} <a:zueiroanonimobotemoji:440504316613230592>'.format(member.name),
                color=member.color,
                description='Reaja ao avatar de {}! <a:zueiroanonimobotemoji:440504316613230592>'.format(
                    member.name))
            embed.set_image(url=member.avatar_url)
            avatar = await client.send_message(message.channel, embed=embed)
            await client.add_reaction(avatar, '👍')
            await client.add_reaction(avatar, '❤')
            await client.add_reaction(avatar, '😂')
            await client.add_reaction(avatar, '😱')
            await client.add_reaction(avatar, '💩')

        except:
            user = message.author
            embedavata = discord.Embed(
                title='<a:zueiroanonimobotemoji:440504316613230592> Avatar de: {} <a:zueiroanonimobotemoji:440504316613230592>'.format(user.name),
                color=user.color,
                description='Reaja ao avatar de {}! <a:zueiroanonimobotemoji:440504316613230592>'.format(
                    user.name))
            embedavata.set_image(url=user.avatar_url)
            avatar2 = await client.send_message(message.channel, embed=embedavata)
            await client.add_reaction(avatar2, '👍')
            await client.add_reaction(avatar2, '❤')
            await client.add_reaction(avatar2, '😂')
            await client.add_reaction(avatar2, '😱')
            await client.add_reaction(avatar2, '💩')

    if message.content.lower().startswith('zserverinfo'):
        server = message.server
        online = len([m.status for m in message.server.members
                      if m.status == discord.Status.online])
        offline = len([m.status for m in message.server.members
                      if m.status == discord.Status.offline])
        dnd = len([m.status for m in message.server.members
                      if m.status == discord.Status.dnd])
        idle = len([m.status for m in message.server.members
                      if m.status == discord.Status.idle])
        cargosserv = [role.name for role in message.server.roles if role.name != "@everyone"]

        embed3 = discord.Embed(
            title="Informações do server <a:zueiroanonimobotemoji:440504316613230592> ",
            descriptino=None,
        )
        embed3.add_field(name="<a:nyancat:450290566802964480> Nome do server", value=message.server.name, inline=True)
        embed3.add_field(name="<a:nyancat:450290566802964480> Criado em", value=message.server.created_at.strftime("%d/%m/%Y às %H:%M"))
        embed3.add_field(name="<a:nyancat:450290566802964480> Server ID", value=message.server.id, inline=True)
        embed3.add_field(name="<a:nyancat:450290566802964480> Dono", value=message.server.owner.mention)
        embed3.add_field(name="<a:nyancat:450290566802964480> Região do Server", value=str(message.server.region).title())
        embed3.add_field(name="<a:nyancat:450290566802964480> Emojis", value=f"{len(message.server.emojis)}/100")
        embed3.add_field(name="<a:nyancat:450290566802964480> Membros ({}):".format(len(message.server.members)), value=f"**{online}<:online:438399398808911882> {offline}<:offline:438399398762905600> \n{dnd}<:dnd:438399396548313091> {idle}<:idle:438399398796460032>**")
        embed3.add_field(name="<a:nyancat:450290566802964480> Cargos ({}):".format(len(message.server.roles)), value="```{}```".format(cargosserv))
        embed3.set_thumbnail(url=message.server.icon_url)
        embed3.set_footer(text="Criado por SHAIDERWOW#6701 - Copyright © 2018 - Quer saber mais ? digite zHelp", icon_url="https://images-ext-1.discordapp.net/external/OMP4WooSTGR7TMyMtuRSyDPApIIB3f2POTZV6PPLBgM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/320339126601777152/6044af07c657f2d82a2b5bcfbed01d3d.webp")
        await client.send_message(message.channel, embed=embed3)

    if message.content.lower().startswith('zgpsteam'):
        await client.send_message(message.channel, "**Entra lá bb** \nhttps://goo.gl/R2mC2g")

    if message.content.lower().startswith('zgif'):
        embgif = discord.Embed(
            title='O gif escolhido aleatóriamente foi....',
            color=azul,
            descriptino=None,
        )
        choice = random.randint(1,17)
        if choice == 1:
            linkdogif = "https://i.pinimg.com/originals/03/38/ed/0338ed402affbb1f80961f09a7153d35.gif"
        if choice == 2:
            linkdogif = "https://www.tenor.co/O1zu.gif"
        if choice == 3:
            linkdogif = "https://media.giphy.com/media/Ewd3jzmdc9XKo/giphy.gif"
        if choice == 4:
            linkdogif = "https://i.pinimg.com/originals/82/32/0d/82320d4e1f8d1b1f4a7878817cc02bb9.gif"
        if choice == 5:
            linkdogif = 'http://1.bp.blogspot.com/--a2oXKQftfs/Ua5gSz1aSXI/AAAAAAAAEAk/kKlQQB8liyg/s1600/huehuehue-brbrbr-oque-e-significado-brchan-b-como-usar-humortalouco.gif'
        if choice == 6:
            linkdogif = "https://img.buzzfeed.com/buzzfeed-static/static/2017-04/21/12/asset/buzzfeed-prod-fastlane-03/anigif_sub-buzz-8560-1492791743-1.gif"
        if choice == 7:
            linkdogif = "https://im-01.gifer.com/BkSi.gif"
        if choice == 8:
            linkdogif = "http://muitobacana.com/wp-content/uploads/2017/09/gif-engra%C3%A7ado-que-se-mexe-para-whatsapp-7.gif"
        if choice == 9:
            linkdogif = "https://thumbs.gfycat.com/DefensiveFrayedGentoopenguin-size_restricted.gif"
        if choice == 10:
            linkdogif = "http://www.whatstube.com.br/wp-content/uploads/2016/08/quando-o-desespero-bate.gif"
        if choice == 11:
            linkdogif = "https://www.tenor.co/RhQf.gif"
        if choice == 12:
            linkdogif = "https://media.giphy.com/media/d3mlE7uhX8KFgEmY/source.gif"
        if choice == 13:
            linkdogif = "https://cdn.discordapp.com/attachments/425048501504704543/427455890300469248/20161023-001_1.gif"
        if choice == 14:
            linkdogif = "https://cdn.discordapp.com/attachments/425048501504704543/427227841315340298/Gifs_animados_1_thumb.gif"
        if choice == 15:
            linkdogif = "https://cdn.discordapp.com/attachments/425048501504704543/427226506423566336/pikachu_troll.gif"
        if choice == 16:
            linkdogif = "https://media.tenor.com/images/6afb17492c5b0a711b51afe70e24d3c4/tenor.gif"
        if choice == 17:
            linkdogif = "https://media.giphy.com/media/fc5sXBODbh1UA/giphy.gif"

        embgif.set_image(url=linkdogif)
        await client.send_message(message.channel, embed=embgif)

    if message.content.lower().startswith('zflipcoin'):
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '😀')
        if choice == 2:
            await client.add_reaction(message, '👑')

    if message.content.lower().startswith('zvotar'):
        try:
            user = message.author
            phrase = message.content[6:]
            embed4 = discord.Embed(title="VOTAÇÃO", description=" \n ", color=user.color)
            embed4.add_field(name="{} Opinou...".format(message.author.name), value="{}".format(phrase),
                           inline=False)
            embed4.set_thumbnail(url=message.author.avatar_url)
            votacao = await client.send_message(message.channel, embed=embed4)
            await client.delete_message(message)
            await client.add_reaction(votacao, '✅')
            await client.add_reaction(votacao, '❌')

        except:
            user = message.author
            phrase = message.content[6:]
            embed4 = discord.Embed(title="ERROR", description=" \n ", color=0xff0000)
            embed4.add_field(name="Falha ao executar.".format(message.author.name),
                    value="Comando incompleto, digite algo após `zVotar` para criar uma votação", inline=False)
            await client.send_message(message.channel, embed=embed4)

    if message.content.lower().startswith("zgames"):
        server = message.server
        embed1 = discord.Embed(
            title="Escolha seus jogos!",
            color=roxo
        )
        embed1.add_field(name="<a:zueiroanonimobotemoji:440504316613230592>",
                         value="**CS:GO =** <:person_csgo:439190430924668939>\n"
                        "**Gartic  =**  <:gartic:442757221411979284> \n"
                        "**GTA V  =** <:gtav:442822601295790080>\n"
                        "**PUBG =** <:pubg:442758461810409482>\n"
                        "**Brawlhalla =** <:brawlhalla:442757169675370497>\n"
                        "**VRCHAT =** <:vrchat:442758209585807361>\n"
                        "**League of Legends =** <:lol:442758156850823168>\n"
                        "**Roblox =** <:roblox:442757513939648522>\n"
                        ""
                         )
        embed1.add_field(name="<a:zueiroanonimobotemoji:440504316613230592>",
                         value="**Minecraft =** <:minecraft:442757343646580757>\n"
                        "**Rainbow Six  =**  <:r6:442757819926577152> \n"
                        "**Overwatch  =** <:overwatch:442758257799462913>\n"
                        "**Paladins =** <:paladins:442823168810549249>\n"
                        "**Warframe =** <:warframe:442758505816915980>\n"
                        "**Black Squad =** <:blacksquad:442822965718024201>\n"
                        "**Rocket League =** <:rocketleague:442822713195757569>\n"
                        "**Fortnite =** <:fortnite:442823029278638080>\n"
                        ""
                         )
        embed1.set_footer(text="Breve mais... Digite zHelp para saber mais sobre mim")
        botmsg = await client.send_message(message.channel, embed=embed1)

        await client.add_reaction(botmsg, "person_csgo:439190430924668939")
        await client.add_reaction(botmsg, "gartic:442757221411979284")
        await client.add_reaction(botmsg, "gtav:442822601295790080")
        await client.add_reaction(botmsg, "pubg:442758461810409482")
        await client.add_reaction(botmsg, "brawlhalla:442757169675370497")
        await client.add_reaction(botmsg, "vrchat:442758209585807361")
        await client.add_reaction(botmsg, "lol:442758156850823168")
        await client.add_reaction(botmsg, "roblox:442757513939648522")
        await client.add_reaction(botmsg, "minecraft:442757343646580757")
        await client.add_reaction(botmsg, "r6:442757819926577152")
        await client.add_reaction(botmsg, "overwatch:442758257799462913")
        await client.add_reaction(botmsg, "paladins:442823168810549249")
        await client.add_reaction(botmsg, "warframe:442758505816915980")
        await client.add_reaction(botmsg, "blacksquad:442822965718024201")
        await client.add_reaction(botmsg, "rocketleague:442822713195757569")
        await client.add_reaction(botmsg, "fortnite:442823029278638080")


        global msg_id
        msg_id = botmsg.id

        global msg_user
        msg_user = message.author.bot

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji.id == "439190430924668939" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "CS:GO", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="CS:GO")
            print("create")

    if reaction.emoji.id == "442757221411979284" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Gartic", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Gartic")
            print("create")

    if reaction.emoji.id == "442822601295790080" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "GTA V", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="GTA V")
            print("create")

    if reaction.emoji.id == "442758461810409482" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "PUBG", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="PUBG")
            print("create")

    if reaction.emoji.id == "442757169675370497" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Brawlhalla", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Brawlhalla")
            print("create")

    if reaction.emoji.id == "442758209585807361" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "VRCHAT", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="VRCHAT")
            print("create")

    if reaction.emoji.id == "442758156850823168" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "League of Legends", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="League of Legends")
            print("create")

    if reaction.emoji.id == "442757513939648522" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Roblox", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Roblox")
            print("create")

    if reaction.emoji.id == "442757343646580757" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Minecraft", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Minecraft")
            print("create")

    if reaction.emoji.id == "442757819926577152" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Rainbow Six", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Rainbow Six")
            print("create")

    if reaction.emoji.id == "442758257799462913" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Overwatch", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Overwatch")
            print("create")

    if reaction.emoji.id == "442823168810549249" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Paladins", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Paladins")
            print("create")

    if reaction.emoji.id == "442758505816915980" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Warframe", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Warframe")
            print("create")

    if reaction.emoji.id == "442822965718024201" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Black Squad", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Black Squad")
            print("create")

    if reaction.emoji.id == "442822713195757569" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Rocket League", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Rocket League")
            print("create")

    if reaction.emoji.id == "442823029278638080" and msg.id == msg_id and not user == msg_user:
        try:
            role = discord.utils.find(lambda r: r.name == "Fortnite", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
        except:
            await client.create_role(msg_user.server, name="Fortnite")
            print("create")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji.id == "439190430924668939" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "CS:GO", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442757221411979284" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Gartic", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442822601295790080" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "GTA V", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442758461810409482" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "PUBG", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442757169675370497" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Brawlhalla", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442758209585807361" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "VRCHAT", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442758156850823168" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "League of Legends", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442757513939648522" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Roblox", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442757343646580757" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Minecraft", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442757819926577152" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Rainbow Six", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442758257799462913" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Overwatch", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442823168810549249" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Paladins", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442758505816915980" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Warframe", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442822965718024201" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Black Squad", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442822713195757569" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Rocket League", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji.id == "442823029278638080" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Fortnite", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")


@client.event
async def on_member_join(member):
    canal = client.get_channel("417466650451771394")
    regras = client.get_channel("420007865894567946")
    msg = "Bem Vindo ao {}, {}\n Quem sou eu ? eu sou um BOT muito gente boa S2\n Para ver meus comandos digite `zHelp` no servidor \n para me adicionar ao seu servidor acesse: https://goo.gl/kDKqhF".format(member.server.name, member.mention)
    await client.send_message(member, msg)  # substitua canal por member para enviar a msg no DM do membro


@client.event
async def on_member_remove(member):
    canal = client.get_channel("417466650451771394")
    msg = "Adeus garotinho juvenil {}, este server será sua falta".format(member.mention)
    await client.send_message(member, msg)  # substitua canal por member para enviar a msg no DM do membro


client.run(token)
