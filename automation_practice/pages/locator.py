from collections import namedtuple

# setting namedtuple Locator with 'by' and 'value' used by BaseElement class to find elements on the page
Locator = namedtuple('Locator', ['by', 'value'])
