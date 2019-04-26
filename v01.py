import crawler
# django setup
import django
import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'v01.settings'
sys.path.append(os.path.abspath(os.path.dirname(__name__)))
django.setup()
#
from core.models import Page

def tf(bl):
    if bl == 'false':
        return False
    return True
    
def page_to_django(p):
    x = Page()
    x.username= p.username
    x.url = p.url
    x.insta_id = p.insta_id
    x.full_name = p.full_name
    x.country_code = p.country_code
    x.is_varified = tf(p.is_varified)
    x.is_private = tf(p.is_private)
    x.is_join_recently = tf(p.is_join_recently)
    x.is_business_account = tf(p.is_business_account)
    x.business_category_name =  p.business_category_name
    x.num_posts = int(p.num_posts)
    x.num_follower = int(p.num_follower)
    x.num_following = int(p.num_following)
    x.biography = p.biography
    x.save()

brs = crawler.Commands.start()
crawler.Commands.login(brs)

queue = ["digikalacom"]
data = {}
for i in range(10):
    head = queue[0]
    if head not in data:
        p = Crawler.Page.page(head)
        data[head] = p
        p.get_meta()
        p.get_following(brs)
        for x in p.list_following:
            queue.append(x)
        queue = queue[1:]
        print(head + " crawled :)")
        page_to_django(p)

