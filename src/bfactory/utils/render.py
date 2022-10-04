from typing import Dict
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("bfactory.core"),
    autoescape=select_autoescape()
)


def render_to_file(template: str, file_name: str, values: Dict) -> str:
    
    res = ""

    template = env.get_template(template)
    
    res = template.render(values)

    with open(file_name, 'w+') as f:
        f.writelines(res)
        f.close()
    
