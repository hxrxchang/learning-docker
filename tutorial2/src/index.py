from bottle import route, run

@route('/')
def hello():
    print('1111111111111111111111111111')
    return "docker is fun!!"

run(host='0.0.0.0', port=8080, debug=True)
