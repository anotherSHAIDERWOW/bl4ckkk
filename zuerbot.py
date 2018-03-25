import discord
from discord.ext import commands
import random
import asyncio
import random
import os
import io
import re
import time
import requests

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
    if message.content.lower().startswith('zhelp'):
        await client.send_message(message.channel,
                                  "```http\nOlá,\nNo momento ainda não estou pronto, porem posso lhe servir em algumas coisas...\nVou deixar algumas infos abaixo para lhe ajudar\n- Me adicione ao seu Discord  https://goo.gl/SJCndF \n- Servidor oficial CmszJUV``` \n ```- Comandos:\nzHelp = aparece esta mensagem\nzFlipcoin = cara ou coroa \nzVotar (mensagem) = o faz uma votação de acordo com sua pergunta\nzGames = Aparece uma lista de jogos e se você clicar em um dos emotes você ganha o cargo dele, entretando só ganhará o cargo se o servidor tiver os seguintes cargos:\n      CS:GO, League of Legends, Gartic, VRCHAT, Brawlhalla, GTA V, PUBG, Roblox\n       (Obs. os cargos (roles) devem estar escritos igual ao que está acima)\nzSteam = mostra nosso Grupo da Steam\nzAvatar {usuário} = mostra o avatar daquele usuário que foi mencionado\nzServerinfo = mostra as informações do server\nzBotinfo = mostra informações do BOT\nzUserinfo (usuário) = mostra as informações do usuário mencionado\nzGif = Manda um gif aleatório \nBreve mais coisas...```")

    if message.content.lower().startswith('<@421862224454221824>'):
        imagem = requests.get('https://images-ext-2.discordapp.net/external/UuIdfaTGI15OWrW9tZnlXD-rjkhVSzsuQXhUh7463Pg/https/i.imgur.com/T8auOavh.jpg?width=764&height=430', stream=True)
        await client.send_file(message.channel, io.BytesIO(imagem.raw.read()), filename='zueiroanonimo.png', content='<:python:419662789997756419> Falou comigo, {}?'.format(message.author.mention))

    if message.content.lower().startswith('zaviso'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel,embed=errorembedpermi)
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
            color=verde,
            descriptino="Discord BOT Básico - sendo atualizado cada vez mais",
        )
        embedbotin.set_thumbnail(url=client.user.avatar_url)
        embedbotin.add_field(name='Discord BOT Básico', value='Sendo atualizado cada vez mais')
        embedbotin.add_field(name='Me adicione em seu server', value='https://goo.gl/SJCndF ')
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
                description='[Clique aqui](' + member.avatar_url + ') para acessar o link do avatar de {}! <:python:419660191244484609>'.format(
                    member.name))
            embed.set_image(url=member.avatar_url)
            await client.send_message(message.channel, embed=embed)

        except:
            user = message.author
            embedavata = discord.Embed(
                title='<:python:419660191244484609> Avatar de: {} <:python:419660191244484609>'.format(user.name),
                description='[Clique aqui](' + user.avatar_url + ') para acessar o link do avatar de {}! <:python:419660191244484609>'.format(
                    user.name))
            embedavata.set_image(url=user.avatar_url)
            await client.send_message(message.channel, embed=embedavata)




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

    if message.content.lower().startswith('zsteam'):
        await client.send_message(message.channel, "```Entra lá bb``` \nhttps://goo.gl/R2mC2g")

    if message.content.lower().startswith('zgif'):
        choice = random.randint(1, 11)
        if choice == 1:
            await client.send_message(message.channel,
                                      " <:python:420390751399051265> https://i.pinimg.com/originals/03/38/ed/0338ed402affbb1f80961f09a7153d35.gif")
        if choice == 2:
            await client.send_message(message.channel, " <:python:420390751399051265>  https://www.tenor.co/O1zu.gif")
        if choice == 3:
            await client.send_message(message.channel,
                                      " <:python:420390751399051265>  https://media.giphy.com/media/Ewd3jzmdc9XKo/giphy.gif")
        if choice == 4:
            await client.send_message(message.channel,
                                      " <:python:420390751399051265>  https://i.pinimg.com/originals/82/32/0d/82320d4e1f8d1b1f4a7878817cc02bb9.gif")
        if choice == 5:
            await client.send_message(message.channel,
                                      " <:python:420390751399051265>  http://1.bp.blogspot.com/--a2oXKQftfs/Ua5gSz1aSXI/AAAAAAAAEAk/kKlQQB8liyg/s1600/huehuehue-brbrbr-oque-e-significado-brchan-b-como-usar-humortalouco.gif")
        if choice == 6:
            await client.send_message(message.channel,
                                      " <:python:420390751399051265>  https://img.buzzfeed.com/buzzfeed-static/static/2017-04/21/12/asset/buzzfeed-prod-fastlane-03/anigif_sub-buzz-8560-1492791743-1.gif")
        if choice == 7:
            await client.send_message(message.channel,
                                      " <:python:420390751399051265>  https://im-01.gifer.com/BkSi.gif")
        if choice == 8:
            await client.send_message(message.channel,
                                      " <:python:420390751399051265>  http://muitobacana.com/wp-content/uploads/2017/09/gif-engra%C3%A7ado-que-se-mexe-para-whatsapp-7.gif")
        if choice == 9:
            await client.send_message(message.channel,
                                      " <:python:420390751399051265>  https://zippy.gfycat.com/DefensiveFrayedGentoopenguin.gif")
        if choice == 10:
            await client.send_message(message.channel,
                                      " <:python:420390751399051265> http://www.whatstube.com.br/wp-content/uploads/2016/08/quando-o-desespero-bate.gif")
        if choice == 11:
            await client.send_message(message.channel, " <:python:420390751399051265>  https://www.tenor.co/RhQf.gif")

    if message.content.lower().startswith('zflipcoin'):
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '😀')
        if choice == 2:
            await client.add_reaction(message, '👑')

    if message.content.lower().startswith('zvotar'):
        try:
            phrase = message.content[6:]
            embed4 = discord.Embed(title="VOTAÇÃO", description=" \n ", color=amarelo)
            embed4.add_field(name="{} Opinou...".format(message.author.name), value="{}".format(phrase),
                           inline=False)
            embed4.set_thumbnail(url=message.author.avatar_url)
            votacao = await client.send_message(message.channel, embed=embed4)
            await client.delete_message(message)
            await client.add_reaction(votacao, '✅')
            await client.add_reaction(votacao, '❌')

        except:

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
    msg = "Bem Vindo ao {}, {}\n Quem sou eu ? eu sou um BOT muito gente boa S2\n Para ver meus comandos digite `zHelp`".format(
        member.mention)
    await client.send_message(member, msg)  # substitua canal por member para enviar a msg no DM do membro


@client.event
async def on_member_remove(member):
    canal = client.get_channel("417466650451771394")
    msg = "Adeus garotinho juvenil {}, este server será sua falta".format(member.mention)
    await client.send_message(member, msg)  # substitua canal por member para enviar a msg no DM do membro


client.run(token)
