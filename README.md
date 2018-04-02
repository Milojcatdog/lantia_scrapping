# Python Flask Semilla

# Dependencias

* Install flask

```bash
$ pip install flask
$ pip install BeautifulSoup
$ pip install requests
```

# Correr Script
$ python -m python_flask_seed

# Output de flask
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 
```
### Error handling

```json
400 BAD REQUEST
{
  "error": "name is required"
}
```

## Pagina no encontrada

### Request

```
[GET, POST] /not_found HTTP/1.1
Host: localhost:5000
```

### Error handling

```json
404 NOT FOUND
{
  "error": "route not found"
}
```
