long_description = """
# Django Fine Search

https://github.com/bellomusodiq/dj-fine-search

https://pypi.org/project/dj-fine-search/


Django fine search is package that performs search based on keywords. It allows word flexibility
for performing filter in a queryset. 
e.g. The native Model.object.filter(title__icontains='hello world') will return queryset of 
objects that contains substring "hello world", if the "world" comes before the "hello", the 
objects would not be found. Django fine search improves that, Django fine search will include
all objects that has substring "hello world".

```
class MyModel(models.Model):    
    title = models.Charfield(max_length=200)
    text = models.TextField()
    ...
```



perform_search takes in the model, search_text and fields

model: Model class, the model to perform filter on

search_text: string, the query that will be used for the filtering

fields: list or tuple of the fields of the models that the search will be performed on e.g. title and text above

perform_search function returns a list of model objects

~~~
>> pip install dj-fine-search
~~~

```
from fine_search.fine_search import perform_search
# model based search
queryset = perform_search(model=MyModel, search_text='hello world', fields=["title", "text"])
```

~~~
# assume we have the queryset below are result of MyModel.objects.all()
queryset = [{"id": 1, "title": "some title", "text": "hello world, how are you"},
            {"id": 2, "title": "some title2", "text": "the world is good"}, 
            {"id": 3, "title": "some title3", "text": "world hello there, hello"}] 
# if we run perform_search on the MyModel with search_text='hello world' and fields=['title', 'fields']

# it will return all the queries
~~~

it is also possible to perform search on queryset. e.g. queryset that has been filter initialy

~~~
from fine_search.fine_search import perform_search_queryset

q = MyModel.objects.all()

queryset = perform_serach_queryset(queryset=q, search_text='hello world', fields=["title", "text"])
~~~

"""
