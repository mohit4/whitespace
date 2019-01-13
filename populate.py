import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WhiteSpace.settings')

import django
django.setup()

from django.contrib.auth.models import User
from blog.models import Post, Comment

from faker import Faker
fakegen = Faker()

def populate_whitespace(no_of_posts):
    print("Populating {} post(s)".format(no_of_posts))
    for i in range(no_of_posts):
        title = fakegen.text(max_nb_chars=100)
        text = fakegen.text(max_nb_chars=300)
        author = User.objects.get(id=1)
        p = Post(title=title, text=text, author=author)
        p.save()
    print("Populated successfully!")

if __name__ == "__main__":
    # for setting no of posts variable
    no_of_posts = 10
    if len(sys.argv) == 2:
        no_of_posts = int(sys.argv[1])
        if no_of_posts <= 0:
            print("No of posts is given negative, setting default!")
            no_of_posts = 10
    else:
        print("Usage : populate.py <no_of_posts>")
    populate_whitespace(no_of_posts)
    print("End of script!")
