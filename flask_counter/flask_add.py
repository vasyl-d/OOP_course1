from flask import Flask, session, request, Response

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
        count_str = request.args.get('str')
        #add string sanitaze
        num = float(count_str) if count_str else 0
        if 'counter' in session:
            session['counter'] += num
        else:
            session['counter'] = num
        return Response(svg_pixel, mimetype='image/svg+xml;charset=UTF-8')
    elif app == 'res':
        if 'counter' in session:
            text_output = str(session['counter'])
      
            session.pop('counter')
            l = len(text_output)*10
            svg = svg_str.format(text_output, str(l))
            return Response(svg, mimetype='image/svg+xml;charset=UTF-8')
    return Response(svg_pixel, mimetype='image/svg+xml;charset=UTF-8')

@app.route('/')
def welcome():
    text_output = '''Welcome!
    use svg counter to add value: /add?str=number_value_to_add + 
        \n
    use svg counter toshow result /res'''
    l = len(text_output) * 10
    svg = svg_str.format(text_output, str(l))
    return Response(svg, mimetype='image/svg+xml;charset=UTF-8')

if __name__ == '__main__':
    app.debug = False
    app.run()