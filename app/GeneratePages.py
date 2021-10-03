from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader = FileSystemLoader('templates', encoding='utf8'),
    trim_blocks = True
)

def generate():
    tmpl = env.get_template('sample.j2')

    params = {'name':'田中'}
    out = tmpl.render(params)
    print(out)

if __name__ == '__main__':
    generate()