from bs4 import BeautifulSoup

class Semanticizer:
    def __init__(self, tag_mappings=None):
        self.tag_mappings = tag_mappings or {
            'div.nav': 'nav',
            'div.header': 'header',
            'div.footer': 'footer',
            'div.article': 'article',
            'ul.list': 'ul',
            # Add custom mappings here
        }

    def convert_to_semantic(self, html):
        soup = BeautifulSoup(html, 'lxml')
        for selector, new_tag in self.tag_mappings.items():
            for element in soup.select(selector):
                element.name = new_tag
        return str(soup)