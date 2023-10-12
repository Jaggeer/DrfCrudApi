## Installation guide
1. Clone repo
2. Create env. with python ``` -m venv env ```
3. Activate env with ``` run activate.bat in env/Scripts ```
4. Install packages with ``` pip install -r requirements.txt ```
5. Open store/settings.py and change DB settings desired ones
6. Run ``` python manage.py migrate ``` to migrate models to your DB
7. Run ``` python manage.py createsuperuser ``` to create a superuser to log in to the admin panel
8. Run ``` python manage.py runsever ``` to run sever

## Structure of project

### "storeapp/models.py"

In "storeapp/models.py" we have 3 models:
1. Product model, which has 6 fields:
   - title as string, the max length of which is 255
   - price as foreign key to Price model
   - amount as positive int
   - barcode as positive int
   - updateDate as date field
   - productType as foreign key to ProductType model
2. ProductType model, which has 2 fields:
   - title as string, the max length of which is 255
   - description as string
3. Price model, which has 2 fields:
   - currency as string, the max length of which is 1 and represents currency character
   - price as float

### "storeapp/views.py"
In "storeapp/views.py" there is 3 ViewSets: ProductsViewSet, ProductTypeViewSet and PriceViewSet, which inheirit from base class viewsets.ModelViewSet. But in ProductsViewSet we have additional method, which decrease amount of product on specified value taken from parameter.

### "storeapp/serializers.py"
In "storeapp/serializers.py" we have 3 serializers, which are basic ModelSerializers, which take the specified model and serialize all fields of this model.

### "storeapp/admin.py"
In "storeapp/admin.py" we register our models to admin panel and add additional class ProductAdmin to realize search by product title and display updateDate.

### "store/urls.py"
Also there is "store/urls.py" file, in which was created 3 routers for each model we have and defined paths to interact with api.

## How to interact with api

I'll describe separately for each model:
1. Product
   - GET request to ``` 127.0.0.1/api/product ``` to get json list of products
   - GET request to ``` 127.0.0.1/api/product/<pk> ``` to get specific product by id
   - POST request to ``` 127.0.0.1/api/product/ ``` with json, which specifies fields of product model (don't need to specify udateTime, it is auto field), to add new product
   - PATCH request to ``` 127.0.0.1/api/product/<pk> ``` with json, to update specific property of product
   - DELETE request to ``` 127.0.0.1/api/product/<pk> ``` to delete product
   - PATCH request to ``` 127.0.0.1/api/product/<pk>/updateAmount/<decreaseValue> ``` to decrease amount of product by decreaseValue
2. Price
   - GET request to ``` 127.0.0.1/api/price ``` to get json list of prices
   - GET request to ``` 127.0.0.1/api/price/<pk> ``` to get specific price by id
   - POST request to ``` 127.0.0.1/api/price/ ``` with json, which specifies fields of price model, to add new price
   - PATCH request to ``` 127.0.0.1/api/price/<pk> ``` with json, to update specific property of price
   - DELETE request to ``` 127.0.0.1/api/price/<pk> ``` to delete price
3. ProductType
   - GET request to ``` 127.0.0.1/api/productType ``` to get json list of productTypes
   - GET request to ``` 127.0.0.1/api/productType/<pk> ``` to get specific productType by id
   - POST request to ``` 127.0.0.1/api/productType/ ``` with json, which specifies fields of productType model, to add new productType
   - PATCH request to ``` 127.0.0.1/api/productType/<pk> ``` with json, to update specific property of productType
   - DELETE request to ``` 127.0.0.1/api/productType/<pk> ``` to delete productType

You can also perform these actions from admin panel.