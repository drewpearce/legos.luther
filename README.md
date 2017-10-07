# legos.luther

[![Travis](https://travis-ci.org/drewpearce/legos.luther.svg)]()]

Automatically insult your friend -- Martin Luther style.
Happy 500th Anniversary, Reformation!

The Lego module system and Legobot are a FOSS project lovingly crafted by [Bren Briggs and friends](https://github.com/Legobot/Legobot)! All code borrowed from Legobot is ~~stolen~~ lovingly used in their honor.

## Usage
This lego is invoked by calling `!luther` to get a random insult.
If you wish to direct your hatred to a specific person or object, simply include the addressee after the invocation.
Examples: `!luther @legobo` or `!luther Fax machines`

## Installation
This lego fetches its data from https://api.drewpearce.tech, which requires an API key to be included in *config.ini*. If you need a key, contact the [author](https://github.com/drewpearce).
```ini
[luther]
api_key=your_api_key
```

```python
# This is the legobot stuff
from Legobot import Lego
# This is your lego
from legos.luther import Luther

# Legobot stuff here
lock = threading.Lock()
baseplate = Lego.start(None, lock)
baseplate_proxy = baseplate.proxy()

# Add your lego
baseplate_proxy.add_child(Luther, api_key=config['luther']['api_key'])
```
