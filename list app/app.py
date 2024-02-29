from flask import Flask, jsonify , render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__ )# ,static_folder='static' )
uri = "mongodb+srv://sivarajc2005:22aia1083@sivarajc2005.4evmlz6.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.dbsparta

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/list', methods=['GET'])
def list_get():
    shopping = list(db.user.find({},{'_id':False}))
    files={"shop_list": shopping}
    return jsonify(files)



@app.route('/list',methods=['POST'])
def list_post():
    name=request.form['cus_name']
    email=request.form['cus_email']
    number=request.form['order_qun']
    address=request.form['cus_address']
    print(f"Received data: name={name}, email={email}, number={number}, address={address}")


    db.user.insert_one({'cus_name':name,"cus_email":email,'order_qun':number,'cus_address':address})

    return jsonify({'msg':'data added successfully'})

if __name__ =='__main__':
   app.run(debug=True)





