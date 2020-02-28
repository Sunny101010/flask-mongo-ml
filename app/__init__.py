from flask import Flask,render_template
from flask import request, jsonify
from flask_pymongo import PyMongo
import datetime
import dateutil.parser

from sklearn.externals import joblib

#app = Flask(__name__)
app = Flask(__name__,
  	static_folder = './static',
  	template_folder="./templates")
#from app import views, models

app.config['MONGO_DBNAME'] = 'ffe68dbf-7fb4-4bbe-9f72-3cd0b519caea'
app.config['MONGO_URI'] = 'mongodb://9a0c884b-3a06-42ff-972d-db78907d5727:ySIl9NWcehDYlAOxoLGMs3Dqy@42.159.80.108:27017/ffe68dbf-7fb4-4bbe-9f72-3cd0b519caea'

app.url_map.strict_slashes = False
mongo = PyMongo(app)

@app.route("/", methods=['GET','POST'])
def home_page():
    return "<h1>Hello World!</h1>"

@app.route("/rtdata", methods=['GET','POST'])
def rtdata_page():
    #rtdatas = mongo.db.getCollection('ene_rtdata').find({})
    rtdatas = mongo.db.ene_rtdata.find({})
    #rtdatas = mongo.db.ene_rtdata.find_one()
    return render_template('index2.html',rtdatas=rtdatas)

@app.route("/rawdata", methods=['GET','POST'])
def rawdata_page():
    app.logger.info('this is a string')
    tagname = request.args.get("tagname")
    app.logger.info(tagname)
    #age = request.args.get("startDate")
    my_date_str = "2020-01-01T00:00:00Z"
    starttime = dateutil.parser.parse(my_date_str)
    #starttime = datetime(2020, 1, 1)
    #starttime = datetime(2020, 1, 1, 0, 0, 0)
    #rawdatas = mongo.db.ene_rawdata.find({"tagname":"MBR:加水泵","datatime":{'$gt':starttime}})
    rawdatas = mongo.db.ene_rawdata.find({"tagname":tagname,"datatime":{'$gt':starttime}})
    #print(rawdatas)
    #db.col.find({"likes": {$gt:50}, $or: [{"by": "菜鸟教程"},{"title": "MongoDB 教程"}]}).pretty()
    return render_template('index3.html',rawdatas=rawdatas)

@app.route("/price", methods=['GET','POST'])
def houseprice():
    if(request.method == 'POST'):
        data = request.get_json()
        house_price = float(data["area"])
        lin_reg = joblib.load("./linear_reg.pkl")
        return jsonify(lin_reg.predict([[house_price]]).tolist())
    else:
        return  jsonify({"about":"Hello World"})