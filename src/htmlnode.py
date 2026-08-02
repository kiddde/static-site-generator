class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        html = ""
        if self.props is None or self.props == "":
            return ""
        for item in self.props:
            html += f' {item}="{self.props[item]}" '
        return html
    def __repr__(self):
        return f'Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}\n'
