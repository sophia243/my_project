from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.study_cafe


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/reservation', methods=['GET'])
def test_get():
    # title_receive = request.args.get('title_give')
    orders = list(db.reservation.find({},{'_id' : False}))
    return jsonify({'result': 'success', 'data': orders})


@app.route('/reservation', methods=['POST'])
def test_post():
    room_receive = request.form['room_give']
    phone_receive = request.form['phone_give']
    name_receive = request.form['name_give']
    day_receive = request.form['day_give']
    start_receive = request.form['start_give']
    finish_receive = request.form['finish_give']
    doc = {
        "room": room_receive,
        "phone": phone_receive,
        "name": name_receive,
        "day": day_receive,
        "start": start_receive,
        "finish": finish_receive
    }
    db.reservation.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '예약완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
