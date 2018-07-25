import discord
from discord.ext import commands    
import asyncio
import time
import time
import requests



from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen




bot = commands.Bot(command_prefix = "=")

bot.remove_command('help')

print (discord.__version__)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True)
async def send( ctx, channel_id: str = None,  message: str = None,  user: discord.Member = None):
    user = user or ctx.author
    message = message or 'No context'
    channel_id = channel_id or 454956226099413003
    await ctx.bot.get_channel(int(channel_id)).send(message)
    await ctx.bot.get_channel(int(channel_id)).send('Sent by: {}'.format(user.name))
    print('channel_id is: ' + channel_id)    
    print('message is: ' + message)
    print("{} was the one that sent the message".format(user.name))
    print('------')

@bot.command(pass_context=True)         
async def send_private( ctx, channel_id: str = None,  message: str = None,  user: discord.Member = None):
    user = user or ctx.author
    message = message or 'No context'
    channel_id = channel_id or 454956226099413003
    await ctx.bot.get_channel(int(channel_id)).send(str(message))
    print('channel_id is: ' + channel_id)    
    print('message is: ' + message)
    print ("{} was the one that sent the message".format(user.name))
    print('------')

@bot.command(pass_context=True)
async def help_send(ctx):
    author = ctx.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )


    embed.set_author(name='Help')
    embed.add_field(name="=send or =send_private" , value="you can send a message to another channel / server. Just type =send + Channel ID + Message. =send_private does not show the senders name and =send does." , inline=False)
    
    await author.send(author , embed=embed)


########### Functions

"""def does_website_exist(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except requests.exceptions.ConnectionError:
        return False"""

def grab_website(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'})
        if response.status_code == 200:
            return response.content
    except requests.exceptions.ConnectionError:
        return False

def remove_symbols(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '<':
            skip1c += 1
        elif i == '<':
            skip2c += 1
        elif i == '>' and skip1c > 0:                                   
            skip1c -= 1
        elif i == '/>'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret 

def parse_html(html):
    page_soup = soup(html, "html.parser")
    print("parsehtml")
    #checking to extract <h> tag or <title> tag
    try:
        h = str(page_soup.body.h1 or page_soup.body.h2 or page_soup.body.h3)
        if(len(h) > 35):
            """whitelist = set('abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ')
            white_list_result = ''.join(filter(whitelist.__contains__,h))
            white_list_existing_domain_clean = white_list_result[1:]
            white_list_existing_domain_clean_2 = white_list_existing_domain_clean[:-1]"""
            title = str(page_soup.title)

            website_meaning = remove_symbols(title)            
            if(website_meaning == "None"):
                website_meaning = "Either Parked/Not set up"
            if("&amp;" in website_meaning):
                website_meaning = website_meaning.replace("&amp;","&",3)

            return website_meaning 

        elif(len(h) < 35):
            print("helloelif")
            website_meaning = remove_symbols(h)
            
            if(website_meaning == "None"):
                website_meaning = "Either Parked/Not set up"
            if("&amp;" in website_meaning):
                website_meaning = website_meaning.replace("&amp;","&",3)
            return website_meaning
        # Fix bug, cannot handle
        # =mix trees cars
        else:
            print('Not found yet')
            return "Either Parked/Not set up"
    # Fix bug, cannot handle
    # =mix trees cars
    except:
        print('Not found yet')
        return "Either Parked/Not set up"
        
    




############# TO DO
# 4) Move all functions to top
# 5) Name functions real words
# 6) async
# 7) combine parsing with checking if it exists

@bot.command(pass_context=True)
async def mix(ctx, domain_1: str = None, domain_2: str = None):
    await ctx.send('May take upto 1 minute')
    possible_domain_list = []
    start_time = time.time()
    existing_domain_list = []



    possible_domain_list.extend((
    # simple
    'http://www.' + domain_1 + domain_2 + '.com',
    'http://www.' + domain_2 + domain_1 + '.com',
    # random
    'http://www.' + domain_1[:2] + domain_2[:2] + '.com',
    'http://www.' + domain_2[:2] + domain_1[:1] + '.com',
    'http://www.' + domain_1[:-1] + domain_2 + '.com',
    'http://www.' + domain_1[:-1] + domain_2[-1:] + '.com',
    'http://www.' + domain_1[:-1] + domain_2[1:] + '.com',
    'http://www.' + domain_1 + domain_2[-1:] + '.com',
    'http://www.' + domain_1 + domain_2[1:] + '.com',
    'http://www.' + domain_1 + domain_2[-2: -1] + '.com',
    'http://www.' + domain_1[:1] + domain_2 + '.com',
    'http://www.' + domain_1[:1] + domain_2[-1:] + '.com',
    'http://www.' + domain_1[:1] + domain_2[1:] + '.com',
    'http://www.' + domain_1[:1] + domain_2[-2:] + '.com'
    ))
   
    if domain_1.endswith('s'):
        domain_1_new = domain_1[:-1]
        possible_domain_list.extend((
        'http://www.' + domain_1_new + domain_2 + '.com',
        'http://www.' + domain_2 + domain_1_new + '.com'
        ))

    if domain_2.endswith('s'):
        domain_2_new = domain_2[:-1]
        possible_domain_list.extend((
        'http://www.' + domain_2_new + domain_1 + '.com',
        'http://www.' + domain_1 + domain_2_new + '.com'
        ))
        

    if domain_1.endswith('s') and domain_2.endswith('s'):
        domain_1_new = domain_1[:-1]
        domain_2_new = domain_2[:-1] 
        possible_domain_list.extend((
        'http://www.' + domain_1_new + domain_2_new + '.com',
        'http://www.' + domain_2_new + domain_1_new + '.com'
        ))

    for url in possible_domain_list:
        page_html = grab_website(url)
        if page_html:
            #appending domain
            existing_domain_list.append(url)

            website_meaning = parse_html(page_html)
            existing_domain_list.append('**' + str(website_meaning) + '**')

            #appending bool
            existing_domain_list.append("**[True]**")
        else:
            existing_domain_list.append(url)
            existing_domain_list.append("**[False]**")

    await ctx.send(existing_domain_list)    
    print('User has mixed with these 2 keywoards: ' + domain_1 + ' and ' + domain_2)
    
    end_time = time.time()
    print("took the bot: " + str(end_time - start_time) + " seconds to run")
    




bot.run("NDUyMTU4NjQ0NTcwNjg1NDgz.DfMfYg.8WELyB2sjA-jVhPKYnWW08Hvsic")
