import discord
from discord.ext import commands    
import asyncio
import time
import time
import requests


from PIL import Image
from io import BytesIO
from functools import partial
from operator import is_not
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
        global response
        response = requests.get(url, headers = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) ''AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/45.0.2454.101 Safari/537.36'),})
        if response.status_code in {200,503}:
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
    print("parsed       ")
    #checking to extract <h> tag or <title> tag
    try:
        h = str(page_soup.body.h1 or page_soup.body.h2 or page_soup.body.h3)
        if(len(h) > 35):
            """whitelist = set('abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ')
            white_list_result = ''.join(filter(whitelist.__contains__,h))
            white_list_existing_domain_clean = white_list_result[1:]
            white_list_existing_domain_clean_2 = white_list_existing_domain_clean[:-1]"""
            title = str(page_soup.title)
            print("found meaning")
            website_meaning = remove_symbols(title)            
            if(website_meaning == "None"):
                website_meaning = "Parked"
            if("&amp;" in website_meaning):
                website_meaning = website_meaning.replace("&amp;","&",3)

            return website_meaning 

        elif(len(h) < 35):
            print("found meaning")
            website_meaning = remove_symbols(h)
            

            if("is for sale" in website_meaning):
                website_meaning = "Is for sale (parked)"
            if(website_meaning == "None"):
                website_meaning = "Parked"
            if("&amp;" in website_meaning):
                website_meaning = website_meaning.replace("&amp;","&",3)
            return website_meaning  
        # Fix bug, cannot handle
        # =mix trees cars
        else:
            print('Not found yet')
            return "Parked"
    # Fix bug, cannot handle
    # =mix trees cars
    except:
        print('Not found yet')
        return "Parked"
        

    

          




############# TO DO
# 4) Move all functions to top
# 5) Name functions real words
# 6) async
# 7) combine parsing with checking if it exists

@bot.command(pass_context=True)
async def mix(ctx, domain_1: str = None, domain_2: str = None, domain_3: str = None, domain_4: str = None, domain_5: str = None):
    await ctx.send('May take upto 1 minute')

    part1 = []
    part2 = []
    part3 = []
    part4 = []
    part5 = []
    part6 = []
    part7 = []
    part8 = []
    part9 = []
    part10 = []
    
    possible_domain_list = []
    start_time = time.time()
    all_domains = []
    existing_domain_list = []

    var_counter = 1
    real_var_counter = 0
    existing_vars = []
    while(var_counter < 6):
        if 'domain_' + str(var_counter) in locals():
            if locals()['domain_' + str(var_counter)] != None:
                existing_vars.append(locals()['domain_' + str(var_counter)])
                real_var_counter = real_var_counter + 1
        var_counter = var_counter + 1
    print(existing_vars)


    var_z = 0
    var_y = 1
    
    while(var_z < len(existing_vars)):
        replace_y = var_y
        while(var_y < len(existing_vars)):
            print("mixing " + str(var_z) + " with " + str(var_y))
            possible_domain_list.extend((   
            # simple
            'http://www.' + existing_vars[var_z] + existing_vars[var_y] + '.com',
            'http://www.' + existing_vars[var_y] + existing_vars[var_z] + '.com',
            # random
            'http://www.' + existing_vars[var_z][:2] + existing_vars[var_y][:2] + '.com',
            'http://www.' + existing_vars[var_y][:2] + existing_vars[var_z][:1] + '.com',
            'http://www.' + existing_vars[var_z][:-1] + existing_vars[var_y] + '.com',
            'http://www.' + existing_vars[var_z][:-1] + existing_vars[var_y][-1:] + '.com',
            'http://www.' + existing_vars[var_z][:-1] + existing_vars[var_y][1:] + '.com',
            'http://www.' + existing_vars[var_z] + existing_vars[var_y][-1:] + '.com',
            'http://www.' + existing_vars[var_z] + existing_vars[var_y][1:] + '.com',
            'http://www.' + existing_vars[var_z] + existing_vars[var_y][-2: -1] + '.com',
            'http://www.' + existing_vars[var_z][:1] + existing_vars[var_y] + '.com',
            'http://www.' + existing_vars[var_z][:1] + existing_vars[var_y][-1:] + '.com',
            'http://www.' + existing_vars[var_z][:1] + existing_vars[var_y][1:] + '.com',
            ))
        
            if existing_vars[var_z].endswith('s'):
                domain_1_new = existing_vars[var_z][:-1]
                possible_domain_list.extend((
                'http://www.' + domain_1_new + existing_vars[var_y] + '.com',
                'http://www.' + existing_vars[var_y] + domain_1_new + '.com'
                ))

            if existing_vars[var_y].endswith('s'):
                domain_2_new = existing_vars[var_y][:-1]
                possible_domain_list.extend((
                'http://www.' + domain_2_new + existing_vars[var_z] + '.com',
                'http://www.' + existing_vars[var_z] + domain_2_new + '.com'
                ))
                

            if existing_vars[var_z].endswith('s') and existing_vars[var_y].endswith('s'):
                domain_1_new = existing_vars[var_z][:-1]
                domain_2_new = existing_vars[var_y][:-1] 
                possible_domain_list.extend((
                'http://www.' + domain_1_new + domain_2_new + '.com',
                'http://www.' + domain_2_new + domain_1_new + '.com'
                ))
            var_y = var_y + 1
            #print("var_y is now: " + str(var_y))
        var_y = replace_y + 1
        #print("var_y new is now: " + str(var_y))
        var_z = var_z + 1
        #print("var_z is now: " + str(var_z))



    for url in possible_domain_list:
        page_html = grab_website(url)
        if page_html:


            #        200's
            if(response.status_code == 200):
                #appending domain
                all_domains.append("<" + url + ">")

                website_meaning = parse_html(page_html)
                all_domains.append('**' + str(website_meaning) + '**' + "\n")
                #existing_domains_list.extend((url, "Status code: 200", ))
            #        300's
            if(response.status_code == 301):
                #appending domain
                all_domains.append("<" + url + ">")
                all_domains.append('**' + "Perma moved" + '**' + "\n")
                
            if(response.status_code == 302 or response.status_code == 307):
                #appending domain
                all_domains.append("<" + url + ">")
                all_domains.append('**' + "Redirection" + '**' + "\n")
        
            
            #        500's
            if(response.status_code == 503):
                #appending domain
                all_domains.append("<" + url + ">")
                all_domains.append('**' + "Under maintenance" + '**' + "\n")
                
            if(response.status_code == 500):
                #appending domain
                all_domains.append("<" + url + ">")
                all_domains.append('**' + "Server Error" + '**' + "\n")
                
            if(response.status_code == 550):
                #appending domain
                all_domains.append("<" + url + ">")
                all_domains.append('**' + "Permission Denied!" + '**' + "\n")
        else:
            
            all_domains.append("<" + url + ">")
            all_domains.append("**Website does not exist!**" + "\n")

    await ctx.send( " ".join(map(str,all_domains)))
    print('User has mixed with these 2 keywoards: ' + domain_1 + ' and ' + domain_2)
    


    end_time = time.time()
    print("took the bot: " + str(end_time - start_time) + " seconds to run")
    





