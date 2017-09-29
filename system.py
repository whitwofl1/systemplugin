from errbot import BotPlugin, botcmd
import os
hostname ="google.com"
response = os.system("ping -c 1" + hostname)

class System(BotPlugin):
    """
    This is a very basic system plugin
    """

    @botcmd  # flags a command
    def ping(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot can reach out
        """
        return response  # This string format is markdown.
