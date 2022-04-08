from django.shortcuts import render
import requests
from .models import Article
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

def get_articles(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=c4f60c7e47cc2ec71f09e8150081ff0e&keywords=school+safety& countries=us')
    r2 = requests.get('https://gnews.io/api/v4/search?q=school+safety&country=us&from= 2022-01-06T20:39:50Z&token=244cdfb52dcc42eec7bd1083dcd21b79')
    res = r.json()
    res2 = r2.json()
    data = res['data']
    data2 = res2['articles']
    title = []
    description = []
    image = []
    url = []
    for i in range(len(data)):
        if data[i]['title'] == None or data[i]['description'] == None or data[i]['image'] == None or data[i]['url'] == None:
            continue
        else:
            title.append(data[i]['title'])
            description.append(data[i]['description'])
            image.append(data[i]['image'])
            url.append(data[i]['url'])
    for i in range(len(data2)):
        if data2[i]['title'] == None or data2[i]['description'] == None or data2[i]['image'] == None or data2[i]['url'] == None:
            continue
        else:
            title.append(data2[i]['title'])
            description.append(data2[i]['description'])
            image.append(data2[i]['image'])
            url.append(data2[i]['url'])
    news = zip(title , description, image, url)
    return render(request, 'schoolsafetynews/main.html', {'news': news})

def post_detail(request, slug):
    template_name = 'detail.html'
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'article': article,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
