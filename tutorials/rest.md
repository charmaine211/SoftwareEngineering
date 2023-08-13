
## Testing the REST API

The application contains a REST API for the Signatures model. 
You can test the REST API with:

```
http -a admin:admin http://127.0.0.1:8000/ou/signatures/
```

and obtain a list of signatures. A user 'admin' with password 'admin'
is enabled in the application and must be used during each REST API
interaction.

