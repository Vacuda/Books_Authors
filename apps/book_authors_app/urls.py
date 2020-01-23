from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.books_main),

    ##books
    url(r'^books_main$', views.books_main),
    url(r'^add_book$', views.add_book),
    url(r'^delete_book$', views.delete_book),
    url(r'^view_book$', views.view_book),

    ##books - specific book
    url(r'^books_view/(?P<id>[0-9]+)$', views.books_view),
    url(r'^link_author$', views.link_author),
    url(r'^remove_author$', views.remove_author),

    ##authors
    url(r'^authors_main$', views.authors_main),
    url(r'^add_author$', views.add_author),
    url(r'^delete_author$', views.delete_author),
    url(r'^view_author$', views.view_author),

    ##authos - specific author
    url(r'^authors_view/(?P<id>[0-9]+)$', views.authors_view),
    url(r'^link_book$', views.link_book),
    url(r'^remove_book$', views.remove_book),
    ]