from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render,get_object_or_404
from blogApp.models import Post,Comment
from django.views.generic import ListView, DetailView
from blogApp.forms import EmailSendForm, CommentForm

class PostListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def mail_send_view(request,post_id):
    post= get_object_or_404(Post,id=post_id,status='published')
    sent = False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject = '{} ({}) recommends you to read"{}"'.format(cd['name'],cd['email'], post.title)
            post_url = request.build_absolute_uri(post.get_absolute_url())
            message = 'Read Post At:\n{}\n\n{}\'s Comments:\n{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'abhirvablog@gmail.com',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()
    return render(request,"templates/blog/sharebymail.html",{'form':form,'post':post,'sent':sent})

def comments_view(request,year,month,day,post):
    post = get_object_or_404(Post, slug_field=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment  = None
    if request.method=='POST':
        comment_form = CommentForm(data=request.POST)
        if CommentForm.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'templates/blog/post_detail.html',{'posts':post,
                                                              'comments':comments,
                                                              'new_commment':new_comment,
                                                              'comment_form':comment_form})


























# Create your views here.
#def post_list_view(request):
    #post_list = Post.objects.all()
   # return render(request, "blog/post_list.html",{'post_list':post_list})

#def post_detail_view(request,year,month,day,post):
    #post = get_object_or_404(Post,slug_field=post,
    #                         status='published',
    #                         publish__year=year,
    #                         publish__month=month,
    #                         publish__day=day)
    #return render(request,'blog/post_detail.html',{'post':post})

#def post_list(self,request):
    #    post_list = Post.objects.all()
    #    paginator = Paginator(post_list,2)
    #    page_number = request.GET.get('page')
    #    try:
    #        post_list=paginator.page(page_number)
    #    except PageNotAnInteger:
     #       post_list=paginator.page(1)
     #   except EmptyPage:
    #        post_list=paginator.page(paginator.num_pages)
    #    return render(request,"blog/post_list.html",{'post_list':post_list})
