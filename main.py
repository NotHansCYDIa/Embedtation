import discord
import json
import os
from keep_alive import *
from discord.ext import commands
from typing import Optional, Literal
from discord import app_commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# guild = discord.Object(id=1110454353401237547)
token = os.environ['Token']


class abot(discord.Client):

  def __init__(self):
    super().__init__(intents=discord.Intents.default())
    self.synced = False

  async def on_ready(self):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="commands"), status=discord.Status.online)
    await tree.sync()
    self.synced = True
    self.embeddata = {
      "title":
      "",
      "color":
      discord.Colour.random(),
      "optional": [{
        "description": "",
        "linkurl": "",
        "author": "",
        "authorimageurl": "",
        "authorlink": "",
        "thumbnailurl": "",
        "iconimageurl": "",
        "footer": "",
        "footericonurl": ""
      }],
      "fields": []
    }
    print("===== Embedtation =====")
    print("     bot is ready")


bot = abot()
tree = app_commands.CommandTree(bot)
cl = Literal["Red", "Orange", "Brown", "Yellow", "Green", "Blue", "Purple",
             "Pink", "Random"]


@tree.command(name="create",
              description="Create a new fresh embed")
async def createself(interaction: discord.Interaction, title: str, color: cl,
                     description: Optional[str], linkurl: Optional[str],
                     author: Optional[str], authorimageurl: Optional[str],
                     authorlink: Optional[str], thumbnailurl: Optional[str],
                     iconimageurl: Optional[str], footer: Optional[str],
                     footericonurl: Optional[str]):

  bot.embeddata = {
    "title":
    "",
    "color":
    discord.Colour.random(),
    "optional": [{
      "description": "",
      "linkurl": "",
      "author": "",
      "authorimageurl": "",
      "authorlink": "",
      "thumbnailurl": "",
      "iconimageurl": "",
      "footer": "",
      "footericonurl": ""
    }],
    "fields": []
  }
  data = bot.embeddata
  data['title'] = title

  if color == "Red":
    data['color'] = discord.Colour.red()
  elif color == "Orange":
    data['color'] = discord.Colour.orange()
  elif color == "Brown":
    data['color'] = discord.Colour.brown()
  elif color == "Yellow":
    data['color'] = discord.Colour.yellow()
  elif color == "Green":
    data['color'] = discord.Colour.green()
  elif color == "Blue":
    data['color'] = discord.Colour.blue()
  elif color == "Purple":
    data['color'] = discord.Colour.purple()
  elif color == "Pink":
    data['color'] = discord.Colour.magenta()
  else:
    data['color'] = discord.Colour.random()

  data['optional'][0]['description'] = description
  data['optional'][0]['linkurl'] = linkurl
  data['optional'][0]['author'] = author
  data['optional'][0]['authorimageurl'] = authorimageurl
  data['optional'][0]['authorlink'] = authorlink
  data['optional'][0]['thumbnailurl'] = thumbnailurl
  data['optional'][0]['iconimageurl'] = iconimageurl
  data['optional'][0]['footer'] = footer
  data['optional'][0]['footericonurl'] = footericonurl
  
  embed = discord.Embed(
    title="Created!",
    description=
    "You have created an embed! Do </addfield:1113731529957453886> to make a new field or do </embed:1113736865200226304> to run/message the embed.",
    colour=discord.Colour.green())
  await interaction.response.send_message(embed=embed, ephemeral=True)


@tree.command(name="addfield",
              description="Add a field to the embed")
async def afself(interaction: discord.Interaction, title: str,
                 description: str, inlined: bool):

  data = bot.embeddata

  dn = {"title": title, "description": description, "inlined": inlined}

  data['fields'].append(dn)

  embed = discord.Embed(
    title=f"Created {title}!",
    description=
    "Successfully Created a new field! You can run the command again or do </embed:1113736865200226304> if your finish to run the embed.",
    colour=discord.Colour.green())
  await interaction.response.send_message(embed=embed, ephemeral=True)


@tree.command(name="removefield",
              description="Remove a field from the embed")
async def removefield(interaction: discord.Interaction, title: str):
  data = bot.embeddata
  removed_fields = []

  for field in data['fields']:
    if field['title'] == title:
      data['fields'].remove(field)
      removed_fields.append(field)

  if removed_fields:

    embed = discord.Embed(
      title="Successful!",
      description=f"Removed field that has the title \"{title}\"",
      colour=discord.Colour.green())
    await interaction.response.send_message(embed=embed, ephemeral=True)
  else:

    embed = discord.Embed(
      title="Error",
      description=f"There are no field that has the title \"{title}\"",
      colour=discord.Colour.red())
    await interaction.response.send_message(embed=embed, ephemeral=True)


@tree.command(name="embed", description="Run/Message embed")
async def embedself(interaction: discord.Interaction):

  data = bot.embeddata
  opt = data["optional"][0]

  if data["title"] == "" or data["title"] == None:
    await interaction.response.send_message(
      "Please create a new embed by doing /create.", ephemeral=True)
  else:
    embed = discord.Embed(title=data["title"],
                          description=opt["description"],
                          colour=data["color"],
                          url=opt["linkurl"])
    embed.set_thumbnail(url=opt["thumbnailurl"])
    embed.set_image(url=opt["thumbnailurl"])
    if opt["author"] is not None:
      embed.set_author(name=opt["author"],
                       url=opt["authorlink"],
                       icon_url=opt["authorimageurl"])
    embed.set_footer(text=opt["footer"], icon_url=opt["footericonurl"])

    for field in data['fields']:
      embed.add_field(name=field['title'],
                      value=field['description'],
                      inline=field['inlined'])

    await interaction.response.send_message(embed=embed)

@tree.command(name="instructions", description="Instructions on how to create an embed")
async def instructionsself(interaction: discord.Interaction):

    embed = discord.Embed(title="Instructions", description="Instructions on how to create an embed", colour=discord.Colour.green())
    embed.add_field(name="Create a new embed", value="To create a new embed, use </create:1113716720440459325>. If you created a new embed before and you wanted to create one, IT WILL OVERRIDE THE EMBED YOU CREATED.", inline=False)
    embed.add_field(name="Creating fields and removing them.", value="To create fields after you created your new embed, do </addfield:1113731529957453886>. To remove a field then do </removefield:1113733288398422067>.", inline=False)
    embed.add_field(name="Running Embeds", value="To message/run the embed, use </embed:1113736865200226304> then you're done!", inline=False)


    await interaction.response.send_message(embed=embed, ephemeral=True)



keep_alive()
bot.run(token)
