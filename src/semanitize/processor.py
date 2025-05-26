from .sanitizer import Sanitizer
from .semanticizer import Semanticizer

class HTMLProcessor:
    def __init__(self, sanitizer=None, semanticizer=None):
        self.sanitizer = sanitizer or Sanitizer()
        self.semanticizer = semanticizer or Semanticizer()

    def process(self, html):
        clean_html = self.sanitizer.sanitize(html)
        semantic_html = self.semanticizer.convert_to_semantic(clean_html)
        return semantic_html