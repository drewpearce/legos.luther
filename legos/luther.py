from Legobot.Lego import Lego
import requests
import logging
import json

logger = logging.getLogger(__name__)

class Luther(Lego):
    def listening_for(self, message):
        if message['text'] is not None:
            try:
                return message['text'].split()[0] == '!luther'
            except Exception as e:
                logger.error('''Luther lego failed to check message text:
                            {}'''.format(e))
                return False
    def handle(self, message):
        logger.debug('Handling message...')
        opts = self._handle_opts(message)
        # Set a default return_val in case we can't handle our crap
        return_val = '¯\_(ツ)_/¯'
        random_insult = self._get_insult()
        return_val = random_insult

        self.reply(message, return_val, opts)

    def _handle_opts(self, message):
        try:
            target = message['metadata']['source_channel']
            opts = {'target': target}
        except IndexError:
            opts = None
            logger.error('''Could not identify message source in message:
                        {}'''.format(str(message)))
        return opts

    def _get_insult(self):
        insult_request = requests.get('https://api.drewpearce.tech/api/v2/random_luther?api_key=d8209ab55fbafeb4e13d4bde17532613d04ce119601077ae931f96df6e84653b')
        if insult_request.status_code == requests.codes.ok:
            insult = insult_request.text
        else:
            insult = 'There was an error retrieving your insult.'
        return insult

    def get_name(self):
        return 'luther'

    def get_help(self):
        return 'Fetch a Martin Luther insult. Usage: !luther [username|some noun]'
