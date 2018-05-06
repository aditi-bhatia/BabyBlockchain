## Blockchain for Product Inventory
### Team Incognito: CMPE 273, Distributed Systems

Aditi	Bhatia

Harshrajsinh	Rathod

Venkat Pushpak Gollamudi

Aravindhan	Elayakumar

Akinfemi	Akin-Aluko

## TO DO LIST

-> UI should be able to GET and POST all requests, responses and data. Connectivity code needs to be written for this (use the updated UI code I pushed -aditi)
-> FLASK API for all requests needs to be written:
--->GET by product_id
--->GET all products by a specific manufacturer
--->Transfer products [POST new transactions for retailer manufacturer ->]
--->manufacturer->retailer [GET updated retailer wallet]
--->Etc. there are probably some that I am forgetting


#### Start nodes
```js
FLASK_APP=server.py flask run --port=5001
```

```js
FLASK_APP=server.py flask run --port=5002
```

#### Register nodes
Include all other nodes in the JSON file other than the node you're already on.
For registering node 5002 on node 5001: 
```js
curl -i -X POST http://localhost:5001/nodes/register -d @register-node5001.json --header "Content-Type: application/json"
```

For registering node 5001 on node 5002: 
```js
curl -i -X POST http://localhost:5002/nodes/register -d @register-node5002.json --header "Content-Type: application/json"
```

#### Register a new item as a manufacturer node
```js
curl -i -X POST http://localhost:5001/transactions/new -d @entry.json --header "Content-Type: application/json"
```

#### Replicate/update nodes
To replicate all new changes (such as the ones made on 5001) on node 5002:
```js
curl -i -X GET http://127.0.0.1:5002/nodes/resolve
```
Run on all nodes that have not been updated.


#### Get the updated blockchain to see updates
```js
curl -i -X GET http://127.0.0.1:5001/chain
curl -i -X GET http://127.0.0.1:5001/mine
```