# Register all nodes 
```js

POST http://127.0.0.1:5001/register
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