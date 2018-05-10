Blockchain project for registration of baby products. Implements proof of work, replication, consensus, merkle trees.
# Register all nodes 
```js

POST POST http://localhost:5001/nodes/register 
{
	"nodes": [
		"http://127.0.0.1:5002",
		"http://127.0.0.1:5003",
		"http://127.0.0.1:5004"
	]
}



POST http://localhost:5002/nodes/register 
{
	"nodes": [
		"http://127.0.0.1:5001",
		"http://127.0.0.1:5003",
		"http://127.0.0.1:5004"
	]
}

POST http://localhost:5003/nodes/register 
{
	"nodes": [
		"http://127.0.0.1:5002",
		"http://127.0.0.1:5001",
		"http://127.0.0.1:5004"
	]
}


POST http://localhost:5004/nodes/register 
{
	"nodes": [
		"http://127.0.0.1:5001",
		"http://127.0.0.1:5002",
		"http://127.0.0.1:5003"
	]
}


```

# Register all products: Front End
```js
upc: B07CRZWXQD
product: MEGNYA Leather Baby Moccasins
link: https://www.amazon.com/MEGNYA-Leather-Moccasins-Toddler-ZH0003-Brown-12-5/dp/B07BBVPSPW/ref=sr_1_1_sspa?ie=UTF8&qid=1525936891&sr=8-1-spons&keywords=baby+shoes&psc=1
quantity: 90
price: 18.99
manufacturer: MEGNYA


upc: B074P49GC8
product: Hudson Baby Animal Plush Bathrobe, Pretty Elephant
link: https://www.amazon.com/Hudson-Baby-Animal-Bathrobe-Elephant/dp/B074P49GC8/ref=sr_1_5?s=apparel&ie=UTF8&qid=1525993651&sr=1-5&nodeID=7141123011&psd=1&keywords=baby&th=1
quantity: 120
price: 10.99
manufacturer: Hudson


```

# Check to see a product with product ID
```js
http://127.0.0.1:5001/product/B07CRZWXQD

```

# Transfer a product from one owner to another
```js
upc: B07CRZWXQD
old_owner: MEGNYA
new_owner: Aditi
```

# Get transaction block by transaction 
```js
http://127.0.0.1:5001/transaction/3cc33f7e1a07784de4912c8dd702c4ddc6914051
```

# Replication on all nodes
```js
http://127.0.0.1:5002/nodes/resolve
http://127.0.0.1:5003/nodes/resolve
http://127.0.0.1:5004/nodes/resolve
```

# View full chain with all products on all nodes (check replication)
```js
http://127.0.0.1:5001/chain
http://127.0.0.1:5002/chain
http://127.0.0.1:5003/chain
http://127.0.0.1:5004/chain
```




