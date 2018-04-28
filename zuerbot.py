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
    await client.change_presence(game=discord.Game(name='zHelp //// discord.me/zueirosanonimous'))




@client.event
async def on_message(message):




    if message.content.lower().startswith('zsugestao'):
        try:
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
            embsuges.add_field(name="<:10barra10:438472637765779456> Informações do usuário que enviou a sugestão <:10barra10:438472637765779456>",
                            value="**Nome**: {} \n"
                            "**Apelido no seu server**: {} \n"
                            "**Seu ID**: {} \n"
                            "**Tag**: {} \n"
                            "**Enviada através do server**: {}".format(user.name, user.nick, user.id, user.discriminator, message.server.name)
                              )

            embsuges.set_footer(text="Este é um comando para sugestões sobre o BOT! nada mais")
            await client.send_message(shaiderwow, embed=embsuges)
            await client.send_message(message.channel, 'Sua sugestão foi enviada para o servidor de suporte :3')
            await client.send_message(canalsuges, embed=embsuges)
        except:
            await client.send_message(message.channel, 'Desculpe, não entendi')



    if message.content.lower().startswith('zcsgo'):
        user = message.author
        try:
            csgo1 = message.content[6:]
        #    csgoname = requests.get(
        #        'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamids=' + csgo1 + '&format=json')
            csgo2 = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamid=' + csgo1 + '&l=br')
            csgoloads1 = json.loads(csgo2.text)
        #    csgoloads2 = json.loads(csgoname.text)
        #    namecsgo = csgoloads2['response']['players'][0]['personaname']
            killscsgo = csgoloads1['playerstats']['stats'][0]['total_kills']
            deathcsgo = csgoloads1['playerstats']['stats'][0]['total_deaths']
            plantacsgo = csgoloads1['playerstats']['stats'][0]['total_planted_bombs']
            defusecsgo = csgoloads1['playerstats']['stats'][0]['total_defused_bombs']
        #    tempocsgo = csgoloads1['playerstats']['stats'][0]['total_time_played']
            winscsgo = csgoloads1['playerstats']['stats'][0]['total_wins']
            moneycsgo = csgoloads1['playerstats']['stats'][0]['total_money_earned']
            thumbcsgo = 'https://orig00.deviantart.net/82ff/f/2015/340/b/b/counter_strike_global_offensive_png_icon_by_vezty-d87f3ww.png'

            embedcsgo = discord.Embed(color=user.color)
            embedcsgo.add_field(name='<:personcs:439190430924668939> Informações da conta <:personcs:439190430924668939>',
                                value="<:globalcsgo:439190468337598474> **Nick Atual:** xx <:globalcsgo:439190468337598474>\n"
                                      "<:miracsgo:439190488780898315> **Total de Kills:** {}           <:armacsgo:439190272413532160> **Total de mortes:** {} \n"
                                      "<:trcsgo:439190365980065792> **Bombas plantadas:** {}           <:ctcsgo:439190338364768256> **Total de bombas defusadas:** {} \n"
                                      "<:a_csgo:439190388830371852> **Total de vitórias:** {}            <:b_csgo:439190449710956544> **Total de Money em partidas:** {} \n"
                                      "<:x_csgo:439190408686469120> **Total de tempo jogado:** xx \n"
                                      "".format(killscsgo, deathcsgo, plantacsgo, defusecsgo, winscsgo, moneycsgo, ))
            embedcsgo.set_thumbnail(url=thumbcsgo)
            embedcsgo.set_footer(text="Vem X1 noob, tenho Asiimov")
            await client.send_message(message.channel, embed=embedcsgo)
        except discord.errors.HTTPException:
            await client.send_message(message.channel, "Só consigo procurar por ID's de conta Steam ;-; ")






    if message.content.lower().startswith('zsteam'):
        user = message.author
        try:
            testcmnd = '76561198168296588'
            steam1 = message.content[7:]
            steam2 = requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamids=' + steam1 + '&format=json')
            steam3 = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=C17D1FB55BAAFBA0288B05AF103BC7B4&steamid=' + steam1 + '&format=json')
            steamload1 = json.loads(steam2.text)
            steamload2 = json.loads(steam3.text)
            nomeste = steamload1['response']['players'][0]['personaname']
            jogosste = steamload2['response']['game_count']
            temposte = steamload1['response']['players'][0]['timecreated']
        #    ulonlineste = steamload1['response']['players'][0]['lastlogoff'] tempo estranho
        #    jogandoste = steamload1['response']['players'][0]['gameextrainfo'] não da de ativar o comando sem estar jogando
            idste = steamload1['response']['players'][0]['steamid']
            linkste = steamload1['response']['players'][0]['profileurl']
            avatarste = steamload1['response']['players'][0]['avatarfull']

            embedsteam = discord.Embed(color=user.color)
            embedsteam.add_field(
                name='<:10barra10:438472637765779456> Aqui está a conta Steam que pediu, {}'.format(user.name),
                value="**Nick:** {} \n"
                      "**Conta criada em:** {} \n"
                      "**Total de jogos:** {} \n"
                      "**ID Steam:** {} \n"
                      "**Link do perfil:** {}"
                      "".format(nomeste, time.strftime("%d %B %Y às %H:%M", time.localtime(temposte)), jogosste, idste, linkste)
            )
            embedsteam.set_image(url=avatarste)
            embedsteam.set_footer(text='#ZueiroAnonimoJogaNaSteam')
            await client.send_message(message.channel, embed=embedsteam)
        except:
            await client.send_message(message.channel, "Só consigo procurar contas por ID's por enquanto ;-; \n"
                                                       "infelizmente contas sem jogos não serão mostradas por bugs.")

    if message.content.lower().startswith('zfilme'):
        user = message.author
        try:
            filme1 = message.content[7:]
            filme2 = requests.get('http://www.omdbapi.com/?apikey=c7ba758c&t=' + filme1 + '&type=movie')
            filme = json.loads(filme2.text)
            nomefil = (filme['Title'])
            anofil = (filme['Year'])
            imdbfil = (filme['imdbRating'])
            duracaofil = (filme['Runtime'])
            paisfil = (filme['Country'])
            produtorafil = (filme['Production'])
            linguagemfil = (filme['Language'])
            diretorfil = (filme['Director'])
            posterfil = (filme['Poster'])


            embedfil = discord.Embed(color=user.color)
            embedfil.add_field(name='<:10barra10:438472637765779456> Aqui está o filme 10 barra 10 que pediu, {}'.format(user.name),
                               value="🎬 **Filme:** {} \n"
                                     "                  📆 **Ano:** {} \n"
                                     "⏱ **Duração:** {} \n"
                                     "                  🔢 **Nota:** {} \n"
                                     "🎦 **Diretor:** {} \n"
                                     "                  🏨 **Produtora:** {} \n"
                                     "🌍 **País:** {} \n"
                                     "                  👅 **Linguagem:** {} \n" 
                                     "".format(nomefil, anofil, duracaofil, imdbfil, diretorfil, produtorafil, paisfil, linguagemfil)
                               )
            embedfil.set_image(url=posterfil)
            embedfil.set_footer(text="#ZueiroAninomoVirouCinéfolo")
            await client.send_message(message.channel, embed=embedfil)
        except discord.errors.HTTPException:
            await client.send_message(message.channel, "Putz grila Nilce, não consegui encontrar o filme!  :C")


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

    if message.content.lower().startswith('zserie'):
        embserie = discord.Embed(
            title='{}, aqui está sua recomendação'.format(message.author.name),
            color=azul,
            descriptino=None,
        )
        choice = random.randint(1,3)
        if choice == 1:
            tituloserie = 'Sherlock'
            sinopseserie = 'O dr. John Watson precisa de um lugar para morar em Londres. Ele é apresentado ao detetive Sherlock Holmes e os dois acabam desenvolvendo uma parceria intrigante, na qual a dupla vagará pela capital inglesa solucionando assassinatos e outros crimes brutais. Tudo isso em pleno século XXI.'
            fotinhaserie = 'http://cabanadoleitor.com.br/wp-content/uploads/2017/01/sherlock-season-4-netflix.jpg'
            authorserie = 'SHAIDERWOW#6701'
        if choice == 2:
            tituloserie = 'Game of Thrones'
            sinopseserie = 'Há muito tempo, em um tempo esquecido, uma força destruiu o equilíbrio das estações. Em uma terra onde os verões podem durar vários anos e o inverno toda uma vida, as reivindicações e as forças sobrenaturais correm as portas do Reino dos Sete Reinos. A irmandade da Patrulha da Noite busca proteger o reino de cada criatura que pode vir de lá da Muralha, mas já não tem os recursos necessários para garantir a segurança de todos. Depois de um verão de dez anos, um inverno rigoroso promete chegar com um futuro mais sombrio. Enquanto isso, conspirações e rivalidades correm no jogo político pela disputa do Trono de Ferro, o símbolo do poder absoluto.'
            fotinhaserie = 'https://upload.wikimedia.org/wikipedia/pt/a/a0/GameofThrones.png'
            authorserie = 'SHAIDERWOW#6701'
        if choice == 3:
            tituloserie = 'La casa de papel'
            sinopseserie = 'La Casa de Papel é uma série de televisão espanhola do gênero de filmes de assalto. Criada por Álex Pina para as redes televisão espanhola Antena 3, a série estreou em 2 de maio de 2017 estrelando Úrsula Corberó (Tókyo), Alba Flores (Nairóbi), Álvaro Morte (El Profesor), Itziar Ituño (Raquel Murillo), Pedro Alonso (Berlin), Paco Tous (Moscou), Jaime Lorente (Denver), Miguel Herrán (Rio), Darko Peric (Helsinque) e Roberto García (Oslo). A série foi adicionada internacionalmente no catálogo da Netflix no dia 25 de dezembro de 2017 com uma nova edição e diferente quantidade de episódios'
            fotinhaserie = 'https://pbs.twimg.com/profile_images/953288656046952448/wmbDYoH4_400x400.jpg'
            authorserie = 'Tulio 🌠#7588'


        embserie.add_field(name=tituloserie, value=sinopseserie)
        embserie.set_image(url=fotinhaserie)
        embserie.add_field(name='Recomende também!', value='`Adicione sua série também em: https://goo.gl/forms/9ijb6PLgyjEvJY5d2`')
        embserie.set_footer(text='Recomendação criada por {}.'.format(authorserie))
        recoserie = await client.send_message(message.channel, embed=embserie)
        await client.add_reaction(recoserie, '😍')
        await client.add_reaction(recoserie, '😃')
        await client.add_reaction(recoserie, '😑')
        await client.add_reaction(recoserie, '☹')




    if message.content.lower().startswith('z.py'):
        usermsgcod = message.content[4:]
        try:
            await client.send_message(message.channel,'<:python:426890674256740384> {} enviou o segunte código:\n```python\n{} \n```'.format(message.author.mention, usermsgcod))
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Esqueceu de por o código, bb.')

    if message.content.lower().startswith('zhelp'):
        user = message.author
        embhelp2 = discord.Embed(title='<:zueiro:426887690101981195> Olá, {}. <:hm:426887690101981195>'.format(message.author.name), color=user.color,
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
                                          '**zSteam** `<ID da conta>`**:** Eu lhe mostro informações sobre a conta Steam'
                                          '**zFlipcoin : **Me faz reagir com cara(😀) ou coroa(👑).\n'
                                          '**zFilme** `<nome do filme>`**:** Eu te mostro informações do filme escolhido.\n'
                                          '**zGames : **Te dá o cargo do jogo caso você reaja com o emoji relativo ao mesmo.\n'
                                          '`Obs:Só funciona se o servidor tiver os cargos`\n'
                                          '**zPing : **Exibe meu tempo de resposta.\n'
                                          '**zSugestao** `<mensagem>`**:** Envia sua sigestão diretamente pro meu dono.\n'
                                          '**z.Py** `<código>`**:** Coloca a fonte python do discord no seu código.\n'
                                          '<:python:419660191244484609>**Comandos que requerem permissões de administrador.**<:python:419660191244484609>\n'
                                          '**zAviso** `<menção>` `<mensagem>` **:** Envia uma mensagem ao usuário mencionado através de mim.\n'
                                '**ME ADICIONE AO SEU SERVIDOR**\n'
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
            title='<:python:419662789997756419> Falou comigo, {}?'.format(message.author.name),
            color=user.color,
            descriptino="VACILÃO MORRE CEDO",
        )
        embpapaco.set_image(
            url='https://images-ext-2.discordapp.net/external/UuIdfaTGI15OWrW9tZnlXD-rjkhVSzsuQXhUh7463Pg/https/i.imgur.com/T8auOavh.jpg?width=764&height=430')
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

    if message.content.lower().startswith('zaviso'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel,'Somente para ADMs do server, desculpa bb')
        try:
            user = message.mentions[0]
            msgg = message.content[6:]
            await client.send_message(user, msgg)

        except:

            await client.send_message(message.channel, 'Escreva algo para eu enviar no privado deste usuário.')

    if message.content.lower().startswith('zping'):
        timep = time.time()
        emb = discord.Embed(title='Aguarde', color=0x565656)
        pingm0 = await client.send_message(message.channel, embed=emb)
        ping = time.time() - timep
        pingm1 = discord.Embed(title='Pong!', description=':ping_pong: Ping - %.01f segundos' % ping, color=0x15ff00)
        await client.edit_message(pingm0, embed=pingm1)


    if message.content.lower().startswith('zdiga'):

        try:

            await client.send_message(message.channel, message.content[5:])
            await client.delete_message(message)

        except:

            await client.send_message(message.channel, 'Escreva algo para eu repetir.')




    elif message.content.lower().startswith('zbotinfo'):
        embedbotin = discord.Embed(
            title=" <:python:419660191244484609> Olá, sou o Zueiro Anonimo <:python:419660191244484609> ",
            color=amarelo,
            descriptino="Discord BOT Básico - sendo atualizado cada vez mais",
        )
        embedbotin.set_thumbnail(url=client.user.avatar_url)
        embedbotin.add_field(name='Discord BOT Básico', value='Sendo atualizado cada vez mais')
        embedbotin.add_field(name='Me adicione em seu server', value='http://swifttopia.com/6870268/zueiroanonimo')
        embedbotin.add_field(name='estou online em',
                             value='` ' + (str(len(client.servers))) + ' `  Serve(s) <:python:419660191244484609> ')
        embedbotin.add_field(name='Em contato com', value=str(len(set(client.get_all_members()))) + ' usuarios')
        embedbotin.set_footer(text="Copyright © 2018 - Criado por SHAIDERWOW#6701 - Quer saber mais ? digite zHelp")
        await client.send_message(message.channel, embed=embedbotin)

    elif message.content.lower().startswith('zuserinfo'):
        try:
            member = message.mentions[0]
            embedusu = discord.Embed(
                title='<:python:419660191244484609> Informações de: {} <:python:419660191244484609>'.format(
                    member.name),
                color=member.color,
                descriptino=None,
            )
            embedusu.set_thumbnail(url=member.avatar_url)
            embedusu.add_field(name="Seu Nome", value=member.name)
            embedusu.add_field(name='Seu apelido neste server', value=member.nick)
            embedusu.add_field(name="Seu Id", value=member.id)
            embedusu.add_field(name="Status", value=member.status)
            embedusu.add_field(name='Jogando:', value=member.game)
            embedusu.add_field(name="Entrou no server em", value=member.joined_at)
            embedusu.add_field(name="Maior Cargo ", value=member.top_role)
            embedusu.add_field(name="Cor", value=member.color)
            embedusu.add_field(name="Tag", value=member.discriminator)
            await client.send_message(message.channel, embed=embedusu)
        except:
            user = message.author
            embedusu1 = discord.Embed(
                title='<:python:419660191244484609> Informações de: {} <:python:419660191244484609>'.format(
                    user.name),
                color=user.color,
                descriptino=None,
            )
            embedusu1.set_thumbnail(url=user.avatar_url)
            embedusu1.add_field(name="Seu Nome", value=user.name)
            embedusu1.add_field(name='Seu apelido neste server', value=user.nick)
            embedusu1.add_field(name="Seu Id", value=user.id)
            embedusu1.add_field(name="Status", value=user.status)
            embedusu1.add_field(name='Jogando:', value=user.game)
            embedusu1.add_field(name="Entrou no server em", value=user.joined_at)
            embedusu1.add_field(name="Maior Cargo ", value=user.top_role)
            embedusu1.add_field(name="Cor", value=user.color)
            embedusu1.add_field(name="Tag", value=user.discriminator)
            await client.send_message(message.channel, embed=embedusu1)


    elif message.content.lower().startswith('zavatar'):
        try:
            member = message.mentions[0]
            embed = discord.Embed(
                title='<:python:419660191244484609> Avatar de: {} <:python:419660191244484609>'.format(member.name),
                color=member.color,
                description='Reaja ao avatar de {}! <:python:419660191244484609>'.format(
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
                title='<:python:419660191244484609> Avatar de: {} <:python:419660191244484609>'.format(user.name),
                color=user.color,
                description='Reaja ao avatar de {}! <:python:419660191244484609>'.format(
                    user.name))
            embedavata.set_image(url=user.avatar_url)
            avatar2 = await client.send_message(message.channel, embed=embedavata)
            await client.add_reaction(avatar2, '👍')
            await client.add_reaction(avatar2, '❤')
            await client.add_reaction(avatar2, '😂')
            await client.add_reaction(avatar2, '😱')
            await client.add_reaction(avatar2, '💩')


    elif message.content.lower().startswith('zserverinfo'):
        server = message.server
        online = len([m.status for m in message.server.members
                      if m.status == discord.Status.online or
                      m.status == discord.Status.idle])

        embed3 = discord.Embed(
            title="Informações do server <:python:419660191244484609> ",
            color=amarelo,
            descriptino=None,
        )
        embed3.add_field(name="Server name", value=message.server.name, inline=True)
        embed3.add_field(name="Criado em", value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        embed3.add_field(name="Server ID", value=message.server.id, inline=True)
        embed3.add_field(name="Dono", value=message.server.owner.mention)
        embed3.add_field(name="Numero de cargos", value=len(message.server.roles), inline=True)
        embed3.add_field(name="Membros", value=len(message.server.members), inline=True)
        embed3.add_field(name="Online", value=f"**{online}/{len(message.server.members)}**")
        embed3.add_field(name="Região do Server", value=str(message.server.region).title())
        embed3.add_field(name="Emojis", value=f"{len(message.server.emojis)}/100")
        embed3.set_thumbnail(url=message.server.icon_url)
        embed3.set_footer(text="Copyright © 2018 - SHAIDERWOW - Zueiros Anonimous")
        await client.send_message(message.channel, embed=embed3)

    if message.content.lower().startswith('zgpsteam'):
        await client.send_message(message.channel, "```Entra lá bb``` \nhttps://goo.gl/R2mC2g")

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
        embed1 = discord.Embed(
            title="Escolha seus jogos!",
            color=roxo,
            description="- CS:GO = 🔫\n"
                        "- Gartic  =  🖌 \n"
                        "- GTA V  = 💰\n"
                        "- PUBG = 🛡\n"
                        "- Brawlhalla = ⚔\n"
                        "- VRCHAT = 📺\n"
                        "- League of Legends = ⌛\n"
                        "- Roblox = 📦\n"
                        "Breve mais...\n"
                        "Digite 'zHelp' para saber sobre mim",
        )

    botmsg = await client.send_message(message.channel, embed=embed1)

    await client.add_reaction(botmsg, "🔫")
    await client.add_reaction(botmsg, "🖌")
    await client.add_reaction(botmsg, "💰")
    await client.add_reaction(botmsg, "🛡")
    await client.add_reaction(botmsg, "⚔")
    await client.add_reaction(botmsg, "📺")
    await client.add_reaction(botmsg, "⌛")
    await client.add_reaction(botmsg, "📦")

    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author


@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🔫" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "CS:GO", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "🖌" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Gartic", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "💰" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "GTA V", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "🛡" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "PUBG", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "⚔" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Brawlhalla", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "📺" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "VRCHAT", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "⌛" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "League of Legends", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "📦" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Roblox", msg.server.roles)
        await client.add_roles(user, role)
        print("add")






@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🔫" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "CS:GO", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "🖌" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Gartic", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "💰" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "GTA V", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "🛡" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "PUBG", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "⚔" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Brawlhalla", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "📺" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "VRCHAT", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "⌛" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "League of Legends", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "📦" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Roblox", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")


@client.event
async def on_member_join(member):
    canal = client.get_channel("417466650451771394")
    regras = client.get_channel("420007865894567946")
    msg = "Bem Vindo ao {}, {}\n Quem sou eu ? eu sou um BOT muito gente boa S2\n Para ver meus comandos digite `zHelp`".format(member.server.name, member.mention)
    await client.send_message(member, msg)  # substitua canal por member para enviar a msg no DM do membro


@client.event
async def on_member_remove(member):
    canal = client.get_channel("417466650451771394")
    msg = "Adeus garotinho juvenil {}, este server será sua falta".format(member.mention)
    await client.send_message(member, msg)  # substitua canal por member para enviar a msg no DM do membro


client.run(token)
