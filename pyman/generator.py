from jinja2 import Environment, FileSystemLoader

def create_class_template(collection):
    
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('wrapper.txt')

    msg = template.render(name=collection.get('info',{}).get('name'), base_url="http://google.com", items=collection.get('item'))

    with open("output.py", 'w') as outfile:
        outfile.write(msg)