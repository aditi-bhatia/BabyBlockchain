import datetime
import hashlib
import json
from time import time
from urllib.parse import urlparse

import requests


class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100, content={})

    def register_node(self, address):
        """
        Add a new node to the list of nodes
        :param address: Address of node. Eg. 'http://192.168.0.5:5000'
        """

        parsed_url = urlparse(address)
        print("PARSED URL: ")
        print(parsed_url.netloc)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: A blockchain
        :return: True if valid, False if not
        """

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """
        This is our consensus algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.
        :return: True if our chain was replaced, False if not
        """

        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False

    def new_block(self, proof, previous_hash, content):
        """
        Create a new Block in the Blockchain
        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of previous Block
        :return: New Block
        """
        if len(content):
            product_id = content['product_id']
            manufacturer = content['manufacturer'],
            product_name = content['product_name'],
            price = content['price'],
            quantity = content['quantity']

            block = {
                'index': len(self.chain) + 1,
                'timestamp': time(),
                'transactions': self.current_transactions,
                'proof': proof,
                'previous_hash': previous_hash or self.hash(self.chain[-1]),
                'product_id': product_id,
                'manufacturer': manufacturer,
                'product_name': product_name,
                'price': price,
                'quantity': quantity
            }
        else:
            # creating the genesis block
            block = {
                'index': 1,
                'timestamp': time(),
                'transactions': self.current_transactions,
                'proof': proof,
                'previous_hash': "085asad7ratte4131563",
                'product_id': 0,
                'manufacturer': 0,
                'product_name': 0,
                'price': 0,
                'quantity': 0
            }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, old_owner, new_owner, id):
        transaction = {
            'transaction_id': hashlib.sha1(
                old_owner.encode() + new_owner.encode() + str(datetime.datetime.now()).encode()).hexdigest(),
            'old_owner': old_owner,
            'new_owner': new_owner
        }

        # self.current_transactions.append(transaction)
        new_block = []
        for block in self.chain:
            print(type(block['product_id']))
            print(type(id))
            if block['product_id'] == id:
                block['transactions'].append(transaction)
                new_block = block
                break
        else:
            return "Not found"

        return new_block
        # return self.last_block['index'] + 1

    def  get_transaction(self,id):

       for block in self.chain:
           for trans in block['transactions']:
               if trans['transaction_id'] ==id:
                   test=block['transactions']
                   break

               else:
                   test="error"
       return test


    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof
        :param last_proof: Previous Proof
        :param proof: Current Proof
        :return: True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
