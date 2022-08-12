'''published on repl:
https://Counter.dmitriievvasili.repl.co
'''
from flask import Flask, session, request, Response
from re import findall
import logging
logging.basicConfig(level=logging.INFO)

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


@app.route('/<app>', methods=['GET'])
def index(app):
    if app =='add':
        #add string sanitaze
        count_str = findall('(\d+)', request.args.get('str'))
        if count_str == []:
            logging.info('empty string')
            return Response(svg_pixel, mimetype='image/svg+xml;charset=UTF-8')
        count_str = count_str[0]
        num = float(count_str) if count_str else 0
        if 'counter' in session:
            session['counter'] += num
            logging.info('Session counter: %d' % session['counter'])
            logging.info(f'Session: {session}')
        else:
            session['counter'] = num
            logging.info('Session counter: %d' % session['counter'])
            logging.info(f'Session: {session}')
        return Response(svg_pixel, mimetype='image/svg+xml;charset=UTF-8')
    elif app == 'res':
        if 'counter' in session:
            text_output = str(session['counter'])
            logging.info('Output: %s' % text_output)
            logging.info(f'Session: {session}')
            l = len(text_output)*10
            svg = svg_str.format(text_output, str(l))
            return Response(svg, mimetype='image/svg+xml;charset=UTF-8')
        else:
            logging.info(f'Session: {session}')
    elif app == 'pop':
        if 'counter' in session:
            logging.info('Poping counter: %s' % session['counter'])
            logging.info(f'Session: {session}')
            session.pop('counter')
    return Response(svg_pixel, mimetype='image/svg+xml;charset=UTF-8')

@app.route('/')
def welcome():
    text_output = '''Welcome!
    use svg counter to add value: /add?str=number_value_to_add + 
    use svg counter toshow result /res'''
    l = len(text_output) * 10
    svg = svg_str.format(text_output, str(l))
    return Response(svg, mimetype='image/svg+xml;charset=UTF-8')

if __name__ == '__main__':
    app.debug = True
    app.run()  #in production mode host="0.0.0.0"
    