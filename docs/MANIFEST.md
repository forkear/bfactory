# bfactory/ manifest.json


## Manifest example 


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


# Schema

In schema we define our models

```
"schema": [  ]   
```

# Model

In the model we only have to define its name and its attributes

```
{ 
    "name":"Model Name",
    "attrs":[ ] 
}              
```

#  (attrs) Model Fields

The fields are a json object that has as attributes the name, the field type, if it is required and other attributes that will vary according to the type of field used.

```
{
    "name":"NAME",
    "type":"TYPE",
    "req":REQ,
    ...
    ...
    ...
}
```

For example, if we use a field type "fk" that corresponds to a relationship to another object in our model (ForeignKey), we have to add the fk attribute and give it the name of the object to which we are going to reference as a value.

This example is as follows:

```
{
    "name":"author",
    "type":"fk",
    "fk": "Author"
    "req":true,
}
```



## (TYPE) Fields Type


Below is a table with all the types of fields currently supported by bfactory


| NAME     | Django Model field    |
| ---------| ----------------------| 
| str      | CharField             |
| text     | TextField             |
| bool     | BooleanField          |
| user     | ForeignKey            |
| owner    | ForeignKey            |
| int      | IntegerField          |
| pint     | PositiveIntegerField  |
| decimal  | DecimalField          |
| fk       | ForeignKey            |
| datetime | DateTimeField         |
| date     | DateField             |

### Additional attributes:


<br>

## str

| Name     |  Description  | Value          |
| ---------|---------------|----------------| 
| default  |  Default value| "String"


## text

| Name     |  Description  | Value          |
| ---------|---------------|----------------| 
| default  |  Default value| "String"


## bool

| Name     |  Description  | Value          |
| ---------|---------------|----------------| 
| default  |  Default value| true/false

## fk  

| Name     |  Description                      |   Value          |
| ---------|-----------------------------------|------------------| 
| default  | the name of the object it relates | "NameOfTheModel" |


## datetime 

| Name      |  Description                      |   Value          |
| ----------|-----------------------------------|------------------| 
| auto_now  | the default date and time | true/false  |

## date 

| Name      |  Description                      |   Value          |
| ----------|-----------------------------------|------------------| 
| auto_now  | the default date and time | true/false  |


## user     

## owner

## int      

## pint     

## decimal  
