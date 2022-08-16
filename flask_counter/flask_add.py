'''published on repl:
https://Counter.dmitriievvasili.repl.co
'''
from flask import Flask, request, Response
from re import findall
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'jump$in_secret!_value'

svg_pixel = '''<?xml version="1.0" encoding="utf-8"?>
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
                width="1px" height="1px" viewBox='0 0 1 1' style="border:0;">
                <line/>
            </svg>'''

svg_str = '''<?xml version="1.0" encoding="utf-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
    width="{1}" height="14"><text font-size="12" y="1em" font-family="Helvetica">{0}</text></svg> '''

NUM = {int, float}

class Counter:
    __instance_id = None
    counter = dict()
    def __new__(cls, *args, **kwargs):
        if cls.__instance_id == None:
            cls.__instance_id = super().__new__(cls)
        return cls.__instance_id
    
    def __init__(self, *args):
        if args:
            self.counter[args[0]] = 0

    def add_counter(self, name, value):
        if type(value) in NUM:
            if name in self.counter:
                self.counter[name] += value
            else:
                self.counter[name] = value
    
    def pop_counter(self, name):
        if name in self.counter:
            self.counter.pop(name)

    def get_counter(self, name):
        if name in self.counter:
            return self.counter[name]
        return None

@app.route('/', methods=['GET'])
def index():
    todo = request.args.get('do')
    cl = Counter()
    if todo =='add':
        #add string sanitaze
        count_str = findall('(\d+)', request.args.get('str'))
        name = request.args.get('name')
        if count_str == []:
            logging.info('empty string')
            return Response(svg_pixel, mimetype='image/svg+xml;charset=UTF-8')
        count_str = count_str[0]
        num = float(count_str) if count_str else 0
        if cl.get_counter(name):
            cl.add_counter(name, num)
            logging.info(f'Session add counter: {name} {num}')
        else:
            cl.add_counter(name, num)
            logging.info(f'New counter: {name} {num}')
        return Response(svg_pixel, mimetype='image/svg+xml;charset=UTF-8')
    elif todo == 'res':
        name = request.args.get('name')
        num = cl.get_counter(name)
        if num:
            text_output = str(num)
            logging.info('Output: %s' % text_output)
            l = len(text_output)*10
            svg = svg_str.format(text_output, str(l))
            return Response(svg, mimetype='image/svg+xml;charset=UTF-8')
        else:
            logging.info(f'Session with empty counter: {name} {num}')
    elif todo == 'pop':
        name = request.args.get('name')
        if cl.get_counter(name):
            logging.info('Poping counter: %s' % name)
            cl.pop_counter(name)
        return Response(svg_pixel, mimetype='image/svg+xml;charset=UTF-8')
    elif todo == '':
        text_output = '''Welcome!
            use svg counter to add value: /?do=add&name=NameCounter&str=number_value_to_add + 
            to show result /?do=res
            to clear counter /?do=pop&name=NameCounter
            '''
        l = len(text_output) * 10
        svg = svg_str.format(text_output, str(l))
        return Response(svg, mimetype='image/svg+xml;charset=UTF-8')
    return Response(svg_pixel, mimetype='image/svg+xml;charset=UTF-8')

if __name__ == '__main__':
    app.debug = True
    app.run()  #in production mode host="0.0.0.0"
    