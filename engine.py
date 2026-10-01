class Engine():
    def __init__(self, bot_settings):
        self.bot_settings = bot_settings

    def show_settings(self):
        return self.bot_settings