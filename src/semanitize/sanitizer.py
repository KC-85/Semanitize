import bleach

class Sanitizer:
    def __init__(self, allowed_tags=None, allowed_attributes=None):
        self.allowed_tags = allowed_tags or bleach.sanitizer.allowed_tags
        self.allowed_attributes = allowed_attributes or bleach.sanitizer.allowed_attributes

    def sanitize(self, html):
        return bleach.clean(html, tags=self.allowed_tags, attributes=self.allowed_attributes)
