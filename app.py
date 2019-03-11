from flask import Flask

app = Flask(__name__)
stores = [
  {
    'name': 'My Wonderful Store',
    'items': [
      {
        'name': 'My Item',
        'price': 15.99
      }
    ]
  }
]

@app.route('/') #'http:www.google.com/'
def home():
  return "Hello, world!"


app.run(port=5000)

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
  pass
# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
  pass
# GET /store
@app.route('/store')
def get_stores():
  pass
# POST /store/<string:name>/item {name: price:}
@app.route('store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
  pass
# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  pass
