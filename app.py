from flask import Flask, request, render_template, redirect, url_for, abort, json, session
app = Flask(__name__) 

import gameset
import dbdb
app.secret_key = b'ee3aaa!111/'

@app.route('/')
def index(): 
    return 'mainpage'
    
@app.route('/hello')
def hello(): 
    return 'Hello, World!'

@app.route('/hello/<name>') ## 철권 캐릭터 입력
def hellovar(name): 
    character = gameset.character(name)
    return render_template('gameS.html', data=character)

## @app.route('/game')
##def gameS():
##    with open("static/save.txt", "r", encoding='utf-8') as f:
##        data = f.read()
##        character = json.loads(data)
##    return "{} 기술을 사용하여 공격합니다.".format(character["skill"][0])

@app.route('/input/<int:num>')
def input(num):
        if num == 1:
            with open("static/save.txt", "r", encoding='utf-8') as f:
                data = f.read()
                character = json.loads(data)
            return "{} 기술을 사용하여 승리합니다.".format(character["skill"][0])
        elif num == 2:
            with open("static/save.txt", "r", encoding='utf-8') as f:
                data = f.read()
                character = json.loads(data)
            return "{} 기술을 사용하여 승리합니다.".format(character["skill"][1])
        elif num == 3:
            with open("static/save.txt", "r", encoding='utf-8') as f:
                data = f.read()
                character = json.loads(data)
            return "{} 기술을 사용하여 승리합니다.".format(character["skill"][2])
        elif num == 4:
            return "기권하여 패배합니다."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        
        if id == 'abc' and pw == '1234':
            session['user'] =id
            return '''
                <script> alert("안녕하세요 {}님")
                location.href = "/form"
                </script>
            '''.format(id)
            # return redirect(url_for('form'))
        else:
            return "아이디 또는 패스워드를 확인하세요"

@app.route('/logout') 
def logout(): 
    session.pop('user', None)
    return redirect(url_for('form'))

@app.route('/form') 
def form():
    if 'user' in session: 
        return render_template('naver.html') 
    return redirect(url_for('login'))

    
@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET': # args_dict = request.args.to_dict() # print(args_dict) 
        return "GET 방법이다."
    else: 
        num = request.form["num"] 
        name = request.form["name"]
        dbdb.insert_data(num, name)
        return "POST로 전달된 데이터({}, {})".format(num, name) 

@app.route('/getinfo')  ## JSON 파일 입출력 예시 학생 로그인
def getinfo(): 
    ret = dbdb.select_all()
    print(ret)
    return render_template('getinfo.html', data=ret)
    # return '번호 : {}, 이름 : {}'.format(ret[0], ret[1])

@app.route('/move/<site>')
def insite(site):
    if site == 'naver':
        return redirect(url_for('naver'))
    elif site == 'daum':
        return redirect(url_for('daum'))
    else:
        abort(404)
        # return '없는 페이지입니다.

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL 확인하세요", 404

@app.route('/naver')
def naver(): 
    return redirect("https://www.naver.com/")

@app.route('/daum')
def daum():
    return redirect("https://www.daum.net/")

@app.route('/img')
def img():
    return render_template('image.html')

if __name__ == '__main__': 
    app.run(debug=True)