from discord_webhook import DiscordWebhook, DiscordEmbed


def send_notifications(hook, title, description, color, fields):
    notification = DiscordWebhook(url=hook)
    # create embed object for webhook
    embed = DiscordEmbed(title=title, description=description, color=color)
    fields = fields

    for field in fields:
         embed.add_embed_field(name=field[0], value=field[1])

    notification.add_embed(embed)
    response = notification.execute()
