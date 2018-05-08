from uuid import uuid4
import requests
from flask import Flask, jsonify, request, render_template

from blockchain import Blockchain

# Instantiate the Node
app = Flask(__name__, template_folder='templates')

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


# blockchain.register_node('http://127.0.0.1/5001')
# blockchain.register_node('http://127.0.0.1/5002')
# blockchain.register_node('http://127.0.0.1/5003')
# blockchain.register_node('http://127.0.0.1/5004')
# blockchain.register_node('http://127.0.0.1/5005')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/register", methods=['POST'])
def register():
    print(request.form)
    content = request.get_json()
    print("content")
    print(content)
    # TODO: create block
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    previous_hash = blockchain.hash(last_block)

    # creating a block
    block = blockchain.new_block(proof, previous_hash, content)

    # TODO: make changes to frontend to acknowledge registration
    return jsonify(block), 200
    # return render_template('index.html')


@app.route("/transfer", methods=['POST'])
def transfer():
    print(request.form)
    # TODO: backend stuff
    # TODO:make changes to html
    return render_template('index.html')


@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    # last_block = blockchain.last_block
    # last_proof = last_block['proof']
    # proof = blockchain.proof_of_work(last_proof)
    #
    # previous_hash = blockchain.hash(last_block)
    # block = blockchain.new_block(proof, previous_hash)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    # blockchain.new_transaction(
    #     sender="0",
    #     product_name="0",
    #     price=0,
    #     recipient=node_identifier,
    #     quantity=1,
    #     link="empty"
    # )
    #
    # # Forge the new Block by adding it to the chain
    # previous_hash = blockchain.hash(last_block)
    # block = blockchain.new_block(proof, previous_hash)
    #
    # response = {
    #     'message': "New Block Forged",
    #     'index': block['index'],
    #     'transactions': block['transactions'],
    #     'proof': block['proof'],
    #     'previous_hash': block['previous_hash'],
    # }
    response = requests.get(f'http://127.0.0.1:5001/chain')
    print(response)

    return jsonify(response.json()), 200


# @app.route('/transactions/new', methods=['POST'])
# def new_transaction():
#     values = request.get_json()
#
#     # Check that the required fields are in the POST'ed data
#     required = ['sender', 'product_name', 'price', 'recipient', 'quantity', 'link']
#     if not all(k in values for k in required):
#         return 'Missing values', 400
#
#     # Create a new Transaction
#     index = blockchain.new_transaction(values['sender'], values['product_name'], values['price'],
#                                        values['recipient'], values['quantity'], values['link'])
#
#     response = {'message': f'Transaction will be added to Block {index}'}
#     return jsonify(response), 201


@app.route('/transactions/<id>', methods=['POST'])
def new_transaction(id):
    values = request.get_json()
    block = blockchain.new_transaction(values['old_owner'], values['new_owner'], id)
    return jsonify(block),200


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/transact/<id>', methods=['GET'])
def new_action(id):
    #data = requests.get(f'http://127.0.0.1:5001/chain')
    response=blockchain.get_transaction(id)
    return jsonify(response),200



@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port, debug=True)
