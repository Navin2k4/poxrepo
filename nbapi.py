# File: rest_server.py
from flask import Flask, jsonify

app = Flask(__name__)  # Fix: __name__ instead of _name_

# Sample API endpoint
@app.route('/api/devices', methods=['GET'])
def get_devices():
    devices = [
        {"id": 1, "ip": "10.0.0.1"},
        {"id": 2, "ip": "10.0.0.2"},
        {"id": 3, "ip": "10.0.0.3"}
    ]
    return jsonify(devices)

# POX will call this to start the server
def launch():
    app.run(host='0.0.0.0', port=5000, d ebug=True)


sudo apt install python3-flask curl mininet git
git clone https://github.com/noxrepo/pox.git

./pox.py 
openflow.of_01 
forwarding.l2_learning 
rest_server

sudo mn
--topo single,3
--controller remote,ip=127.0.0.1
--switch ovsk,protocols=OpenFlow13