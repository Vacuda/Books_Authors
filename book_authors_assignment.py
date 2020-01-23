
Book.objects.create(title="C Sharp")
Book.objects.create(title="Java")
Book.objects.create(title="Python")
Book.objects.create(title="PHP")
Book.objects.create(title="Ruby")

Author.objects.create(first_name="Jane", last_name="Austen")
Author.objects.create(first_name="Emily", last_name="Dickinson")
Author.objects.create(first_name="Fyodor", last_name="Dostoevsky")
Author.objects.create(first_name="William", last_name="Shakespeare")
Author.objects.create(first_name="Lau", last_name="Tzu")

x=Book.objects.get(title="C Sharp")
x.title="C#"
x.save()

x=Author.objects.get(first_name="William")
x.first_name="Bill"
x.save()

x=Author.objects.first()
y=Book.objects.get(id=1)
z=Book.objects.get(id=2)
x.books.add(y)
x.books.add(z)
x.save()

##I know there are simplier ways to do the following, but I 
##am trying to challenge myself if the database was large or
##I didn't assume that the fourth author was id=4

x=Author.objects.get(id=2)
y=Book.objects.all()
counter=0
for i in y:
    counter=counter+1
    if counter <=3:
        i.author.add(x)
        i.save()
print(x.books.all())

x=Author.objects.get(id=3)
y=Book.objects.all()
counter=0
for i in y:
    counter=counter+1
    if counter <=4:
        i.author.add(x)
        i.save()
    print(x.books.all())

x=Author.objects.get(id=4)
y=Book.objects.all()
for i in y:
    i.author.add(x)
    i.save()
    print(x.books.all())

Book.objects.get(id=3).author.all()

###Hmm...You can chain everything...awesome

Book.objects.get(id=3).author.remove(Book.objects.get(id=3).author.first())

Book.objects.get(id=2).author.add(Author.objects.get(id=5))

Author.objects.get(id=3).books.all()

Book.objects.get(id=5).author.all()

###I should have named the related_name as authors, not author