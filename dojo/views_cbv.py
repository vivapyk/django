from django.views.generic import View, TemplateView
from django.http import HttpResponse


class PostListView1(View):
    def get(self, request):
        name = '영근'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)
    def get_template_string(self):
        return '''
            <h1>AskDjango</h1>
            <p>{name}</p>
            <p>장고만세</p>
        '''

post_list1 = PostListView1.as_view()


class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_cotext_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context
post_list2 = PostListView2.as_view()



# class PostView3(object):
#     pass
#
#
# class PostView4(object):
#     pass

