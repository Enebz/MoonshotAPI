import yaml

with open("config.yml", 'r') as stream:
    conf = yaml.safe_load(stream)

def GetCommandConfig(ctx):
    cmd = ctx.command
    return conf["Cogs"][cmd.cog.qualified_name][cmd.name]
