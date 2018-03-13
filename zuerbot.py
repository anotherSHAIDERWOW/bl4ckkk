
import random
import discord
import asyncio
import random
import secreto

client = discord.Client ()

roxo =0x690FC3
token = secreto.seu_token()
msg_id = None
msg_user = None

@client.event
async def on_ready ():
    print('BOT ONLINE - Testando')
    print(client.user.name)
    print(client.user.id)
    print('https://discord.gg/CmszJUV')


@client.event
async def on_message(message):
    if message.content.lower().startswith('zhelp'):
        await client.send_message(message.channel, "```http\nOlá,\nNo momento ainda não estou pronto, porem posso lhe servir em algumas coisas...\nVou deixar alguns emojis abaixo para lhe ajudar\n- Me adicione ao seu Discord  https://goo.gl/SJCndF \n- Servidor oficial https://discord.gg/CmszJUV \n- Comandos:\nzHelp = aparece esta mensagem\nzFlipcoin = cara ou coroa \nzGames = Aparece uma lista de jogos e se você clicar em um dos emotes você ganha o cargo dele, entretando só ganhará o cargo se o servidor tiver os seguintes cargos:\n      CS:GO, League of Legends, Gartic, VRCHAT, Brawlhalla, GTA V, PUBG, Roblox\n       (Obs. os cargos (roles) devem estar escritos igual ao que está acima)\nzSteam = mostra nosso Grupo da Steam\nBreve mais coisas...```")


    if message.content.lower().startswith('zsteam'):
        await client.send_message(message.channel, "{0.author.mention}```Entra lá bb``` \nhttps://goo.gl/R2mC2g")

    if message.content.lower().startswith('zflipcoin'):
        choice = random.randint(1,2)
        if choice == 1:
          await client.add_reaction (message, '😀')
        if choice == 2:
          await client.add_reaction (message, '👑')

    if message.content.lower().startswith("zgames"):
     embed1 =discord.Embed(
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

    if reaction.emoji == "🔫" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "CS:GO", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🖌" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Gartic", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "💰" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "GTA V", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🛡" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "PUBG", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⚔" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Brawlhalla", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "📺" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "VRCHAT", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⌛" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "League of Legends", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "📦" and msg.id == msg_id: #and user == msg_user:
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

client.run(token)
