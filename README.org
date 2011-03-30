* Django-quickblocks
  
** Overview
   Django Quickblocks is a plugable Django based web application. Quickblocks has been developed to be more generic
   on how contents are being integrated within web applications.

   Quickblocks key factor is how easy it is to categorize contents depending on where and how you want to display them by
   giving the users the power to use their creativity. Designing django-quickblocks we have focused on how
   contents are being displayed from thousand sites and from there we managed to make it more generic.

   Quickblocks makes content management for average general sites a blast.

** Features
   - Create quickblock types
   - Create different quicblock from quickblock type
   - Use fields of your choice (quickblocks type maybe used most of the time.)
   - Template tags that integrates quickblocks in the template on the fly
   - more...

** Download

*** From Github
    You can always get the latest version of django-quickblocks from github. Using git you can clone the django-quickblocks
    or download either zipped version within your favorite browser and put it into your project folder.

    My prefered way is to have requirements into a simple text file in the root of your project.
    We like to call it =pip-requires.txt=(your choice).
    Put =-e git+http://github.com/nyaruka/django-quickblocks.git#egg=django_quickblocks= on its own line
    and install everything in the file as following:
    #+BEGIN_EXAMPLE
    pip install -r pip-requires.txt
    #+END_EXAMPLE

** Configuration
   To enable django-quickblocks for your project edit the projects =settings.py= and add the following:
   #+BEGIN_EXAMPLE
   INSTALLED_APPS = (
       Other apps ...
       'django_reversion',
       'django_quickblocks'
   )
   #+END_EXAMPLE

   Then syncronize your database to include these apps
   #+BEGIN_EXAMPLE
   % python manage.py syncdb
   #+END_EXAMPLE

** Getting Started
   Once you have quickblock types and quickblocks it is time to display them in the template. There is where template tags comes into play.

   This app offers one templatetag =load_quickblocks=. Which does a query for all active Quickblock objects for the passed QuickblockType
   identified by its slug. You can then access that list within your context.

   It accepts one parameter the =slug=

*** Syntax
   #+BEGIN_EXAMPLE
   {% load_quickblocks [name]  %}
   #+END_EXAMPLE

*** Example usage:
   #+BEGIN_EXAMPLE
   {% load_quickblocks  %}
   ...
   {% load_quickblocks "home_banner_blocks" %}
   ...
   #+END_EXAMPLE
**** Note:
     You may also use the shortcut tag =load-qbs= as ={% load_qbs "home_banner_blocks" %}=

     If you specify a slug that hos noi associated quicl block, then an error message will be inserted in your
     template. You man change this text by setting the value fothe =QUICKBLOCK_IF_INVALID= in your settings
