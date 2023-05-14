# bfactory

[![](https://img.shields.io/pypi/v/bfactory.svg?maxAge=3600)](https://pypi.org/project/bfactory/)


## Build a API from a json manifest


## Install

To deploy this project run

```bash
  pip install bfactory
```


## Create a manifest file

We need to create a manifest.json.

```text
example: /tmp/manifest.json 
```


```json
{
    "name":"Todo App",
    "version": "1",
    "auth": "jwt",
    
    "database":{
        "type":"sqlite",
        "name":"database.sqlite",
        "username":"",
        "password":"",
        "host":"",
        "port":""        
    },
    "schema":
        [
            {   
                "name":"Tarea",
                "perm":"700",
                "attrs":[
                    {
                        "name":"descripcion",
                        "type":"str",
                        "req":true,
                        "default":""
                    },
                    {
                        "name":"realizada",
                        "type":"bool",
                        "req":false,
                        "default":false
                    },
                    {
                        "name":"owner",
                        "type":"User",
                        "req":true,
                        "default":""
                    }
                ]
            }
        ]
}

```


## Run

```bash
  bfactory -m /tmp/manifest.json  -p /tmp/todo -f  --run
```


## Help

 
```bash
bfactory --help
```

## Todo

we are continually improving all types of attributes that are used in the model. Currently there is only support for the ones listed above and each of them also needs to be improved. In version 1.0 we will have full support and better documentation. Thanks for understanding. Balances and may the force be with you


## License

[![MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)  
