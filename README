I keep finding myself re-using this simple bit of code, so I thought I should open-source it, even though it's not much more than a snippet.

A SingletonModel is a django model that only ever has one record. You can't use the admin to create a new instance, or delete the existing one.

Some might argue that singleton models are an inefficient way of using a relational database, but in practice it's no biggie - most web sites have some important one-off content (eg. the Home Page), and  singleton models map well to how content editors generally think.

I suspect I have cadged some of this code from someone else (likely ex-colleague http://github.com/jphalip/), but a quick Google doesn't show up anything like this already out there. So here it is. I hope you find it useful.

Installation
------------

pip install django-singletons

There is no need to include it in INSTALLED_APPS

Example Usage
-------------

in models.py


from singleton_models.models import SingletonModel

class HomePage(SingletonModel):
    welcome = models.TextField()
    
    def __unicode__(self):
        return u"The Home Page" # something like this will make admin message strings more coherent
        
    class Meta:
        verbose_name = "Home Page" # once again this will make sure your admin UI doesn't have illogical text
        verbose_name_plural = "Home Page"


in admin.py

from singleton_models.admin import SingletonModelAdmin
from models import HomePage
        
admin.site.register(HomePage, SingletonModelAdmin)
