from flask import Flask, request, render_template, redirect, url_for, abort, json, session
app = Flask(__name__) 

import gameset
import dbdb

app.secret_key = b'aaa!111/'

@app.route('/')
def index(): 
    return render_template('main.html')
    
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

##로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        
        ret = dbdb.select_user(id, pw)
        if ret != None:
            session['user'] = id
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

##회원가입
@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']
        ret = dbdb.check_id(id)
        if ret != None:
            return '''
                    <script>
                    alert('이미 존재하는 아이디입니다.');
                    location.href='/join';
                    </script>
                    '''
        dbdb.insert_user(id, pw, name)
        return redirect(url_for('login'))

@app.route('/logout') 
def logout(): 
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/form') 
def form():
    return render_template('login.html')

    
@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET':
        return "GET 방법이다."
    else: 
        num = request.form["num"] 
        name = request.form["name"]
        dbdb.insert_data(num, name)
        return "POST로 전달된 데이터({}, {})".format(num, name) 


## 학생정보
@app.route('/getinfo')  ## JSON 파일 입출력 예시 학생 로그인
def getinfo():
    if 'user' in session:
        ret = dbdb.select_all()
        return render_template('getinfo.html', data = ret)

    return redirect(url_for('login'))

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

if __name__ == '__main__': 
    app.run(debug=True)