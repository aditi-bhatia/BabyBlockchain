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

# Register all nodes: Front End
```js
upc: B07CRZWXQD
product: MEGNYA Leather Baby Moccasins
link: https://www.amazon.com/MEGNYA-Leather-Moccasins-Toddler-ZH0003-Brown-12-5/dp/B07BBVPSPW/ref=sr_1_1_sspa?ie=UTF8&qid=1525936891&sr=8-1-spons&keywords=baby+shoes&psc=1
quantity: 90
price: 18.99
manufacturer: MEGNYA


upc: B07CRZWXQD
product: MEGNYA Leather Baby Moccasins
link: https://www.amazon.com/MEGNYA-Leather-Moccasins-Toddler-ZH0003-Brown-12-5/dp/B07BBVPSPW/ref=sr_1_1_sspa?ie=UTF8&qid=1525936891&sr=8-1-spons&keywords=baby+shoes&psc=1
quantity: 90
price: 18.99
manufacturer: MEGNYA


```

